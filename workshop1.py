#f = open("test.txt", mode='w')
#f.write("my first file\n")
#f.write("This file\n")
#f.write("contain three lines\n")
#f.close()

#with open("test.txt", 'r') as f:
#    text_string = f.read()
    # Run f.close()

#print(text_string)

print()
oper = input("provide operator:\n")
int1 = input("provide integer1:\n")
int2 = input("provide integer2:\n")
if(oper == 'x'):
    oper = '*'
print( int1, oper, int2 )
calc = int1 + oper
calc = calc + int2
print (calc)
val = eval(calc)
print(val)
