print("How To Dress")
temp = int(input("Current Outside Temperature (in Farenheit): "))  # ask user to input current temperature 
if temp >= 80:                                      # if & elif statements run to check temp, displays proper response for what to wear
    print("Wear shorts and a t-shirt")
elif temp >=70 and temp < 80:                       # and statements catch low end of temp range for any given response
    print("Wear shorts or long pants and a t-shirt")
elif temp >=50 and temp < 70:
    print("Wear long pants, a t-shirt, and a light coat")
elif temp >= 30 and temp < 50:
    print("Wear Long pants, long sleeve shirt, and a coat")
elif temp >= 0 and temp < 30:
    print("Wear long pants, long sleeve shirt, and a heavy coat")
elif temp >= -40 and temp < 0:
    print("Wear long pants, a long sleeve shirt, heavy coat, hat, and gloves")
elif temp < -40:
    print("Wear pajamas, dont go out")
