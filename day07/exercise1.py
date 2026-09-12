def get_city(students, name):
    return students[name]["city"]


student = {
    "george": {"age": 22, "city": "Handan"},
    "alex": {"age": 25, "city": "Berlin"}
}

print(get_city(student, "alex"))
print(get_city(student, "george"))
print(get_city(student, "omiman"))