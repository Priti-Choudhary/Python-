def print_gender(gender):
    match gender.upper():
        case "M":
            return "Male"
        case "F":
            return "Female"

gender = "M"
print(print_gender(gender))