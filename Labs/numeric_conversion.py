# 3502C Lab 4 Code
# Written by: Michael Muraglia
# 6/18/20233

def hex_char_decode(digit):
    #  function to decode hex characters to digits
    #  below are logic gates for characters A - F
    #  Returns corresponding digit for character passed in
    if (digit == 'A') or (digit == 'a'):
        digit = 10
    elif digit == 'B' or (digit == 'b'):
        digit = 11
    elif digit == 'C' or (digit == 'c'):
        digit = 12
    elif digit == 'D' or (digit == 'd'):
        digit = 13
    elif digit == 'E' or (digit == 'e'):
        digit = 14
    elif digit == 'F' or (digit == 'f'):
        digit = 15

    digit = int(digit)

    return digit


def hex_string_decode(hex):
    #  returns decoded hex string
    result = 0  # initializing results variable
    index = 0  # Initializing indexing variable
    if hex[0:2] == '0x':  # removes unnecessary hexadecimal prefix
        hex = hex[2::]
    for digit in hex[::-1]:
        digit = int(hex_char_decode(digit))  # Coverts str to int
        result += digit * 16 ** index  # stores current result of calculation
        index += 1
    return result


def binary_string_decode(binary):
    #  returns decoded binary string
    result = 0  # initializing results variable
    index = 0  # Initializing indexing variable
    if binary[0:2] == '0b':  # removes unnecessary binary prefix
        binary = binary[2::]
    for digit in binary[::-1]:
        digit = int(digit)  # Coverts str to int
        result += digit * 2 ** index  # stores current result of calculation
        index += 1
    return result


def binary_to_hex(binary):
    #  Converts Binary string to corresponding Hex String
    result = 0  # initializing results variable
    final_result = ""  # initializing final results variable
    if binary[0:2] == '0b':  # removes unnecessary hexadecimal prefix
        binary = binary[2::]
    binary = int(binary)  # Converting to int
    while binary > 0:
        cluster = binary % 10000  # Gets next 4 sequence of numbers
        cluster = str(cluster)  # converts to string
        index = 0  # indexing variable
        for digit in cluster[::-1]:  # iterates through the cluster
            digit = int(digit)  # converts to int
            digit = digit * 2 ** index
            index += 1
            result += digit
        # determine if the custer represented a character and if so assigns it to correct character
        if result == 10:
            result = 'A'
        elif result == 11:
            result = 'B'
        elif result == 12:
            result = 'C'
        elif result == 13:
            result = 'D'
        elif result == 14:
            result = 'E'
        elif result == 15:
            result = 'F'
        else:
            result = str(result)  # converts to string
        final_result = result + final_result  # concatenate results
        result = 0  # resets results variable
        binary = binary // 10000  # removes previous 4 looked at digits
    return final_result


def main():
    while True:
        #  main menu printing
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit\n")

        #  user selection
        user_selection = int(input('Please enter an option: '))

        if user_selection == 1:
            user_string = input("Please enter the numeric string to convert: ")

            decoded = hex_string_decode(user_string)
            print(f'Result: {decoded}\n')

        elif user_selection == 2:
            user_string = input("Please enter the numeric string to convert: ")
            decoded = binary_string_decode(user_string)
            print(f'Result: {decoded}\n')

        elif user_selection == 3:
            user_string = input("Please enter the numeric string to convert: ")
            decoded = binary_to_hex(user_string)
            print(f'Result: {decoded}\n')

        elif user_selection == 4:  # user exits program
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
