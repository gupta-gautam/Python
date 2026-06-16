# Dictionaries

info = {
    "name": "gautam",
    "age": 18,
    "titles": (84, 76, 33),
    "subjects": {
        "chem": 94,
        "maths": 95,
        "phy": 99
    }
}

print(type(info))

print(info)

print(info["subjects"]["maths"])

print(info.keys())
print(info.values())

print(info.get("name2"))  # if i write
# print(student["name2"]) will give an error

info.update({"city": "delhi"})

print(info)

# Sets
