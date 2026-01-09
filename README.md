# ATIS Generator for Aviation Practice

A Python tool that generates realistic ATIS (Automatic Terminal Information Service) messages for aviation training and practice. Designed for the DACH region (Germany, Austria, Switzerland) using ICAO standards.

## Features

- **37 DACH Region Airports** with accurate runway configurations
- **4-Tier Difficulty System** for progressive learning:
  - 🟢 **Super Easy**: Perfect CAVOK conditions, simple format for learning ATIS structure
  - 🟡 **Easy**: Good weather with minor variations, building confidence
  - 🟠 **Medium**: Realistic operational conditions, developing proficiency
  - 🔴 **Hard**: Challenging weather with low visibility, RVR, complex remarks
- **Realistic Weather Generation**: Wind, visibility, clouds, precipitation, RVR
- **ICAO-Compliant Format**: Proper phraseology and structure
- **Directus Integration**: Stores generated ATIS entries in your Directus CMS

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.py` with your Directus credentials:

```python
DIRECTUS_URL = "https://your-directus-instance.com"
DIRECTUS_EMAIL = "your@email.com"
DIRECTUS_PASSWORD = "your_password"
NUM_ATIS_TO_GENERATE = 500
```

## Usage

### Generate ATIS Entries

```bash
python main.py
```

This will:
1. Set up the Directus schema (airport & atis_entries collections)
2. Populate airports with DACH region data
3. Generate the specified number of ATIS entries

### Test the Generator

```bash
python generator.py
```

Outputs sample ATIS messages for each difficulty level.

## Difficulty Levels

| Level | Visibility | Wind | Weather | Remarks |
|-------|------------|------|---------|---------|
| Super Easy | 10km+ (CAVOK) | <8kt, no gusts | None | None |
| Easy | 5km+ | <15kt | Light only | Rare, simple |
| Medium | 1.5km+ | <28kt, gusts | Moderate | Common |
| Hard | 100m+ | <45kt, gusty | Complex | Multiple |

## Sample Output

**Super Easy:**
> Frankfurt Main information Alpha. Recorded at 1200 Zulu. Runway in use 25R. Expect ILS approach. Transition level 70. Wind 260 degrees, 5 knots. Visibility 10 kilometers or more. CAVOK. Temperature 15, dewpoint 10. QNH 1013 hectopascals. Advise on initial contact you have information Alpha.

**Hard:**
> Hamburg information Mike. Recorded at 0845 Zulu. Runway in use 33, 05. Expect ILS CAT III approach. Transition level 90. Wind 340 degrees, 37 knots, gusting 52 knots. Visibility 400 meters. RVR runway 33 350 meters improving. Present weather: freezing rain, fog. Broken at 100 feet, overcast at 300 feet. Temperature minus 2, dewpoint minus 3. QNH 989 hectopascals. LOW LEVEL WIND SHEAR ON FINAL. BRAKING ACTION POOR. Advise on initial contact you have information Mike.

## Project Structure

```
atis_generator/
├── config.py           # Directus credentials & settings
├── data.py             # Airport data, difficulty settings, weather codes
├── directus_client.py  # Directus API client
├── generator.py        # ATIS generation logic
├── main.py             # Main orchestration script
├── requirements.txt    # Python dependencies
└── README.md
```

## Airports Included

Major airports from Germany (ED**), Austria (LO**), and Switzerland (LS**):
- EDDF (Frankfurt), EDDM (München), EDDL (Düsseldorf), EDDB (Berlin)
- LOWW (Wien), LOWS (Salzburg), LOWI (Innsbruck)
- LSZH (Zürich), LSGG (Genève), LSZB (Bern)
- And 27 more regional airports...

## License

MIT License

## Contributing

Pull requests welcome! Ideas for improvement:
- Audio generation (TTS)
- More airports/regions
- METAR/TAF parsing
- Web interface for practice
