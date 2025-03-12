def read_names():
    name_file = open("names.txt")
    names = name_file.read().split(",")
    return names

