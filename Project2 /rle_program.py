# COP3502 Project 2B - Run-length Encoding (RLE) with Images Python
# Coder: Michael Muraglia
# Date: 7/9/2023

from console_gfx import ConsoleGfx


def to_hex_string(data):  # converts hex to string
    string = ""
    for datapoint in data:
        if datapoint <= 9:  # if hex number is <= 9
            string += str(datapoint)
        elif datapoint == 10:  # if hex number is between 10 and 15
            string += 'a'
        elif datapoint == 11:
            string += 'b'
        elif datapoint == 12:
            string += 'c'
        elif datapoint == 13:
            string += 'd'
        elif datapoint == 14:
            string += 'e'
        else:
            string += 'f'
    return string  # returns string value of hex number


def count_runs(flat_data):  # counts the number of runs in unencoded data
    runs = 1 # initializes variable
    current = flat_data[0]  # current number being investigated
    count = 1  # How many times current appears
    for num in flat_data[1:]:
        if current == num:
            count += 1  # Increments count variable
            if count == 15:  # determines if current run is longer than 15 pixels
                runs += 1
                count = 1
                current = num
        else:
            runs += 1
            count = 1
            current = num
    return runs


def encode_rle(flat_data):  # encodes flat data to rle data
    current = flat_data[0]  # current number being investigated
    count = 1  # How many times current appears
    rle = []  # run length array to be returned
    finalvalue = len(flat_data[1:])  # determines if on final value of flat data
    iterations = 0  # variable to help determine if on final value of flat data

    for num in flat_data[1:]:
        iterations += 1
        if count == 15:  # determines if current run is 15 or greater
            count = 1
            current = num
            continue
        if current == num:
            count += 1  # Increments count variable
            if count == 15:  # determines if current run is 15 or greater
                rle.append(count)  # appends count to rle list
                rle.append(current)  # appends current value to rle list
        else:
            rle.append(count)  # appends count to rle list
            rle.append(current)  # appends current value to rle list
            count = 1
            current = num
        if iterations == finalvalue:  # adds final value of flat data to rle list
            rle.append(count)
            rle.append(current)
    return rle


def get_decoded_length(rle_data):  # determines decompressed size rle data
    counter = 0
    length = 0
    for digit in rle_data:
        if counter == 0 or counter % 2 == 0:  # starts at 0 index rle_data entry and increments by 2 to select frequency
            length += digit  # adds frequency
            counter += 1
        else:
            counter += 1
            continue
    return length


def decode_rle(rle_data):  # returns decoded rle list
    decoded = []  # initializes decoded rle list
    for i in range(0, len(rle_data), 2):  # creates variable i to iterate through every other value in rle list
        for j in range(0, rle_data[i]):  # iterates through indicated number of frequency for desired number of pixels
            decoded.append(rle_data[i+1])  # appends correct number of indicated number of pixels
    return decoded


def string_to_data(data_string):  # translates hexadecimal formate into byte data
    bytedata = []
    for digit in data_string:
        if (digit == '0') or (digit == '1') or (digit == '2') or (digit == '3') or (digit == '4') or (digit == '5') or \
           (digit == '6') or (digit == '7') or (digit == '8') or (digit == '9'):  # determines if digit is 0-9
            digit = int(digit)  # converts digit to int
            bytedata.append(digit)
        elif digit == 'a':  # determines if digit is a-f and coverts to 10-15 respectively
            digit = 10
            bytedata.append(digit)
        elif digit == 'b':
            digit = 11
            bytedata.append(digit)
        elif digit == 'c':
            digit = 12
            bytedata.append(digit)
        elif digit == 'd':
            digit = 13
            bytedata.append(digit)
        elif digit == 'e':
            digit = 14
            bytedata.append(digit)
        elif digit == 'f':
            digit = 15
            bytedata.append(digit)
    return bytedata


def main():
    # Display Welcome Message
    print("Welcome to the RLE image encoder!\n")

    # Display Spectrum Message
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    image_data = None

    while True:
        # 1. print all the menu Options
        print("\nRLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data\n")

        # Prompt the user for menu option
        option = int(input("Select a Menu Option: "))
        # Set up option 0, 1, 2, 6 properly (Part A)
        if option == 0:
            break
        elif option == 1:
            # Prompt the filename entered by user
            image_data = input('Enter the name of file to load: ')
            image_data = ConsoleGfx.load_file(image_data)
        elif option == 2:
            # Store the ConsoleGfx image
            image_data = ConsoleGfx.test_image
        elif option == 6:
            # Display loaded image
            ConsoleGfx.display_image(image_data)


if __name__ == "__main__":
    main()
