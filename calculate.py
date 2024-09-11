import re
def addition(random_string):
    if random_string == "" or re.match(r'^\D*$', random_string):
        return 0
    return int(random_string)



