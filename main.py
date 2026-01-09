"""
Main script to set up Directus schema and generate ATIS entries
"""
import time
from typing import Dict, List
from directus_client import DirectusClient, setup_schema
from generator import ATISGenerator
from data import DACH_AIRPORTS
from config import NUM_ATIS_TO_GENERATE


def deduplicate_airports(airports: List[Dict]) -> List[Dict]:
    """Remove duplicate airports based on ICAO code."""
    seen = set()
    unique = []
    for airport in airports:
        if airport["icao"] not in seen:
            seen.add(airport["icao"])
            unique.append(airport)
    return unique


def populate_airports(client: DirectusClient) -> Dict[str, int]:
    """Populate the airport collection with DACH airports.
    Returns a mapping of ICAO code to Directus ID.
    """
    print("\n✈️ Populating airports...")
    
    # Check existing airports
    existing = client.get_items("airport")
    existing_icao = {a.get("icao"): a["id"] for a in existing if a.get("icao")}
    
    if existing_icao:
        print(f"  Found {len(existing_icao)} existing airports")
    
    # Prepare airports to insert
    airports_to_insert = []
    unique_airports = deduplicate_airports(DACH_AIRPORTS)
    
    for airport in unique_airports:
        if airport["icao"] not in existing_icao:
            airports_to_insert.append({
                "icao": airport["icao"],
                "name": airport["name"],
                "city": airport.get("city"),
                "country": airport.get("country"),
                "elevation_ft": airport.get("elevation_ft"),
                "transition_altitude": airport.get("transition_altitude", 5000),
                "default_freq": airport.get("default_freq"),
                "runways": airport.get("runways")
            })
    
    if airports_to_insert:
        # Insert in batches to avoid timeout
        batch_size = 10
        for i in range(0, len(airports_to_insert), batch_size):
            batch = airports_to_insert[i:i+batch_size]
            client.insert_items("airport", batch)
            time.sleep(0.5)  # Small delay between batches
        
        # Refresh the mapping
        existing = client.get_items("airport")
        existing_icao = {a.get("icao"): a["id"] for a in existing if a.get("icao")}
    
    print(f"  ✓ Total airports in database: {len(existing_icao)}")
    return existing_icao


def generate_atis_entries(client: DirectusClient, airport_mapping: Dict[str, int], 
                          count: int = 500) -> None:
    """Generate and insert ATIS entries with balanced difficulty distribution."""
    print(f"\n📻 Generating {count} ATIS entries...")
    
    generator = ATISGenerator()
    
    # Four difficulty tiers with weighted distribution
    # 20% super_easy, 30% easy, 35% medium, 15% hard
    difficulties = ["super_easy", "easy", "medium", "hard"]
    difficulty_weights = [0.20, 0.30, 0.35, 0.15]
    
    entries = []
    difficulty_counts = {d: 0 for d in difficulties}
    
    for i in range(count):
        # Select difficulty based on weights
        difficulty = random.choices(difficulties, difficulty_weights)[0]
        difficulty_counts[difficulty] += 1
        
        # Select a random airport that exists in the database
        valid_airports = [a for a in DACH_AIRPORTS if a["icao"] in airport_mapping]
        if not valid_airports:
            print("  ✗ No valid airports found in database!")
            return
        
        airport = random.choice(valid_airports)
        airport_id = airport_mapping[airport["icao"]]
        
        # Generate ATIS
        atis_data = generator.generate_atis(airport=airport, difficulty=difficulty)
        entry = generator.to_directus_format(atis_data, airport_id)
        entries.append(entry)
        
        # Progress indicator
        if (i + 1) % 50 == 0:
            print(f"  Generated {i + 1}/{count} entries...")
    
    # Show distribution
    print(f"\n  Difficulty distribution:")
    for diff, cnt in difficulty_counts.items():
        pct = (cnt / count) * 100
        print(f"    {diff.replace('_', ' ').title()}: {cnt} ({pct:.1f}%)")
    
    # Insert in batches
    print(f"\n📤 Uploading entries to Directus...")
    batch_size = 25
    success_count = 0
    
    for i in range(0, len(entries), batch_size):
        batch = entries[i:i+batch_size]
        try:
            if client.insert_items("atis_entries", batch):
                success_count += len(batch)
        except Exception as e:
            print(f"  ✗ Error inserting batch: {e}")
        
        # Progress and rate limiting
        if (i + batch_size) % 100 == 0:
            print(f"  Uploaded {min(i + batch_size, len(entries))}/{len(entries)} entries...")
        time.sleep(0.3)
    
    print(f"  ✓ Successfully inserted {success_count} ATIS entries")


import random  # Add this at the top


def main():
    """Main entry point."""
    print("=" * 60)
    print("ATIS Generator for Directus")
    print("=" * 60)
    
    # Initialize client
    client = DirectusClient()
    
    if not client.login():
        print("Failed to authenticate. Please check your credentials.")
        return
    
    # Step 1: Set up schema
    print("\n📋 Step 1: Setting up database schema...")
    setup_schema(client)
    
    # Refresh auth token (in case setup took a while)
    client.refresh_auth()
    
    # Step 2: Populate airports
    print("\n📋 Step 2: Populating airports...")
    airport_mapping = populate_airports(client)
    
    if not airport_mapping:
        print("No airports found. Cannot generate ATIS entries.")
        return
    
    # Refresh auth token
    client.refresh_auth()
    
    # Step 3: Generate ATIS entries
    print(f"\n📋 Step 3: Generating {NUM_ATIS_TO_GENERATE} ATIS entries...")
    generate_atis_entries(client, airport_mapping, NUM_ATIS_TO_GENERATE)
    
    print("\n" + "=" * 60)
    print("✅ ATIS generation complete!")
    print("=" * 60)
    print(f"\nYou can now view your data at: {client.base_url}")
    print("Collections created/updated:")
    print("  - airport (DACH airports with runway data)")
    print("  - atis_entries (generated ATIS practice entries)")


if __name__ == "__main__":
    main()
