import json

import requests

URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users(url):
    """API se users laata hai. Error aane par khaali list return karta hai."""
    try:
        response = requests.get(url, timeout=10)   # 1. request bhejo
        response.raise_for_status()                # 2. 404/500 par error uthao
        return response.json()                     # 3. sab theek to data do
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")                   # 4. error aaya to message
        return []                                  # 5. crash nahi, khaali list


def extract_user_info(user):
    """Ek user dictionary se kaam ki 5 cheezein nikalta hai."""
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "city": user["address"]["city"],
        "company": user["company"]["name"],
    }


def save_to_json(data, filename):
    """Data ko JSON file mein save karta hai."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_from_json(filename):
    """JSON file padhta hai. File na mile to khaali list return karta hai."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File nahi mili: {filename}")
        return []


def main():
    # Sahi URL
    good_users = fetch_users(URL)
    print("Good URL users:", len(good_users))

    # Galat URL
    bad_users = fetch_users("https://jsonplaceholder.typicode.com/galat-page")
    print("Bad URL users:", len(bad_users))

    # Cleaned data
    clean_users = [extract_user_info(u) for u in good_users]
    print("Total:", len(clean_users))
    print("First:", clean_users[0])

    # Save karo, phir wapas padhke check karo
    save_to_json(clean_users, "users.json")
    loaded_users = load_from_json("users.json")
    print("Loaded from file:", len(loaded_users))


if __name__ == "__main__":
    main()