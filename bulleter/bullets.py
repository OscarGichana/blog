text_file = "test.txt"

def bullet_file(text_file):
    '''
    Function that adds * at the begining of a line.
    '''

with open("test.txt", "r") as f:
    data = f.readlines()
    print(data)
data = [' *  '+line for line in data]

f = open("text.txt", "w")
f.writelines(data)
f.close()



def capital_file(text_file):
    '''
    Function that capitalizes 1st word of a line.
    '''

with open("test.txt", "r") as file:
	cakes = file.readlines()
	for c in cakes:
		lines = c.split(" ")
		print(lines[0])

for l in lines:
  capital = [lines[0].upper()+line for line in cakes]
  print(capital)
l  = open("tst.txt", "w")
l.writelines(capital)
l.close()

