"""
Directus API client for managing ATIS collections
"""
import requests
import json
from typing import Optional, Dict, Any, List
from config import DIRECTUS_URL, DIRECTUS_EMAIL, DIRECTUS_PASSWORD


class DirectusClient:
    def __init__(self):
        self.base_url = DIRECTUS_URL
        self.token: Optional[str] = None
        self.refresh_token: Optional[str] = None
    
    def login(self) -> bool:
        """Authenticate with Directus and get access token."""
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={"email": DIRECTUS_EMAIL, "password": DIRECTUS_PASSWORD}
        )
        if response.status_code == 200:
            data = response.json()["data"]
            self.token = data["access_token"]
            self.refresh_token = data["refresh_token"]
            print("✓ Successfully authenticated with Directus")
            return True
        else:
            print(f"✗ Authentication failed: {response.json()}")
            return False
    
    def _headers(self) -> Dict[str, str]:
        """Get headers with authorization token."""
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def refresh_auth(self) -> bool:
        """Refresh the access token."""
        response = requests.post(
            f"{self.base_url}/auth/refresh",
            json={"refresh_token": self.refresh_token}
        )
        if response.status_code == 200:
            data = response.json()["data"]
            self.token = data["access_token"]
            self.refresh_token = data["refresh_token"]
            return True
        return False
    
    def get_collections(self) -> List[Dict]:
        """Get all collections."""
        response = requests.get(
            f"{self.base_url}/collections",
            headers=self._headers()
        )
        if response.status_code == 200:
            return response.json()["data"]
        return []
    
    def collection_exists(self, collection_name: str) -> bool:
        """Check if a collection exists."""
        collections = self.get_collections()
        return any(c["collection"] == collection_name for c in collections)
    
    def get_fields(self, collection: str) -> List[Dict]:
        """Get all fields for a collection."""
        response = requests.get(
            f"{self.base_url}/fields/{collection}",
            headers=self._headers()
        )
        if response.status_code == 200:
            return response.json()["data"]
        return []
    
    def field_exists(self, collection: str, field_name: str) -> bool:
        """Check if a field exists in a collection."""
        fields = self.get_fields(collection)
        return any(f["field"] == field_name for f in fields)
    
    def create_collection(self, collection_config: Dict) -> bool:
        """Create a new collection."""
        response = requests.post(
            f"{self.base_url}/collections",
            headers=self._headers(),
            json=collection_config
        )
        if response.status_code in [200, 204]:
            print(f"✓ Created collection: {collection_config['collection']}")
            return True
        else:
            print(f"✗ Failed to create collection: {response.json()}")
            return False
    
    def create_field(self, collection: str, field_config: Dict) -> bool:
        """Create a new field in a collection."""
        response = requests.post(
            f"{self.base_url}/fields/{collection}",
            headers=self._headers(),
            json=field_config
        )
        if response.status_code in [200, 204]:
            print(f"  ✓ Created field: {collection}.{field_config['field']}")
            return True
        else:
            error_msg = response.json() if response.text else "Unknown error"
            print(f"  ✗ Failed to create field {field_config['field']}: {error_msg}")
            return False
    
    def create_relation(self, relation_config: Dict) -> bool:
        """Create a relation between collections."""
        response = requests.post(
            f"{self.base_url}/relations",
            headers=self._headers(),
            json=relation_config
        )
        if response.status_code in [200, 204]:
            print(f"✓ Created relation: {relation_config['collection']}.{relation_config['field']}")
            return True
        else:
            print(f"✗ Failed to create relation: {response.json()}")
            return False
    
    def insert_item(self, collection: str, item: Dict) -> Optional[Dict]:
        """Insert a single item into a collection."""
        response = requests.post(
            f"{self.base_url}/items/{collection}",
            headers=self._headers(),
            json=item
        )
        if response.status_code in [200, 204]:
            return response.json().get("data")
        else:
            print(f"✗ Failed to insert item: {response.json()}")
            return None
    
    def insert_items(self, collection: str, items: List[Dict]) -> bool:
        """Insert multiple items into a collection."""
        response = requests.post(
            f"{self.base_url}/items/{collection}",
            headers=self._headers(),
            json=items
        )
        if response.status_code in [200, 204]:
            print(f"✓ Inserted {len(items)} items into {collection}")
            return True
        else:
            print(f"✗ Failed to insert items: {response.json()}")
            return False
    
    def get_items(self, collection: str, limit: int = -1) -> List[Dict]:
        """Get items from a collection."""
        params = {"limit": limit} if limit > 0 else {}
        response = requests.get(
            f"{self.base_url}/items/{collection}",
            headers=self._headers(),
            params=params
        )
        if response.status_code == 200:
            return response.json()["data"]
        return []
    
    def delete_items(self, collection: str, ids: List[int]) -> bool:
        """Delete items from a collection by IDs."""
        response = requests.delete(
            f"{self.base_url}/items/{collection}",
            headers=self._headers(),
            json=ids
        )
        return response.status_code in [200, 204]
    
    def clear_collection(self, collection: str) -> bool:
        """Remove all items from a collection."""
        items = self.get_items(collection, limit=-1)
        if not items:
            return True
        ids = [item["id"] for item in items]
        return self.delete_items(collection, ids)


