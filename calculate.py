import re
def addition(random_string):
    if random_string == "" or re.match(r'^\D*$', random_string):
        return 0
    if "," in random_string:
        num_list = random_string.split(",")
        return int(num_list[0]) + int(num_list[1])
    return int(random_string)



