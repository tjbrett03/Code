a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))
rad = b**2-4*a*c
denom = 2*a
if rad < 0:
    print("error, negative")
elif(denom == 0):
    print("error, cannot divide by 0")
else:
    print("the roots are:",  (-b+rad**0.5)/denom, (-b-rad**0.5)/denom)
    
