# DACH Region Airports Data
# Contains major airports from Germany (ED), Austria (LO), and Switzerland (LS)

DACH_AIRPORTS = [
    # Germany - Major International
    {
        "icao": "EDDF",
        "name": "Frankfurt Main",
        "city": "Frankfurt",
        "country": "DE",
        "elevation_ft": 364,
        "transition_altitude": 5000,
        "default_freq": "118.025",
        "runways": [
            {"designator": "07L", "heading": 70, "length_m": 4000, "ils": True},
            {"designator": "25R", "heading": 250, "length_m": 4000, "ils": True},
            {"designator": "07C", "heading": 70, "length_m": 4000, "ils": True},
            {"designator": "25C", "heading": 250, "length_m": 4000, "ils": True},
            {"designator": "07R", "heading": 70, "length_m": 4000, "ils": True},
            {"designator": "25L", "heading": 250, "length_m": 4000, "ils": True},
            {"designator": "18", "heading": 180, "length_m": 4000, "ils": True}
        ]
    },
    {
        "icao": "EDDM",
        "name": "München Franz Josef Strauß",
        "city": "München",
        "country": "DE",
        "elevation_ft": 1487,
        "transition_altitude": 5000,
        "default_freq": "123.125",
        "runways": [
            {"designator": "08L", "heading": 80, "length_m": 4000, "ils": True},
            {"designator": "26R", "heading": 260, "length_m": 4000, "ils": True},
            {"designator": "08R", "heading": 80, "length_m": 4000, "ils": True},
            {"designator": "26L", "heading": 260, "length_m": 4000, "ils": True}
        ]
    },
    {
        "icao": "EDDL",
        "name": "Düsseldorf",
        "city": "Düsseldorf",
        "country": "DE",
        "elevation_ft": 147,
        "transition_altitude": 5000,
        "default_freq": "126.300",
        "runways": [
            {"designator": "05L", "heading": 50, "length_m": 3000, "ils": True},
            {"designator": "23R", "heading": 230, "length_m": 3000, "ils": True},
            {"designator": "05R", "heading": 50, "length_m": 2700, "ils": True},
            {"designator": "23L", "heading": 230, "length_m": 2700, "ils": True}
        ]
    },
    {
        "icao": "EDDB",
        "name": "Berlin Brandenburg",
        "city": "Berlin",
        "country": "DE",
        "elevation_ft": 157,
        "transition_altitude": 5000,
        "default_freq": "127.775",
        "runways": [
            {"designator": "07L", "heading": 70, "length_m": 3600, "ils": True},
            {"designator": "25R", "heading": 250, "length_m": 3600, "ils": True},
            {"designator": "07R", "heading": 70, "length_m": 4000, "ils": True},
            {"designator": "25L", "heading": 250, "length_m": 4000, "ils": True}
        ]
    },
    {
        "icao": "EDDH",
        "name": "Hamburg Helmut Schmidt",
        "city": "Hamburg",
        "country": "DE",
        "elevation_ft": 53,
        "transition_altitude": 5000,
        "default_freq": "127.125",
        "runways": [
            {"designator": "05", "heading": 50, "length_m": 3250, "ils": True},
            {"designator": "23", "heading": 230, "length_m": 3250, "ils": True},
            {"designator": "15", "heading": 150, "length_m": 3666, "ils": True},
            {"designator": "33", "heading": 330, "length_m": 3666, "ils": True}
        ]
    },
    {
        "icao": "EDDK",
        "name": "Köln Bonn",
        "city": "Köln",
        "country": "DE",
        "elevation_ft": 302,
        "transition_altitude": 5000,
        "default_freq": "125.625",
        "runways": [
            {"designator": "06", "heading": 60, "length_m": 1863, "ils": False},
            {"designator": "24", "heading": 240, "length_m": 1863, "ils": False},
            {"designator": "14L", "heading": 140, "length_m": 3815, "ils": True},
            {"designator": "32R", "heading": 320, "length_m": 3815, "ils": True},
            {"designator": "14R", "heading": 140, "length_m": 2459, "ils": True},
            {"designator": "32L", "heading": 320, "length_m": 2459, "ils": False}
        ]
    },
    {
        "icao": "EDDS",
        "name": "Stuttgart",
        "city": "Stuttgart",
        "country": "DE",
        "elevation_ft": 1276,
        "transition_altitude": 5000,
        "default_freq": "126.125",
        "runways": [
            {"designator": "07", "heading": 70, "length_m": 3345, "ils": True},
            {"designator": "25", "heading": 250, "length_m": 3345, "ils": True}
        ]
    },
    {
        "icao": "EDDP",
        "name": "Leipzig Halle",
        "city": "Leipzig",
        "country": "DE",
        "elevation_ft": 465,
        "transition_altitude": 5000,
        "default_freq": "126.100",
        "runways": [
            {"designator": "08L", "heading": 80, "length_m": 3600, "ils": True},
            {"designator": "26R", "heading": 260, "length_m": 3600, "ils": True},
            {"designator": "08R", "heading": 80, "length_m": 3600, "ils": True},
            {"designator": "26L", "heading": 260, "length_m": 3600, "ils": True}
        ]
    },
    {
        "icao": "EDDN",
        "name": "Nürnberg",
        "city": "Nürnberg",
        "country": "DE",
        "elevation_ft": 1046,
        "transition_altitude": 5000,
        "default_freq": "127.500",
        "runways": [
            {"designator": "10", "heading": 100, "length_m": 2700, "ils": True},
            {"designator": "28", "heading": 280, "length_m": 2700, "ils": True}
        ]
    },
    {
        "icao": "EDDC",
        "name": "Dresden",
        "city": "Dresden",
        "country": "DE",
        "elevation_ft": 755,
        "transition_altitude": 5000,
        "default_freq": "125.100",
        "runways": [
            {"designator": "04", "heading": 40, "length_m": 2850, "ils": True},
            {"designator": "22", "heading": 220, "length_m": 2850, "ils": True}
        ]
    },
    {
        "icao": "EDDW",
        "name": "Bremen",
        "city": "Bremen",
        "country": "DE",
        "elevation_ft": 14,
        "transition_altitude": 5000,
        "default_freq": "126.650",
        "runways": [
            {"designator": "09", "heading": 90, "length_m": 2040, "ils": True},
            {"designator": "27", "heading": 270, "length_m": 2040, "ils": True}
        ]
    },
    {
        "icao": "EDDV",
        "name": "Hannover",
        "city": "Hannover",
        "country": "DE",
        "elevation_ft": 183,
        "transition_altitude": 5000,
        "default_freq": "123.075",
        "runways": [
            {"designator": "09L", "heading": 90, "length_m": 2340, "ils": True},
            {"designator": "27R", "heading": 270, "length_m": 2340, "ils": True},
            {"designator": "09R", "heading": 90, "length_m": 3800, "ils": True},
            {"designator": "27L", "heading": 270, "length_m": 3800, "ils": True}
        ]
    },
    {
        "icao": "EDDT",
        "name": "Berlin Tegel",  # Historical reference
        "city": "Berlin",
        "country": "DE",
        "elevation_ft": 122,
        "transition_altitude": 5000,
        "default_freq": "121.750",
        "runways": [
            {"designator": "08L", "heading": 80, "length_m": 3023, "ils": True},
            {"designator": "26R", "heading": 260, "length_m": 3023, "ils": True}
        ]
    },
    {
        "icao": "EDLW",
        "name": "Dortmund",
        "city": "Dortmund",
        "country": "DE",
        "elevation_ft": 425,
        "transition_altitude": 5000,
        "default_freq": "121.300",
        "runways": [
            {"designator": "06", "heading": 60, "length_m": 2000, "ils": True},
            {"designator": "24", "heading": 240, "length_m": 2000, "ils": True}
        ]
    },
    {
        "icao": "EDLP",
        "name": "Paderborn Lippstadt",
        "city": "Paderborn",
        "country": "DE",
        "elevation_ft": 699,
        "transition_altitude": 5000,
        "default_freq": "119.150",
        "runways": [
            {"designator": "06", "heading": 60, "length_m": 2180, "ils": True},
            {"designator": "24", "heading": 240, "length_m": 2180, "ils": True}
        ]
    },
    {
        "icao": "EDDR",
        "name": "Saarbrücken",
        "city": "Saarbrücken",
        "country": "DE",
        "elevation_ft": 1058,
        "transition_altitude": 5000,
        "default_freq": "119.100",
        "runways": [
            {"designator": "09", "heading": 90, "length_m": 2000, "ils": True},
            {"designator": "27", "heading": 270, "length_m": 2000, "ils": True}
        ]
    },
    {
        "icao": "EDFH",
        "name": "Frankfurt Hahn",
        "city": "Hahn",
        "country": "DE",
        "elevation_ft": 1649,
        "transition_altitude": 5000,
        "default_freq": "118.050",
        "runways": [
            {"designator": "03", "heading": 30, "length_m": 3800, "ils": True},
            {"designator": "21", "heading": 210, "length_m": 3800, "ils": True}
        ]
    },
    {
        "icao": "EDNY",
        "name": "Friedrichshafen",
        "city": "Friedrichshafen",
        "country": "DE",
        "elevation_ft": 1367,
        "transition_altitude": 5000,
        "default_freq": "119.350",
        "runways": [
            {"designator": "06", "heading": 60, "length_m": 2356, "ils": True},
            {"designator": "24", "heading": 240, "length_m": 2356, "ils": True}
        ]
    },
    {
        "icao": "EDJA",
        "name": "Memmingen",
        "city": "Memmingen",
        "country": "DE",
        "elevation_ft": 2077,
        "transition_altitude": 5000,
        "default_freq": "119.550",
        "runways": [
            {"designator": "06", "heading": 60, "length_m": 3000, "ils": True},
            {"designator": "24", "heading": 240, "length_m": 3000, "ils": True}
        ]
    },
    
    # Austria
    {
        "icao": "LOWW",
        "name": "Wien Schwechat",
        "city": "Wien",
        "country": "AT",
        "elevation_ft": 600,
        "transition_altitude": 5000,
        "default_freq": "128.125",
        "runways": [
            {"designator": "11", "heading": 110, "length_m": 3500, "ils": True},
            {"designator": "29", "heading": 290, "length_m": 3500, "ils": True},
            {"designator": "16", "heading": 160, "length_m": 3600, "ils": True},
            {"designator": "34", "heading": 340, "length_m": 3600, "ils": True}
        ]
    },
    {
        "icao": "LOWS",
        "name": "Salzburg W.A. Mozart",
        "city": "Salzburg",
        "country": "AT",
        "elevation_ft": 1411,
        "transition_altitude": 5000,
        "default_freq": "118.100",
        "runways": [
            {"designator": "15", "heading": 150, "length_m": 2750, "ils": True},
            {"designator": "33", "heading": 330, "length_m": 2750, "ils": True}
        ]
    },
    {
        "icao": "LOWG",
        "name": "Graz",
        "city": "Graz",
        "country": "AT",
        "elevation_ft": 1115,
        "transition_altitude": 5000,
        "default_freq": "126.700",
        "runways": [
            {"designator": "16C", "heading": 160, "length_m": 3000, "ils": True},
            {"designator": "34C", "heading": 340, "length_m": 3000, "ils": True}
        ]
    },
    {
        "icao": "LOWI",
        "name": "Innsbruck Kranebitten",
        "city": "Innsbruck",
        "country": "AT",
        "elevation_ft": 1907,
        "transition_altitude": 5000,
        "default_freq": "119.100",
        "runways": [
            {"designator": "08", "heading": 80, "length_m": 2000, "ils": True},
            {"designator": "26", "heading": 260, "length_m": 2000, "ils": True}
        ]
    },
    {
        "icao": "LOWK",
        "name": "Klagenfurt",
        "city": "Klagenfurt",
        "country": "AT",
        "elevation_ft": 1470,
        "transition_altitude": 5000,
        "default_freq": "118.250",
        "runways": [
            {"designator": "10L", "heading": 100, "length_m": 2700, "ils": True},
            {"designator": "28R", "heading": 280, "length_m": 2700, "ils": True}
        ]
    },
    {
        "icao": "LOWL",
        "name": "Linz Hörsching",
        "city": "Linz",
        "country": "AT",
        "elevation_ft": 978,
        "transition_altitude": 5000,
        "default_freq": "120.100",
        "runways": [
            {"designator": "08", "heading": 80, "length_m": 3000, "ils": True},
            {"designator": "26", "heading": 260, "length_m": 3000, "ils": True}
        ]
    },
    
    # Switzerland
    {
        "icao": "LSZH",
        "name": "Zürich Kloten",
        "city": "Zürich",
        "country": "CH",
        "elevation_ft": 1416,
        "transition_altitude": 5000,
        "default_freq": "128.525",
        "runways": [
            {"designator": "10", "heading": 100, "length_m": 2500, "ils": True},
            {"designator": "28", "heading": 280, "length_m": 2500, "ils": True},
            {"designator": "14", "heading": 140, "length_m": 3700, "ils": True},
            {"designator": "32", "heading": 320, "length_m": 3700, "ils": True},
            {"designator": "16", "heading": 160, "length_m": 3300, "ils": True},
            {"designator": "34", "heading": 340, "length_m": 3300, "ils": True}
        ]
    },
    {
        "icao": "LSGG",
        "name": "Genève Cointrin",
        "city": "Genève",
        "country": "CH",
        "elevation_ft": 1411,
        "transition_altitude": 5000,
        "default_freq": "128.025",
        "runways": [
            {"designator": "04", "heading": 40, "length_m": 3900, "ils": True},
            {"designator": "22", "heading": 220, "length_m": 3900, "ils": True}
        ]
    },
    {
        "icao": "LSZA",
        "name": "Lugano Agno",
        "city": "Lugano",
        "country": "CH",
        "elevation_ft": 915,
        "transition_altitude": 5000,
        "default_freq": "118.850",
        "runways": [
            {"designator": "01", "heading": 10, "length_m": 1350, "ils": False},
            {"designator": "19", "heading": 190, "length_m": 1350, "ils": False}
        ]
    },
    {
        "icao": "LSZB",
        "name": "Bern Belp",
        "city": "Bern",
        "country": "CH",
        "elevation_ft": 1674,
        "transition_altitude": 5000,
        "default_freq": "120.850",
        "runways": [
            {"designator": "14", "heading": 140, "length_m": 1730, "ils": True},
            {"designator": "32", "heading": 320, "length_m": 1730, "ils": True}
        ]
    },
    {
        "icao": "LSZR",
        "name": "St. Gallen Altenrhein",
        "city": "St. Gallen",
        "country": "CH",
        "elevation_ft": 1306,
        "transition_altitude": 5000,
        "default_freq": "119.375",
        "runways": [
            {"designator": "10", "heading": 100, "length_m": 1500, "ils": False},
            {"designator": "28", "heading": 280, "length_m": 1500, "ils": True}
        ]
    },
    {
        "icao": "LSME",
        "name": "Emmen",
        "city": "Emmen",
        "country": "CH",
        "elevation_ft": 1400,
        "transition_altitude": 5000,
        "default_freq": "124.250",
        "runways": [
            {"designator": "04", "heading": 40, "length_m": 2500, "ils": True},
            {"designator": "22", "heading": 220, "length_m": 2500, "ils": True}
        ]
    },
    {
        "icao": "LSMP",
        "name": "Payerne",
        "city": "Payerne",
        "country": "CH",
        "elevation_ft": 1465,
        "transition_altitude": 5000,
        "default_freq": "131.150",
        "runways": [
            {"designator": "05", "heading": 50, "length_m": 2940, "ils": True},
            {"designator": "23", "heading": 230, "length_m": 2940, "ils": True}
        ]
    },
    {
        "icao": "LSGS",
        "name": "Sion",
        "city": "Sion",
        "country": "CH",
        "elevation_ft": 1582,
        "transition_altitude": 5000,
        "default_freq": "118.275",
        "runways": [
            {"designator": "07", "heading": 70, "length_m": 2000, "ils": True},
            {"designator": "25", "heading": 250, "length_m": 2000, "ils": True}
        ]
    },
    
    # Additional Germany regional
    {
        "icao": "EDDE",
        "name": "Erfurt Weimar",
        "city": "Erfurt",
        "country": "DE",
        "elevation_ft": 1036,
        "transition_altitude": 5000,
        "default_freq": "119.050",
        "runways": [
            {"designator": "10", "heading": 100, "length_m": 2620, "ils": True},
            {"designator": "28", "heading": 280, "length_m": 2620, "ils": True}
        ]
    },
    {
        "icao": "EDDG",
        "name": "Münster Osnabrück",
        "city": "Münster",
        "country": "DE",
        "elevation_ft": 160,
        "transition_altitude": 5000,
        "default_freq": "118.675",
        "runways": [
            {"designator": "07", "heading": 70, "length_m": 2170, "ils": True},
            {"designator": "25", "heading": 250, "length_m": 2170, "ils": True}
        ]
    },
    {
        "icao": "EDLV",
        "name": "Niederrhein Weeze",
        "city": "Weeze",
        "country": "DE",
        "elevation_ft": 106,
        "transition_altitude": 5000,
        "default_freq": "118.750",
        "runways": [
            {"designator": "09", "heading": 90, "length_m": 2440, "ils": True},
            {"designator": "27", "heading": 270, "length_m": 2440, "ils": True}
        ]
    },
    {
        "icao": "EDDF",
        "name": "Frankfurt Main",
        "city": "Frankfurt",
        "country": "DE",
        "elevation_ft": 364,
        "transition_altitude": 5000,
        "default_freq": "118.025",
        "runways": [
            {"designator": "07L", "heading": 70, "length_m": 4000, "ils": True},
            {"designator": "25R", "heading": 250, "length_m": 4000, "ils": True},
            {"designator": "07C", "heading": 70, "length_m": 4000, "ils": True},
            {"designator": "25C", "heading": 250, "length_m": 4000, "ils": True},
            {"designator": "18", "heading": 180, "length_m": 4000, "ils": True}
        ]
    },
    {
        "icao": "EDDZ",
        "name": "Rostock Laage",
        "city": "Rostock",
        "country": "DE",
        "elevation_ft": 138,
        "transition_altitude": 5000,
        "default_freq": "120.925",
        "runways": [
            {"designator": "10", "heading": 100, "length_m": 2520, "ils": True},
            {"designator": "28", "heading": 280, "length_m": 2520, "ils": True}
        ]
    },
]

