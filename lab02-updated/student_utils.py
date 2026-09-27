"""Reusable helpers for working with student records (GPA out of 5.00)."""

DEANS_LIST_MIN = 4.50


def average_gpa(roster):
    """Return the average GPA of a roster. Returns 0.0 if empty."""
    if not roster:
        return 0.0
    gpas = [student["gpa"] for student in roster]
    return sum(gpas) / len(gpas)


def dean_list_names(roster):
    """Return the names of students at or above the Dean's List threshold."""
    names = []
    for student in roster:
        if student["gpa"] >= DEANS_LIST_MIN:
            names.append(student["name"])
    return names
