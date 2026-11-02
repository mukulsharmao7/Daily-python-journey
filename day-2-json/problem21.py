import json


def analyze_students(students):
    """Students ki list se names, average, above-average aur Bhopal count return karta hai."""
    if not students:
        return {"names": [], "average": 0, "above_average": [], "bhopal_count": 0}

    names = [s["name"] for s in students]

    marks = [s["marks"] for s in students]
    average = sum(marks) / len(marks)

    above_average = [s["name"] for s in students if s["marks"] > average]
    bhopal_count = len([s for s in students if s["city"] == "Bhopal"])

    return {
        "names": names,
        "average": average,
        "above_average": above_average,
        "bhopal_count": bhopal_count,
    }


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_from_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File nahi mili: {filename}")
        return []


def main():
    students = [
        {"name": "Amit", "marks": 82, "city": "Bhopal"},
        {"name": "Riya", "marks": 91, "city": "Indore"},
        {"name": "Sam", "marks": 67, "city": "Bhopal"},
        {"name": "Neha", "marks": 74, "city": "Indore"},
        {"name": "Karan", "marks": 58, "city": "Bhopal"},
    ]

    save_to_json(students, "students.json")             # 1. save
    loaded_students = load_from_json("students.json")   # 2. load
    result = analyze_students(loaded_students)          # 3. analyze
    save_to_json(result, "result.json")                 # 4. save result
    print(result)


if __name__ == "__main__":
    main()