# NATO Phonetic Alphabet for information letters
NATO_ALPHABET = [
    "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",
    "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November",
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform",
    "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"
]

# Weather phenomena codes (ICAO format)
WEATHER_PHENOMENA = {
    "intensity": ["-", "", "+"],  # light, moderate, heavy
    "descriptor": ["MI", "BC", "PR", "DR", "BL", "SH", "TS", "FZ"],
    "precipitation": ["DZ", "RA", "SN", "SG", "IC", "PL", "GR", "GS"],
    "obscuration": ["BR", "FG", "FU", "VA", "DU", "SA", "HZ"],
    "other": ["PO", "SQ", "FC", "SS", "DS"]
}

# Cloud types
CLOUD_TYPES = ["FEW", "SCT", "BKN", "OVC"]

# Standard cloud heights (in feet)
CLOUD_HEIGHTS = [500, 700, 800, 1000, 1200, 1500, 1800, 2000, 2500, 3000, 
                 3500, 4000, 4500, 5000, 6000, 7000, 8000, 10000, 12000, 15000, 20000]

# Approach types
APPROACH_TYPES = ["ILS", "ILS CAT II", "ILS CAT III", "VOR", "RNAV", "RNAV (GPS)", "NDB", "Visual"]

# Visibility values in meters (common ICAO values)
VISIBILITY_VALUES = [
    100, 150, 200, 300, 400, 500, 600, 700, 800, 900,  # Very low
    1000, 1200, 1500, 1800, 2000, 2500, 3000, 3500, 4000, 4500, 5000,  # Low to moderate
    6000, 7000, 8000, 9000, 9999  # Good (9999 = 10km or more)
]

