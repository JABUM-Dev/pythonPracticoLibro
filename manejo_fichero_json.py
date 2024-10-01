import json

json_file = open("my_file.json", "w+")

json_test = {
    "name":"Andres",
    "surname":"Mendoza",
    "age":32,
    "language":["Python","VB 6.0", "C#"],
    "website":"https://notengo.com",
}

json.dump(json_test, json_file, indent= 4)

json_file.close()

with open("my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# proceso contrario
json_dict = json.load(open("my_file.json"))
print(json_dict)
