import json


file_path = "json_practice/data.json"


# READ JSON
with open(file_path, "r") as file:
    data = json.load(file)

print("Original Data:")
print(data)


# MODIFY DATA
data["course"] = "Python Django Full Stack"


# WRITE JSON
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

print("\nUpdated data successfully.")


# READ AGAIN
with open(file_path, "r") as file:
    updated_data = json.load(file)

print("\nUpdated Data:")
print(updated_data)