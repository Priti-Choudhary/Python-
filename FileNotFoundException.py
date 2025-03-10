def generate_file_not_found_exception():
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()

generate_file_not_found_exception()