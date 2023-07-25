import os
#f = open("test.txt", mode='w')
#f.write("my first file\n")
#f.write("This file\n")
#f.write("contain three lines\n")
#f.close()

#with open("test.txt", 'r') as f:
#    text_string = f.read()
    # Run f.close()

#print(text_string)

#oper = input("provide operator:\n")
#int1 = input("provide integer1:\n")
#int2 = input("provide integer2:\n")
def calc (oper, int1, int2):
    if(oper == 'x'):
        oper = '*'
        #print( int1, oper, int2 )
    calc = int1 + oper
    calc = calc + int2
    #print(calc)
    val = eval(calc)
    return val
        
#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

def checkLine(LineNum):
    print("hello")

def ReadAndCalc ():
    #with open("copy_step_2.txt", 'r') as f:
    with open("step_2.txt", 'r') as f:
        #for line in f:
        text_string = f.read().splitlines()
        #print(text_string, len(text_string))
        #print(len(text_string))
        i = 0
        total = 0
        goLine = 0
        while i < len(text_string):
            #print("Calculating ", text_string[i])
            data_line = text_string[i].split()
            if (len(data_line) > 2):
                goLine = calc(data_line[2], data_line[3], data_line[4])
                #print(calc(data_line[1], data_line[2], data_line[3]))
            else:
                goLine = data_line[1]
            i = goLine
            if (checkLine(goLine) > 1):
                f.close()
                return i
    f.close()

ReadAndCalc ()
#print(text_string)

