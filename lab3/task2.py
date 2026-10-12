name = input()
last_name, first_name, middle_name = name.split()
result = f"{last_name.capitalize()} {first_name[0].upper()}. {middle_name[0].upper()}."
print(result)
