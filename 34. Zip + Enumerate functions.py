names = ["Jack", "Anna", "Helga"]
ages = [26, 39, 41]

for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index + 1}.{name} > {age}")