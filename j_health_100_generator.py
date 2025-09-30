import pandas as pd
import numpy as np
import random

def generate_j_health_100():
    regions = ["Tokyo", "Osaka", "Hokkaido", "Okinawa", "Kyoto"]
    seasons = ["spring", "summer", "autumn", "winter"]
    data = []
    for i in range(100):
        region = random.choice(regions)
        season = random.choice(seasons)
        base_hr = 72
        base_steps = 4000 if region in ["Tokyo","Osaka"] else 3000
        if season == "summer": base_hr += random.randint(3,8)
        elif season == "winter": base_steps = int(base_steps * 0.6)
        sample = {
            "user_id": f"JP_ELDER_{i+1:03d}",
            "region": region,
            "season": season,
            "avg_heart_rate": base_hr + random.randint(-5,5),
            "daily_steps": base_steps + random.randint(-500,500),
            "sleep_hours": 7 + random.uniform(-1,1),
            "bath_time_min": 30 + random.randint(0,20)
        }
        data.append(sample)
    df = pd.DataFrame(data)
    df.to_csv("j_health_100.csv", index=False)
    print("Generated j_health_100.csv with 100 profiles.")
    return df

if __name__ == "__main__":
    generate_j_health_100()
