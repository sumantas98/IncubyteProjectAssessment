import re
def addition(random_string):
    if random_string == "" or re.match(r'^\D*$', random_string):
        return 0
    '''
    ### Handle only Twice number with comma ###
    if "," in random_string:
        num_list = random_string.split(",")
        return int(num_list[0]) + int(num_list[1])
    '''

    # This Function will handle multiple "," separated numbers like "1,2,3" out put should be 6.
    # Before split it will replace all the \n value with comma then it can use the same function with any further modification.
    random_string = random_string.replace('\n',',')
    list_num = random_string.split(',')
    return sum(int(num) for num in list_num)



