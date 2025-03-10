# Create a dictionary with student IDs and names
student_dict = {
    "S001": "John Doe",
    "S002": "Jane Doe",
    "S003": "Bob Smith",
    "S004": "Alice Johnson",
    "S005": "Mike Brown"
}

# 1.1 Adding values to the dictionary
student_dict["S006"] = "Emma Davis"
print("Updated dictionary:", student_dict)

# 1.2 Updating values in the dictionary
student_dict["S002"] = "Jane Smith"
print("Updated dictionary:", student_dict)

# 1.3 Accessing values in the dictionary
print("Student name for S003:", student_dict["S003"])

# 1.4 Create a nested loop dictionary
nested_dict = {
    "S001": {"name": "John Doe", "grade": "A"},
    "S002": {"name": "Jane Smith", "grade": "B"},
    "S003": {"name": "Bob Smith", "grade": "C"}
}
print("Nested dictionary:", nested_dict)

# 1.5 Access values of nested loop dictionary
print("Student name for S002:", nested_dict["S002"]["name"])
print("Student grade for S003:", nested_dict["S003"]["grade"])

# 1.6 Print keys present in a particular dictionary
print("Keys in student_dict:", student_dict.keys())

# 1.7 Delete a value from a dictionary
del student_dict["S004"]
print("Updated dictionary after deletion:", student_dict)