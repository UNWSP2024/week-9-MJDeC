# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
def main():
  user_input=int(input('Enter the integer number of random numbers to be generated.'))
  if user_input>1000:
    print('Please enter a number lower than 1001.')
    main()
  else:
    outfile=open('rand.txt','w')
    for count in range(user_input):
      randnumb=random.randint(1,500)
      outfile.write(str(randnumb)+'\n')
    outfile.close()

main()
