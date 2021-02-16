with open("test.txt","r") as handle:
    data = handle.read()
    print(data)

handle = open("text.txt", "w")

handle.write("Hello Moringa")
handle.close()