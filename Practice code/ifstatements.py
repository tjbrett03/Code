# Thomas Brett-Labouchere 9/9/2022 CYB 267
planets = ["earth", "saturn", "neptune", "mars"] # Create array with names of planets
density = [1.217, 0.19, 0.45, 0.020]             # Create array with density values of planets
accel = [9.798, 10.44, 11.15, 3.71]              # Create array with acceleration values of planets
userinput = str(input("Planet: ")) 
a = userinput.lower()                       # make program case insensitive
for a in planets:                         # For each iteration of user input in array planets
    print(userinput)
    x = planets.index(a)                 # Set x to the index of user input
    print("Density: ", density[x])               # Print values based on index of user input
    print("Acceleration due to gravity: ", accel[x])
    break