"""
ATIS Generator - Creates realistic ATIS entries for practice
"""
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from data import (
    DACH_AIRPORTS, NATO_ALPHABET, WEATHER_PHENOMENA, CLOUD_TYPES,
    CLOUD_HEIGHTS, APPROACH_TYPES, VISIBILITY_VALUES, RVR_VALUES,
    DIFFICULTY_SETTINGS, REMARKS_BY_DIFFICULTY, APPROACH_TYPES_BY_DIFFICULTY
)


class ATISGenerator:
    """Generates realistic ATIS entries for aviation practice."""
    
    def __init__(self):
        self.airports = DACH_AIRPORTS
    
    def _round_to_nearest(self, value: int, nearest: int) -> int:
        """Round value to nearest increment (for super_easy/easy modes)."""
        return round(value / nearest) * nearest
    
    def generate_wind(self, difficulty: str) -> Dict:
        """Generate realistic wind data based on difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        
        # Calm wind
        if random.random() < settings.get("calm_wind_probability", 0.05):
            return {
                "direction": 0,
                "speed": 0,
                "gust": None,
                "variable_from": None,
                "variable_to": None,
                "is_calm": True
            }
        
        # Generate direction
        direction = random.randint(1, 36) * 10  # 010 to 360 in 10° increments
        
        # Generate speed
        min_speed = settings.get("min_wind_speed", 3)
        max_speed = settings.get("max_wind_speed", 15)
        speed = random.randint(min_speed, max_speed)
        
        # Round numbers for easier difficulties
        if settings.get("use_round_numbers", False):
            speed = self._round_to_nearest(speed, 5)
            if speed < min_speed:
                speed = 5
        
        # Gusts
        gust = None
        if random.random() < settings.get("gust_probability", 0.1) and speed >= 10:
            gust_addition = random.randint(8, 20)
            gust = speed + gust_addition
            if settings.get("use_round_numbers", False):
                gust = self._round_to_nearest(gust, 5)
        
        # Variable wind (only for light winds)
        variable_from = None
        variable_to = None
        if random.random() < settings.get("variable_wind_probability", 0.2) and speed <= 6:
            var_range = random.randint(30, 60)
            variable_from = (direction - var_range) % 360
            variable_to = (direction + var_range) % 360
            if variable_from == 0:
                variable_from = 360
            if variable_to == 0:
                variable_to = 360
            # Round to 10 degrees
            variable_from = self._round_to_nearest(variable_from, 10)
            variable_to = self._round_to_nearest(variable_to, 10)
        
        return {
            "direction": direction,
            "speed": speed,
            "gust": gust,
            "variable_from": variable_from,
            "variable_to": variable_to,
            "is_calm": False
        }
    
    def generate_visibility(self, difficulty: str) -> int:
        """Generate visibility based on difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        
        min_vis = settings["min_visibility"]
        max_vis = settings["max_visibility"]
        
        valid_values = [v for v in VISIBILITY_VALUES if min_vis <= v <= max_vis]
        
        # For super_easy, always return 9999 (10km+)
        if difficulty == "super_easy":
            return 9999
        
        visibility = random.choice(valid_values)
        
        # Round for easier difficulties
        if settings.get("use_round_numbers", False) and visibility < 9999:
            if visibility >= 5000:
                visibility = self._round_to_nearest(visibility, 1000)
            else:
                visibility = self._round_to_nearest(visibility, 500)
        
        return visibility
    
    def generate_rvr(self, visibility: int, runways: List[Dict], difficulty: str) -> Optional[List[Dict]]:
        """Generate RVR data if visibility is low."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        
        # No RVR for easy difficulties or good visibility
        if visibility > 1500 or not runways:
            return None
        
        if random.random() > settings.get("rvr_probability", 0.2):
            return None
        
        rvr_data = []
        num_runways = min(len(runways), random.randint(1, 2 if difficulty == "medium" else 3))
        selected_runways = random.sample(runways, num_runways)
        
        for runway in selected_runways:
            # RVR is typically better than or similar to visibility
            rvr_value = random.choice([v for v in RVR_VALUES if v <= visibility + 300 and v >= visibility - 200])
            trend = random.choice(["U", "D", "N", ""])  # Up, Down, No change, not reported
            rvr_data.append({
                "runway": runway["designator"],
                "value": rvr_value,
                "trend": trend
            })
        
        return rvr_data
    
    def generate_weather(self, difficulty: str) -> Optional[List[str]]:
        """Generate weather phenomena based on difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        
        if random.random() > settings.get("weather_probability", 0.2):
            return None
        
        allowed_weather = settings.get("allowed_weather", None)
        
        phenomena = []
        num_phenomena = 1
        if difficulty == "hard":
            num_phenomena = random.randint(1, 2)
        
        for _ in range(num_phenomena):
            if allowed_weather:
                # Use only allowed weather for this difficulty
                phenomena.append(random.choice(allowed_weather))
            else:
                # Full weather generation for hard mode
                weather_type = random.choice(["precipitation", "obscuration"])
                
                if weather_type == "precipitation":
                    intensity = random.choice(WEATHER_PHENOMENA["intensity"])
                    precip = random.choice(WEATHER_PHENOMENA["precipitation"])
                    
                    # Add descriptor sometimes
                    if random.random() < 0.3:
                        descriptor = random.choice(["SH", "TS", "FZ"])
                        phenomena.append(f"{intensity}{descriptor}{precip}")
                    else:
                        phenomena.append(f"{intensity}{precip}")
                else:
                    phenomena.append(random.choice(WEATHER_PHENOMENA["obscuration"]))
        
        return phenomena if phenomena else None
    
    def generate_clouds(self, difficulty: str, visibility: int) -> Tuple[List[Dict], bool]:
        """Generate cloud layers or CAVOK based on difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        
        # CAVOK conditions - higher probability for easier difficulties
        cavok_prob = settings.get("cavok_probability", 0.1)
        if visibility >= 9999 and random.random() < cavok_prob:
            return [], True  # CAVOK
        
        # For super_easy without CAVOK, just high scattered clouds
        if difficulty == "super_easy":
            return [{"type": "FEW", "height_ft": random.choice([8000, 10000, 12000]), "cb": False}], False
        
        # Generate cloud layers
        num_layers = random.randint(1, settings.get("max_cloud_layers", 3))
        layers = []
        
        min_height = settings.get("min_ceiling", 1000)
        available_heights = [h for h in CLOUD_HEIGHTS if h >= min_height]
        
        used_heights = []
        for i in range(num_layers):
            valid_heights = [h for h in available_heights if h not in used_heights]
            if i > 0:
                valid_heights = [h for h in valid_heights if h > max(used_heights)]
            
            if not valid_heights:
                break
            
            height = random.choice(valid_heights)
            used_heights.append(height)
            
            # Cloud type based on layer position and difficulty
            if i == 0 and difficulty == "hard" and min_height < 500:
                cloud_type = random.choice(["BKN", "OVC"])  # Low ceiling for hard
            elif i == 0 and difficulty == "medium":
                cloud_type = random.choice(["SCT", "BKN", "OVC", "FEW"])
            else:
                cloud_type = random.choice(CLOUD_TYPES)
            
            # CB clouds only in hard mode
            cb = False
            if difficulty == "hard" and random.random() < settings.get("cb_probability", 0.1):
                cb = True
            
            layers.append({
                "type": cloud_type,
                "height_ft": height,
                "cb": cb
            })
        
        layers.sort(key=lambda x: x["height_ft"])
        
        return layers, False
    
    def generate_temperature(self, difficulty: str) -> Tuple[int, int]:
        """Generate realistic temperature and dewpoint based on difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        temp_range = settings.get("temp_range", (-5, 30))
        
        temperature = random.randint(temp_range[0], temp_range[1])
        
        # Round for easier difficulties
        if settings.get("use_round_numbers", False):
            temperature = self._round_to_nearest(temperature, 5)
        
        # Dewpoint spread
        if difficulty in ["super_easy", "easy"]:
            spread = random.randint(3, 8)  # Comfortable spread
        else:
            spread = random.randint(1, 15)  # Can be close (fog) or far
        
        dewpoint = temperature - spread
        
        if settings.get("use_round_numbers", False):
            dewpoint = self._round_to_nearest(dewpoint, 5)
        
        return temperature, dewpoint
    
    def generate_qnh(self, difficulty: str) -> int:
        """Generate realistic QNH value based on difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        qnh_range = settings.get("qnh_range", (1000, 1030))
        
        qnh = random.randint(qnh_range[0], qnh_range[1])
        
        # Round for easier difficulties
        if settings.get("use_round_numbers", False):
            # Use common round values
            round_values = [1010, 1013, 1015, 1020, 1025]
            qnh = min(round_values, key=lambda x: abs(x - qnh))
        
        return qnh
    
    def calculate_transition_level(self, qnh: int) -> int:
        """Calculate transition level based on QNH."""
        # Standard ICAO calculation for DACH region (TA = 5000ft)
        if qnh >= 1031:
            return 60
        elif qnh >= 1014:
            return 70
        elif qnh >= 996:
            return 80
        else:
            return 90
    
    def select_runways(self, airport: Dict, wind: Dict, difficulty: str) -> Dict:
        """Select active runways based on wind direction and difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        runways = airport.get("runways", [])
        
        if not runways:
            return {"arrival": ["09"], "departure": ["09"]}  # Fallback
        
        wind_dir = wind["direction"] if wind["direction"] > 0 else 0
        
        # Find runway(s) most aligned with wind
        best_runways = []
        for runway in runways:
            heading = runway["heading"]
            diff = abs(wind_dir - heading)
            if diff > 180:
                diff = 360 - diff
            best_runways.append((runway, diff))
        
        best_runways.sort(key=lambda x: x[1])
        
        # For easy difficulties, use single runway
        if settings.get("single_runway_only", True):
            active = [best_runways[0][0]["designator"]]
        else:
            num_active = 1 if len(runways) < 4 else random.randint(1, 2)
            active = [r[0]["designator"] for r in best_runways[:num_active]]
        
        return {
            "arrival": active,
            "departure": active
        }
    
    def select_approach_type(self, runway: Dict, visibility: int, clouds: List[Dict], 
                             difficulty: str) -> str:
        """Select appropriate approach type based on conditions and difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        has_ils = runway.get("ils", True)
        
        # Get available approaches for this difficulty
        available_approaches = APPROACH_TYPES_BY_DIFFICULTY.get(difficulty, APPROACH_TYPES)
        
        # Simple approach for easy difficulties
        if settings.get("simple_approach_only", False):
            return random.choice(["ILS", "Visual"] if has_ils else ["Visual", "RNAV"])
        
        # Get ceiling
        ceiling = None
        for cloud in clouds:
            if cloud["type"] in ["BKN", "OVC"]:
                ceiling = cloud["height_ft"]
                break
        
        # CAT III conditions
        if visibility < 300 and has_ils and "ILS CAT III" in available_approaches:
            return "ILS CAT III"
        elif visibility < 550 and has_ils and "ILS CAT II" in available_approaches:
            return "ILS CAT II"
        elif visibility < 800 or (ceiling and ceiling < 300):
            if has_ils:
                return "ILS"
            elif "RNAV" in available_approaches:
                return "RNAV"
        elif visibility >= 5000 and (not ceiling or ceiling > 1500):
            if random.random() < 0.2 and "Visual" in available_approaches:
                return "Visual"
        
        # Default selection from available
        if has_ils:
            ils_options = [a for a in available_approaches if "ILS" in a and "CAT" not in a]
            if ils_options:
                return random.choice(ils_options)
        
        non_visual = [a for a in available_approaches if a != "Visual"]
        return random.choice(non_visual) if non_visual else "ILS"
    
    def generate_remarks(self, difficulty: str, weather: Optional[List[str]]) -> Optional[str]:
        """Generate optional remarks/NOTAMs based on difficulty."""
        settings = DIFFICULTY_SETTINGS[difficulty]
        
        if random.random() > settings.get("remarks_probability", 0.3):
            return None
        
        max_remarks = settings.get("max_remarks", 1)
        if max_remarks == 0:
            return None
        
        # Get remarks appropriate for difficulty
        available_remarks = []
        if difficulty == "easy":
            available_remarks = REMARKS_BY_DIFFICULTY["easy"]
        elif difficulty == "medium":
            available_remarks = REMARKS_BY_DIFFICULTY["easy"] + REMARKS_BY_DIFFICULTY["medium"]
        elif difficulty == "hard":
            available_remarks = (REMARKS_BY_DIFFICULTY["easy"] + 
                                REMARKS_BY_DIFFICULTY["medium"] + 
                                REMARKS_BY_DIFFICULTY["hard"])
        
        if not available_remarks:
            return None
        
        num_remarks = random.randint(1, max_remarks)
        selected = random.sample(available_remarks, min(num_remarks, len(available_remarks)))
        
        # Add wind shear warning in hard mode
        if difficulty == "hard" and random.random() < settings.get("windshear_probability", 0.1):
            selected.append("LOW LEVEL WIND SHEAR ALERT")
        
        return ". ".join(selected)
    
    def format_wind_text(self, wind: Dict) -> str:
        """Format wind for ATIS readout."""
        if wind["is_calm"]:
            return "Wind calm"
        
        text = f"Wind {wind['direction']:03d} degrees, {wind['speed']} knots"
        
        if wind["gust"]:
            text += f", gusting {wind['gust']} knots"
        
        if wind["variable_from"] and wind["variable_to"]:
            text += f", variable between {wind['variable_from']:03d} and {wind['variable_to']:03d} degrees"
        
        return text
    
    def format_visibility_text(self, visibility: int, rvr: Optional[List[Dict]]) -> str:
        """Format visibility for ATIS readout."""
        if visibility >= 9999:
            text = "Visibility 10 kilometers or more"
        elif visibility >= 5000:
            text = f"Visibility {visibility // 1000} kilometers"
        else:
            text = f"Visibility {visibility} meters"
        
        if rvr:
            rvr_texts = []
            for r in rvr:
                rvr_text = f"RVR runway {r['runway']} {r['value']} meters"
                if r["trend"]:
                    trends = {"U": "improving", "D": "decreasing", "N": "no change"}
                    rvr_text += f" {trends.get(r['trend'], '')}"
                rvr_texts.append(rvr_text)
            text += ". " + ", ".join(rvr_texts)
        
        return text
    
    def format_weather_text(self, weather: Optional[List[str]]) -> str:
        """Format weather phenomena for ATIS readout."""
        if not weather:
            return ""
        
        weather_names = {
            "-RA": "light rain",
            "RA": "rain",
            "+RA": "heavy rain",
            "-SN": "light snow",
            "SN": "snow",
            "+SN": "heavy snow",
            "-SHRA": "light rain showers",
            "SHRA": "rain showers",
            "+SHRA": "heavy rain showers",
            "-SHSN": "light snow showers",
            "SHSN": "snow showers",
            "+SHSN": "heavy snow showers",
            "TSRA": "thunderstorm with rain",
            "+TSRA": "heavy thunderstorm with rain",
            "-DZ": "light drizzle",
            "DZ": "drizzle",
            "+DZ": "heavy drizzle",
            "FG": "fog",
            "BR": "mist",
            "HZ": "haze",
            "FU": "smoke",
            "FZRA": "freezing rain",
            "FZDZ": "freezing drizzle",
            "-FZRA": "light freezing rain",
            "+FZRA": "heavy freezing rain",
            "GR": "hail",
            "GS": "small hail",
            "SQ": "squalls"
        }
        
        descriptions = []
        for w in weather:
            if w in weather_names:
                descriptions.append(weather_names[w])
            else:
                descriptions.append(w.lower())
        
        return ", ".join(descriptions)
    
    def format_clouds_text(self, clouds: List[Dict], cavok: bool) -> str:
        """Format clouds for ATIS readout."""
        if cavok:
            return "CAVOK"
        
        if not clouds:
            return "Sky clear"
        
        cloud_names = {
            "FEW": "few",
            "SCT": "scattered",
            "BKN": "broken",
            "OVC": "overcast"
        }
        
        texts = []
        for cloud in clouds:
            height = cloud["height_ft"]
            if height >= 10000:
                height_text = f"{height // 1000} thousand"
            elif height >= 1000:
                thousands = height // 1000
                hundreds = (height % 1000) // 100
                if hundreds > 0:
                    height_text = f"{thousands} thousand {hundreds} hundred"
                else:
                    height_text = f"{thousands} thousand"
            else:
                height_text = f"{height}"
            
            text = f"{cloud_names[cloud['type']]} at {height_text} feet"
            if cloud.get("cb"):
                text += " cumulonimbus"
            texts.append(text)
        
        return ", ".join(texts)
    
    def generate_full_text(self, airport: Dict, data: Dict) -> str:
        """Generate the complete ATIS readout text."""
        lines = []
        
        # Header
        lines.append(f"{airport['name']} information {data['information_letter']}.")
        lines.append(f"Recorded at {data['observation_time'].strftime('%H%M')} Zulu.")
        
        # Runway
        arr_runways = ", ".join(data["active_runways"]["arrival"])
        dep_runways = ", ".join(data["active_runways"]["departure"])
        if arr_runways == dep_runways:
            lines.append(f"Runway in use {arr_runways}.")
        else:
            lines.append(f"Arrival runway {arr_runways}, departure runway {dep_runways}.")
        
        # Approach
        lines.append(f"Expect {data['approach_type']} approach.")
        
        # Transition level
        lines.append(f"Transition level {data['transition_level']}.")
        
        # Wind
        lines.append(f"{self.format_wind_text(data['wind'])}.")
        
        # Visibility
        lines.append(f"{self.format_visibility_text(data['visibility'], data['rvr'])}.")
        
        # Weather (if any)
        weather_text = self.format_weather_text(data.get("weather"))
        if weather_text:
            lines.append(f"Present weather: {weather_text}.")
        
        # Clouds
        lines.append(f"{self.format_clouds_text(data['clouds'], data['cavok'])}.")
        
        # Temperature
        temp = data["temperature"]
        dew = data["dewpoint"]
        temp_sign = "" if temp >= 0 else "minus "
        dew_sign = "" if dew >= 0 else "minus "
        lines.append(f"Temperature {temp_sign}{abs(temp)}, dewpoint {dew_sign}{abs(dew)}.")
        
        # QNH
        lines.append(f"QNH {data['qnh']} hectopascals.")
        
        # Remarks (if any)
        if data.get("remarks"):
            lines.append(f"{data['remarks']}.")
        
        # Closing
        lines.append(f"Advise on initial contact you have information {data['information_letter']}.")
        
        return " ".join(lines)
    
    def generate_atis(self, airport: Optional[Dict] = None, 
                      difficulty: str = "medium") -> Dict:
        """Generate a complete ATIS entry."""
        if airport is None:
            airport = random.choice(self.airports)
        
        # Validate difficulty
        if difficulty not in DIFFICULTY_SETTINGS:
            difficulty = "medium"
        
        # Generate all components
        wind = self.generate_wind(difficulty)
        visibility = self.generate_visibility(difficulty)
        rvr = self.generate_rvr(visibility, airport.get("runways", []), difficulty)
        weather = self.generate_weather(difficulty)
        clouds, cavok = self.generate_clouds(difficulty, visibility)
        temperature, dewpoint = self.generate_temperature(difficulty)
        qnh = self.generate_qnh(difficulty)
        transition_level = self.calculate_transition_level(qnh)
        active_runways = self.select_runways(airport, wind, difficulty)
        
        # Find the runway dict for approach selection
        runway_dict = {"ils": True}
        if airport.get("runways") and active_runways["arrival"]:
            for rwy in airport["runways"]:
                if rwy["designator"] == active_runways["arrival"][0]:
                    runway_dict = rwy
                    break
        
        approach_type = self.select_approach_type(runway_dict, visibility, clouds, difficulty)
        remarks = self.generate_remarks(difficulty, weather)
        information_letter = random.choice(NATO_ALPHABET)
        observation_time = datetime.utcnow() - timedelta(minutes=random.randint(0, 30))
        
        # Compile data
        data = {
            "airport": airport,
            "information_letter": information_letter,
            "observation_time": observation_time,
            "wind": wind,
            "visibility": visibility,
            "rvr": rvr,
            "weather": weather,
            "clouds": clouds,
            "cavok": cavok,
            "temperature": temperature,
            "dewpoint": dewpoint,
            "qnh": qnh,
            "transition_level": transition_level,
            "active_runways": active_runways,
            "approach_type": approach_type,
            "remarks": remarks,
            "difficulty": difficulty
        }
        
        # Generate full text
        data["full_text"] = self.generate_full_text(airport, data)
        
        return data
    
    def to_directus_format(self, atis_data: Dict, airport_id: int) -> Dict:
        """Convert generated ATIS data to Directus insert format."""
        wind = atis_data["wind"]
        
        return {
            "airport": airport_id,
            "information_letter": atis_data["information_letter"],
            "observation_time": atis_data["observation_time"].isoformat(),
            "wind_direction": wind["direction"],
            "wind_speed": wind["speed"],
            "wind_gust": wind["gust"],
            "wind_variable_from": wind["variable_from"],
            "wind_variable_to": wind["variable_to"],
            "visibility_meters": atis_data["visibility"],
            "rvr": atis_data["rvr"],
            "weather_phenomena": atis_data["weather"],
            "clouds": atis_data["clouds"],
            "cavok": atis_data["cavok"],
            "temperature": atis_data["temperature"],
            "dewpoint": atis_data["dewpoint"],
            "qnh": atis_data["qnh"],
            "active_runways": atis_data["active_runways"],
            "approach_type": atis_data["approach_type"],
            "transition_level": atis_data["transition_level"],
            "remarks": atis_data["remarks"],
            "full_text": atis_data["full_text"],
            "difficulty": atis_data["difficulty"]
        }


if __name__ == "__main__":
    # Test the generator with all difficulty levels
    generator = ATISGenerator()
    
    for difficulty in ["super_easy", "easy", "medium", "hard"]:
        print(f"\n{'='*70}")
        print(f"Sample ATIS - {difficulty.upper().replace('_', ' ')} difficulty")
        print(f"Description: {DIFFICULTY_SETTINGS[difficulty]['description']}")
        print('='*70)
        
        atis = generator.generate_atis(difficulty=difficulty)
        print(f"\n{atis['full_text']}")
        print(f"\n--- Details ---")
        print(f"Airport: {atis['airport']['icao']} - {atis['airport']['name']}")
        print(f"Wind: {atis['wind']}")
        print(f"Visibility: {atis['visibility']}m")
        print(f"QNH: {atis['qnh']} hPa")
        print(f"Approach: {atis['approach_type']}")
        if atis.get('weather'):
            print(f"Weather: {atis['weather']}")
        if atis.get('rvr'):
            print(f"RVR: {atis['rvr']}")
        if atis.get('remarks'):
            print(f"Remarks: {atis['remarks']}")
