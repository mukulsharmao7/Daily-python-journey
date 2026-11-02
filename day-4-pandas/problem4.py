import json

import pandas as pd


def load_from_json(filename):
    """JSON file padhta hai. File na mile to khaali list return karta hai."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File nahi mili: {filename}")
        return []


# ---------- Step 1: JSON se DataFrame ----------
users = load_from_json("users.json")   # Python list of dicts
df = pd.DataFrame(users)               # list -> table

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns)
df.info()                              # khud print karta hai


# ---------- Step 2: Column aur row chunna ----------
print("Names:\n", df["name"])
print("Name + City:\n", df[["name", "city"]])
print("First row:\n", df.iloc[0])
print("Last row:\n", df.iloc[-1])

print("Type of df['name']:", type(df["name"]))
print("Type of df[['name', 'city']]:", type(df[["name", "city"]]))


# ---------- Step 3: Filter aur Sort ----------
# 1. id > 5 wale users
filtered = df[df["id"] > 5]
print("id > 5:\n", filtered)

# 2. Filter + sirf name aur email
print("Name + Email (id > 5):\n", df[df["id"] > 5][["name", "email"]])

# 3. name ke hisaab se A-Z (poori table)
print("Sorted by name:\n", df.sort_values("name"))

# 4. id ke hisaab se bade se chhota (poori table)
print("Sorted by id desc:\n", df.sort_values("id", ascending=False))

# 5. ginti
print("Users with id > 5:", len(filtered))