def read_names():
    name_file = open("names.txt", "r")
    names = name_file.read().split(",")
    return names

