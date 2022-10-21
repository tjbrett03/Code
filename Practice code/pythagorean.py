# Thomas Brett
def pythagorean(a):
    a[2] = a[0]**2 + a[1]**2

def main():
    a = [0,0,0]
    a[0] = float(input('input a: '))
    a[1] = float(input('input b: '))
    a[2] = 0
    pythagorean(a)
    print(a[2])

main()
