def date_format(string):
    new_string = string.replace("/", "-")
    new_string = new_string[6:9]+new_string[5]+new_string[0:2]+new_string[3:4]
    return new_string
