def generate_io_exception():
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()

generate_io_exception()