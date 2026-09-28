file_path = "python_exercises/sample.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()

    print("File Content:")
    print("----------------")
    print(content)

except FileNotFoundError:
    print("File not found.")