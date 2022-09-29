# Thomas Brett-Labouchere 9/13/2022 CYB 267/268
temp = str(input("Enter Number:"))      # ask user for input
nums = []                               # initialize list
x = None                                # initialize the condition variable for while loop
i = 0                                   # count length of list
while x != ValueError:
    try:                                # try block to catch invalid input and end program        
        num = float(temp)               # try block attempts to convert the string temp to float num
        nums.append(num)
        i += 1                          # keep count of the length of list nums
        temp = str(input("Enter Number:")) 
            
    except ValueError:                  # runs if conversion of temp to float is unsucessful, resulting in a value error
        x = ValueError
        if temp.lower() == "done":      # make condition case insensitive, checks input variable if user has requested to end program by inputting "done"
            print("done")
            nums.sort(reverse = True)   # sort list from max being [0] to min being the last value
            if i != 0 :
                print("max: " , nums[0], "min:" , nums[i-1])    # print the maximum and minimum values, only if there are more than 0 values.
                                        # this prevents an error if the user inputs done and there are no values in the list
        else:                           # runs if user inputs anything other than break condtion "done" or list input
            print("invalid input, try again!")  
            temp = str(input("\nEnter Number:"))
            x = None                    # keep while loop conditon true, only affects anything if the try block fails, and the if statement returns false
                                        # runs the while loop until this condition is false