i = 10  # starting # of intervals
interval = 3.1/i    # interval
equation = lambda x : -0.5*x**3 + x**2 + 2*x +1
equationOutput = [0]
rectangleAreas = []
def mathFunction():
    x = 0
    while x < 3.1:
        x += interval
        equationOutput.append((equation(x)))
        #print(equationOutput)

    for i in equationOutput:
        num1 = equationOutput[int(i)]
        print(num1)
        rectangleAreas.append((num1 * interval))
    print(num1)
    area = float(sum(rectangleAreas))
    print(area)
    e = area 
    if e < 0.01: 
        i += 1
mathFunction()

