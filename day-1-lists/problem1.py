students = [
    {"name": "Amit", "marks": 82, "city": "Bhopal"},
    {"name": "Riya", "marks": 91, "city": "Indore"},
    {"name": "Sam",  "marks": 67, "city": "Bhopal"},
    {"name": "Neha", "marks": 74, "city": "Indore"},
    {"name": "Karan", "marks": 58, "city": "Bhopal"},
]
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


result = analyze_students(students)
print(result)
print("\n\n------------\n\n")
print(analyze_students([]))   