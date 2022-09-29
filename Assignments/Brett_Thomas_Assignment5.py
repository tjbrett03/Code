# Thomas Brett Labouchere | CYB 267 9/21/2022
def phone_function(userinput): # define function with argument
    numlist = []
    for x in str(userinput): # repeat for every number in userinput variable
        numlist.append(str(x)) # add said number to list 'numlist'
        area_code = "(" + "".join(numlist[0:3]) + ") " # create variable area code and assign it value
        middle = "".join(numlist[3:6]) + "-" # middle of phone number
        end = "".join(numlist[6:10]) # end of phone number 
        phone_number = area_code + middle + end # put all three parts together
    print(phone_number) # print outside of for loop so that phone number only prints once and when completed
try: # try block to catch non number input
    phone_function(int(input("enter phone number: ")))
except ValueError: # print 'value error!' if userinput is not an integer
    print("value error!")




