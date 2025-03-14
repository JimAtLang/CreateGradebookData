def read_names():
    name_file = open("names.txt", "r")
    names = name_file.read().split(",")
    name_file.close()
    return names

