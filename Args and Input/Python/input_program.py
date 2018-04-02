#! python

import sys

# Function used to process standard input
def process_standard_input():
    print("Standard Input:") #Prints header
    while True: #Keep prompting until break
        try: #try catch in order to catch ^CTRL + D
            user_input = input() #Prompt user_input
            print(user_input) #Print what they typed in
        except EOFError: #EOFError is ^CTRL + D on MAC + LINUX
            break # Exit while and stop asking for input
    process_command_line_arguments() #call function to process command line arguments

# Function used to process command line arguments       
def process_command_line_arguments():
    print("Command line arguments:") #Prints header
    option1 = "" # Sets a empty string to be used
    option1flag = False # Sets a empty boolean to be set to test presence
    option2 = "" # Sets a empty string to be used
    option2flag = False # Sets a empty boolean to be set to test presence
    option3 = "option 3" # Sets option3 string to be used
    option3flag = False # Sets a empty boolean to be set to test presence
    for index, data in enumerate(sys.argv): # for loop using enumerate because we need indexes of data next to the arg
        if data == "-o": #if data in sys.argv is '-o' set option1 to be the next item and set the presence flag to true
            try: # Try except for indexerror on outlier cases (ie python input_program.py -h -t Something -o) indexerror after -o
                if "-" not in sys.argv[index+1]: #Check if the next item is NOT another argument. If it is don't save it. 
                    option1 = sys.argv[index + 1] 
                    option1flag = True #Sets presence flag to True
            except (ValueError,IndexError): 
                pass
        if data == "-t": #if data in sys.argv is '-t' set option2 to be the next item and set the presence flag to true
            try: # Try except for indexerror on outlier cases (ie python input_program.py -h -o Something -t) indexerror after -t
                if "-" not in sys.argv[index+1]: #Check if the next item is NOT another argument. If it is don't save it. 
                    option2 = sys.argv[index + 1]
                    option2flag = True #Sets presence flag to True
            except (ValueError,IndexError):
                pass
        if data == "-h": #if data in sys.argv is '-h' set the presence flag to true
            option3flag = True #Sets presence flag to True
    if len(option1) != 0 and option1flag == True: # Check and only print if len(option1 is not 0) and option1flag has been set to True
        print("option 1: " + option1)
    if len(option2) != 0 and option2flag == True: # Check and only print if len(option2 is not 0) and option2flag has been set to True
        print("option 2: " + option2)
    if option3flag == True: # Check and only print if option3flag has been set to True
        print(option3)

           
if __name__ == "__main__":
   process_standard_input()
