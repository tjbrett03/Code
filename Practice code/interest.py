# compund and simple interest
print("Interest Calculator")
principal1 = None
period = float(input("Period in Years: "))
principal = float(input("Principal: "))
rate = float(input("Interest Rate: "))/100
final = None
def comp_int():
    final = principal * (pow((1 + rate), period))
    interest = final - principal
usr_select = str(input("Compund or Simple Interest: "))
if usr_select.lower() == "compound":
    comp_int()
    print(final)


# NOT DONE!