# RVR values in meters
RVR_VALUES = [50, 75, 100, 125, 150, 175, 200, 250, 300, 350, 400, 450, 
              500, 550, 600, 700, 800, 900, 1000, 1200, 1500, 1800, 2000]

# Difficulty settings for weather generation
# Four tiers for progressive learning experience
DIFFICULTY_SETTINGS = {
    "super_easy": {
        # Perfect conditions - beginners learning the ATIS format
        "min_visibility": 9999,
        "max_visibility": 9999,
        "max_cloud_layers": 1,
        "min_ceiling": 5000,
        "max_wind_speed": 8,
        "min_wind_speed": 0,
        "gust_probability": 0.0,
        "weather_probability": 0.0,
        "variable_wind_probability": 0.0,
        "cavok_probability": 0.7,  # High chance of CAVOK
        "calm_wind_probability": 0.3,
        "rvr_probability": 0.0,
        "remarks_probability": 0.0,
        "use_round_numbers": True,  # QNH like 1013, 1020; wind in 5kt increments
        "single_runway_only": True,
        "simple_approach_only": True,  # Only ILS or Visual
        "max_remarks": 0,
        "qnh_range": (1010, 1025),  # Nice stable pressure
        "temp_range": (10, 25),  # Comfortable temperatures
        "description": "Perfect weather, simple format - for learning ATIS structure"
    },
    "easy": {
        # Good conditions with minor variations
        "min_visibility": 5000,
        "max_visibility": 9999,
        "max_cloud_layers": 2,
        "min_ceiling": 3000,
        "max_wind_speed": 15,
        "min_wind_speed": 3,
        "gust_probability": 0.05,
        "weather_probability": 0.15,  # Light weather only
        "variable_wind_probability": 0.1,
        "cavok_probability": 0.3,
        "calm_wind_probability": 0.1,
        "rvr_probability": 0.0,
        "remarks_probability": 0.15,
        "use_round_numbers": True,
        "single_runway_only": True,
        "simple_approach_only": True,
        "max_remarks": 1,
        "allowed_weather": ["-RA", "-DZ", "BR"],  # Only light precip or mist
        "qnh_range": (1005, 1030),
        "temp_range": (5, 28),
        "description": "Good weather with minor variations - building confidence"
    },
    "medium": {
        # Realistic operational conditions
        "min_visibility": 1500,
        "max_visibility": 9999,
        "max_cloud_layers": 3,
        "min_ceiling": 800,
        "max_wind_speed": 28,
        "min_wind_speed": 5,
        "gust_probability": 0.25,
        "weather_probability": 0.4,
        "variable_wind_probability": 0.25,
        "cavok_probability": 0.15,
        "calm_wind_probability": 0.05,
        "rvr_probability": 0.2,
        "remarks_probability": 0.35,
        "use_round_numbers": False,
        "single_runway_only": False,
        "simple_approach_only": False,
        "max_remarks": 2,
        "allowed_weather": ["-RA", "RA", "-SN", "SN", "-DZ", "DZ", "BR", "HZ", "-SHRA", "SHRA"],
        "qnh_range": (995, 1035),
        "temp_range": (-5, 32),
        "description": "Realistic conditions - developing proficiency"
    },
    "hard": {
        # Challenging operational conditions
        "min_visibility": 100,
        "max_visibility": 5000,
        "max_cloud_layers": 4,
        "min_ceiling": 100,
        "max_wind_speed": 45,
        "min_wind_speed": 8,
        "gust_probability": 0.5,
        "weather_probability": 0.75,
        "variable_wind_probability": 0.35,
        "cavok_probability": 0.0,
        "calm_wind_probability": 0.0,
        "rvr_probability": 0.6,
        "remarks_probability": 0.7,
        "use_round_numbers": False,
        "single_runway_only": False,
        "simple_approach_only": False,
        "max_remarks": 3,
        "allowed_weather": None,  # All weather types allowed
        "qnh_range": (975, 1045),
        "temp_range": (-15, 38),
        "cb_probability": 0.15,  # Cumulonimbus clouds
        "windshear_probability": 0.2,
        "description": "Challenging weather - professional readiness"
    }
}

