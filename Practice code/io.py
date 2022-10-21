def filefunction():
    file = open("test.txt", "w")
    userin = str(input("enter some text: "))
    while userin.lower() != "done":
            file.write(userin)
            userin = str(input("enter some text: "))

    file = open("test.txt", "r")
    print(file.read())
filefunction()





