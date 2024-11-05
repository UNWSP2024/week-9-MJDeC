# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    # Add your code here #
    try:
        infile=('numbers.txt','r')
        total=0
        for line in 'numbers.txt':
            number=float(line.strip())
            total+=number
        filename = "numbers.txt" 
        result = sum_numbers_in_file(filename)
        infile.close()
        print('In the sum_numbers_from_file function')
        print('the sum of numbers is', result,'.')
    except IOError:
        print('There was an error locating and/or reading the file. Apologies for the inconvenience.')
    except ValueError:
        print('There was an error converting file items to numbers. Apologies for the inconvenience.')
    ######################

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