def setup_airport_fields(client: DirectusClient) -> None:
    """Add missing fields to the airport collection."""
    print("\n📦 Setting up airport collection fields...")
    
    fields_to_add = [
        {
            "field": "city",
            "type": "string",
            "meta": {
                "interface": "input",
                "special": None,
                "required": False
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "country",
            "type": "string",
            "meta": {
                "interface": "select-dropdown",
                "options": {
                    "choices": [
                        {"text": "Germany", "value": "DE"},
                        {"text": "Austria", "value": "AT"},
                        {"text": "Switzerland", "value": "CH"}
                    ]
                },
                "special": None,
                "required": False
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "elevation_ft",
            "type": "integer",
            "meta": {
                "interface": "input",
                "special": None,
                "required": False,
                "note": "Airport elevation in feet"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "transition_altitude",
            "type": "integer",
            "meta": {
                "interface": "input",
                "special": None,
                "required": False,
                "note": "Transition altitude in feet (typically 5000 for DACH)"
            },
            "schema": {
                "is_nullable": True,
                "default_value": 5000
            }
        },
        {
            "field": "runways",
            "type": "json",
            "meta": {
                "interface": "input-code",
                "options": {
                    "language": "json"
                },
                "special": ["cast-json"],
                "required": False,
                "note": "JSON array of runway configurations"
            },
            "schema": {
                "is_nullable": True
            }
        }
    ]
    
    for field in fields_to_add:
        if not client.field_exists("airport", field["field"]):
            client.create_field("airport", field)
        else:
            print(f"  - Field already exists: airport.{field['field']}")


def setup_atis_entries_collection(client: DirectusClient) -> None:
    """Create the atis_entries collection with all fields."""
    print("\n📦 Setting up atis_entries collection...")
    
    if not client.collection_exists("atis_entries"):
        collection_config = {
            "collection": "atis_entries",
            "meta": {
                "collection": "atis_entries",
                "icon": "radio",
                "note": "Generated ATIS practice entries",
                "hidden": False,
                "singleton": False,
                "sort": 4,
                "group": "Generation_Components"
            },
            "schema": {},
            "fields": [
                {
                    "field": "id",
                    "type": "integer",
                    "meta": {
                        "hidden": True,
                        "interface": "input",
                        "readonly": True
                    },
                    "schema": {
                        "is_primary_key": True,
                        "has_auto_increment": True
                    }
                }
            ]
        }
        client.create_collection(collection_config)
    
    # Define all fields for atis_entries
    fields = [
        {
            "field": "airport",
            "type": "integer",
            "meta": {
                "interface": "select-dropdown-m2o",
                "special": ["m2o"],
                "required": True,
                "display": "related-values",
                "display_options": {"template": "{{icao}} - {{name}}"}
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "information_letter",
            "type": "string",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "NATO phonetic (Alpha, Bravo, etc.)"
            },
            "schema": {
                "max_length": 20,
                "is_nullable": False
            }
        },
        {
            "field": "observation_time",
            "type": "dateTime",
            "meta": {
                "interface": "datetime",
                "special": ["cast-datetime"],
                "required": True,
                "note": "Observation time (Zulu)"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "wind_direction",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "Wind direction in degrees (0-360, or 0 for variable/calm)"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "wind_speed",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "Wind speed in knots"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "wind_gust",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": False,
                "note": "Gust speed in knots (if applicable)"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "wind_variable_from",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": False,
                "note": "Variable wind from direction"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "wind_variable_to",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": False,
                "note": "Variable wind to direction"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "visibility_meters",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "Visibility in meters (9999 = 10km+)"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "rvr",
            "type": "json",
            "meta": {
                "interface": "input-code",
                "options": {"language": "json"},
                "special": ["cast-json"],
                "required": False,
                "note": "Runway Visual Range per runway"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "weather_phenomena",
            "type": "json",
            "meta": {
                "interface": "input-code",
                "options": {"language": "json"},
                "special": ["cast-json"],
                "required": False,
                "note": "Array of weather codes (RA, SN, BR, etc.)"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "clouds",
            "type": "json",
            "meta": {
                "interface": "input-code",
                "options": {"language": "json"},
                "special": ["cast-json"],
                "required": False,
                "note": "Array of cloud layers {type, height_ft, cb}"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "cavok",
            "type": "boolean",
            "meta": {
                "interface": "boolean",
                "required": False,
                "note": "Ceiling And Visibility OK"
            },
            "schema": {
                "is_nullable": True,
                "default_value": False
            }
        },
        {
            "field": "temperature",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "Temperature in Celsius"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "dewpoint",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "Dewpoint in Celsius"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "qnh",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "QNH in hPa"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "active_runways",
            "type": "json",
            "meta": {
                "interface": "input-code",
                "options": {"language": "json"},
                "special": ["cast-json"],
                "required": True,
                "note": "{arrival: [], departure: []}"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "approach_type",
            "type": "string",
            "meta": {
                "interface": "select-dropdown",
                "options": {
                    "choices": [
                        {"text": "ILS", "value": "ILS"},
                        {"text": "ILS CAT II", "value": "ILS CAT II"},
                        {"text": "ILS CAT III", "value": "ILS CAT III"},
                        {"text": "VOR", "value": "VOR"},
                        {"text": "RNAV", "value": "RNAV"},
                        {"text": "RNAV (GPS)", "value": "RNAV (GPS)"},
                        {"text": "NDB", "value": "NDB"},
                        {"text": "Visual", "value": "Visual"}
                    ]
                },
                "required": True
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "transition_level",
            "type": "integer",
            "meta": {
                "interface": "input",
                "required": True,
                "note": "Transition Level (e.g., 70, 80)"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "remarks",
            "type": "text",
            "meta": {
                "interface": "input-multiline",
                "required": False,
                "note": "NOTAMs, special information"
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "full_text",
            "type": "text",
            "meta": {
                "interface": "input-multiline",
                "required": True,
                "note": "Complete ATIS readout text"
            },
            "schema": {
                "is_nullable": False
            }
        },
        {
            "field": "difficulty",
            "type": "string",
            "meta": {
                "interface": "select-dropdown",
                "options": {
                    "choices": [
                        {"text": "Super Easy", "value": "super_easy"},
                        {"text": "Easy", "value": "easy"},
                        {"text": "Medium", "value": "medium"},
                        {"text": "Hard", "value": "hard"}
                    ]
                },
                "required": True,
                "note": "Difficulty level for practice progression"
            },
            "schema": {
                "default_value": "medium",
                "is_nullable": False
            }
        },
        {
            "field": "date_created",
            "type": "timestamp",
            "meta": {
                "interface": "datetime",
                "special": ["date-created", "cast-timestamp"],
                "readonly": True,
                "hidden": True
            },
            "schema": {
                "is_nullable": True
            }
        },
        {
            "field": "user_created",
            "type": "uuid",
            "meta": {
                "interface": "select-dropdown-m2o",
                "special": ["user-created"],
                "readonly": True,
                "hidden": True
            },
            "schema": {
                "is_nullable": True
            }
        }
    ]
    
    for field in fields:
        if not client.field_exists("atis_entries", field["field"]):
            client.create_field("atis_entries", field)
        else:
            print(f"  - Field already exists: atis_entries.{field['field']}")
    
    # Create relation from atis_entries.airport to airport
    client.create_relation({
        "collection": "atis_entries",
        "field": "airport",
        "related_collection": "airport"
    })


def setup_schema(client: DirectusClient) -> None:
    """Set up the complete schema for ATIS generation."""
    setup_airport_fields(client)
    setup_atis_entries_collection(client)
    print("\n✅ Schema setup complete!")


if __name__ == "__main__":
    client = DirectusClient()
    if client.login():
        setup_schema(client)
