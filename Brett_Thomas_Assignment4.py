# thomas brett assignment 4
temp = str(input("Enter Number:"))
nums = []
x = None 
i = 0
while x != ValueError:
    try:                                #try block to catch invalid input and end program        
        num = float(temp)
        nums.append(num)
        i += 1
        temp = str(input("Enter Number:"))
            
    except ValueError:
        x = ValueError
        if temp.lower() == "done":
            print("done")
            nums.sort(reverse = True)
            print("max: " , nums[0], "min:" , nums[i-1])
        else:
            print("invalid input, try again!")
            temp = str(input("\nEnter Number:"))
            x = None

