# CYB 267 Thomas Brett
# 10/21/2022
h = 2 # made up h for now
f = [5, 8, 3] # made up f for now
# f(x) ~= a0 + a1x + a2x^2
# f0 = f0
# f1 = a0 + ha1 + h^2a2
# f2 = a0 + 2ha1 + 4h^2a2 

# a0 = f0
# a1 = (1/2h) (-3f0+4f1-f2)
# a2 = (1/2h^2) (f0-2f1+f2)
a = []
a.append(f[0])
a.append((1/(2*h))*(-3*f[0] + 4*f[1] - f[2]))
a.append((1/(2*h**2))*(f[0] - 2*f[1] + f[2]))
x = float(input("enter the number you want a value for:  "))
f_x = a[0] + a[1]*x + a[2]*x**2
print(f"Your answer is {f_x: .2f}")