# Remarks categorized by complexity
REMARKS_BY_DIFFICULTY = {
    "easy": [
        "RUNWAY SURFACE DRY",
        "BRAKING ACTION GOOD",
        "NOISE ABATEMENT IN EFFECT"
    ],
    "medium": [
        "BIRD ACTIVITY REPORTED",
        "RUNWAY SURFACE WET",
        "BRAKING ACTION MEDIUM",
        "TAXIWAY ALPHA CLOSED",
        "GLIDER ACTIVITY IN THE VICINITY",
        "CONSTRUCTION WORK SOUTH OF RUNWAY",
        "EXPECT MINOR DELAYS"
    ],
    "hard": [
        "LOW LEVEL WIND SHEAR REPORTED ON FINAL",
        "BRAKING ACTION POOR",
        "PRECISION APPROACH PATH INDICATOR UNSERVICEABLE",
        "ILS GLIDEPATH UNSERVICEABLE USE LOC ONLY APPROACH",
        "RUNWAY EDGE LIGHTS UNSERVICEABLE",
        "EXPECT HOLDING DUE TRAFFIC",
        "SNOW REMOVAL IN PROGRESS RUNWAY 25",
        "REDUCED RUNWAY LENGTH AVAILABLE 2500 METERS",
        "WAKE TURBULENCE CAUTION HEAVY DEPARTURE PRECEDING",
        "TEMPORARY OBSTACLE CRANE 85 METERS AGL SOUTH OF FIELD",
        "GPS RAIM NOT AVAILABLE",
        "MULTIPLE BIRD STRIKES REPORTED",
        "RUNWAY CONTAMINATION 25 PERCENT COVERAGE WET SNOW",
        "MILITARY EXERCISE ACTIVE NORTH OF FIELD"
    ]
}

# Approach types by difficulty
APPROACH_TYPES_BY_DIFFICULTY = {
    "super_easy": ["ILS", "Visual"],
    "easy": ["ILS", "Visual", "RNAV"],
    "medium": ["ILS", "ILS CAT II", "RNAV", "RNAV (GPS)", "VOR", "Visual"],
    "hard": ["ILS", "ILS CAT II", "ILS CAT III", "RNAV", "RNAV (GPS)", "VOR", "NDB", "LOC only", "Circling"]
}
