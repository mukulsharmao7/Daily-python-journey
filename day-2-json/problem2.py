import json

students = [
    {"name": "Amit", "marks": 82, "city": "Bhopal"},
    {"name": "Riya", "marks": 91, "city": "Indore"},
    {"name": "Sam", "marks": 67, "city": "Bhopal"},
    {"name": "Neha", "marks": 74, "city": "Indore"},
    {"name": "Karan", "marks": 58, "city": "Bhopal"},
]


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


save_to_json(students, "students.json")





def load_from_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File nahi mili: {filename}")
        return []


loaded_students = load_from_json("students.json")
print("Loaded:", len(loaded_students), "students")

not_found_result = load_from_json("galat_naam.json")
print("Not found result:", not_found_result)