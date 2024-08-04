import numpy as np
import pandas as pd

# Helper function to generate fantasy names
def generate_fantasy_name(prefix, i):
    root = ['Zar', 'Mor', 'Kyr', 'Fen', 'Tor', 'Ser', 'Nar', 'For', 'Gel', 'Bor', 'Syl', 'Cyr']
    suffix = ['ox', 'ith', 'ath', 'um', 'as', 'or', 'on', 'an', 'ian', 'ius', 'en', 'ael']
    return f"{prefix}{np.random.choice(root)}{np.random.choice(suffix)}{i}"

# Improved name generation based on the dominant attribute
def generate_name_with_attribute(i, strength, magic, agility, wisdom):
    base_name = generate_fantasy_name("", i)
    dominant_attribute = max(strength, magic, agility, wisdom)
    if dominant_attribute == strength:
        prefix = "Mighty"
    elif dominant_attribute == magic:
        prefix = "Mystic"
    elif dominant_attribute == agility:
        prefix = "Swift"
    else:
        prefix = "Wise"
    return f"{prefix} {base_name}"

# Data generation for 120 unique creatures
data = {
    "creature_id": [f"creature_{i}" for i in range(1, 121)],
    "strength": np.random.randint(10, 100, size=120),
    "magic": np.random.randint(10, 100, size=120),
    "agility": np.random.randint(10, 100, size=120),
    "wisdom": np.random.randint(10, 100, size=120),
    "ability_effect_damage": np.random.randint(5, 50, size=120),
    "ability_effect_area": [f"{np.random.randint(1, 10)} meters" for _ in range(120)]
}

data["name"] = [generate_name_with_attribute(i, s, m, a, w) for i, s, m, a, w in zip(
    range(1, 121),
    data["strength"],
    data["magic"],
    data["agility"],
    data["wisdom"]
)]

data["description"] = [f"A mystical creature known for its {np.random.choice(['incredible strength', 'mysterious powers', 'ancient wisdom'])}." for _ in range(120)]
data["ability_name"] = [generate_fantasy_name("Ability", i) for i in range(1, 121)]
data["ability_description"] = [f"Grants the power to {np.random.choice(['call forth fire', 'manipulate the winds', 'control the seas', 'warp the reality'])}." for _ in range(120)]
data["image"] = ["template_creature_image.png" for _ in range(120)]
data["card_image"] = ["template_card_image.png" for _ in range(120)]
data["character_image"] = ["template_character_image.png" for _ in range(120)]
data["rarity"] = [np.random.choice(['common', 'rare', 'legendary'], p=[0.7, 0.2, 0.1]) for _ in range(120)]

# Create DataFrame and save to CSV
creatures_df = pd.DataFrame(data)
creatures_csv_path = "/mnt/data/Enhanced_Unique_Creatures.csv"
creatures_df.to_csv(creatures_csv_path, index=False)
