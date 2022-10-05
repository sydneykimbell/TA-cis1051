# ask user how much money they have
# ask user what currency they have
# ask user what currency they want to convert to
# convert currency
# print output


# USER INPUT

def get_user_money():
    '''this function should ask the user for input and return a float value with their total amount of money'''

def get_user_cur_type():
    '''this function should ask the user for input and return a string value with the currency type they currently have'''

def get_cur_to_convert():
    '''this function should ask the user for input and return a string value with the currency type they want to convert to'''


# CONVERSION

def convert_to_usd(total, cur_type):
    '''this function should convert any currency to USD and return a float
    parameters:
    - total: the amount of money the user wants to convert
    - cur_type: the type of currency the user wants to convert to USD'''


def convert_from_usd(total, cur_type):
    '''this function should take in USD and convert to another currency and return a float
    parameters:
    - total: the amount of money the user wants to convert
    - cur_type: the currency the user wants to convert from USD'''


# PRINT OUTPUT

def get_output(initial_total, initial_cur, final_total, final_cur):
    '''this function should take in 4 parameters to print a message about the output of the conversion. this method should return a string'''


def main():

    # first get the user's total money
    total = get_user_money()
    # next, get the current currency type
    initial_cur = get_user_cur_type()
    # then, get the desired currency type
    final_cur = get_cur_to_convert()

    # use a conditional expression to decide to use convert_to_usd or convert_from_usd
    # note that pass is just a placeholder here. replace pass with your own code
    if initial_cur == 'USD' and final_cur != 'USD':
        final = convert_from_usd(total, final_cur)
    elif initial_cur != 'USD' and final_cur == 'USD':
        final = convert_to_usd(total, initial_cur)
    elif initial_cur != 'USD' and final_cur != 'USD':
        middle = convert_to_usd(total, initial_cur)
        final = convert_from_usd(middle, final_cur)
    else:
        final = total

    # make a call to your get_output function and print the output. get_output should return a string so you should set it equal to a variable and print from main.


main()
