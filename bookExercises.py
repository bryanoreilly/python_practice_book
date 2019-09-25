#Exercises from the book python_practice_book
#https://buildmedia.readthedocs.org/media/pdf/python-practice-book/latest/python-practice-book.pdf

#Skipping ahead to test new concepts...
##Lambdas
def fxy(f, x, y):
    return f(x) + f(y)

cube = lambda x: x ** 3

#print(fxy (cube, 2, 3))
#print(fxy(lambda x: x**4 , 2, 3))

##Lists
#x = [1, 2, 3, 4, 5]
#print(x[:2])
#print(x[:])
#x =range(5)
#for i in x:
#   print (i, i*i, i*i*i,)

##27_
#def cumulative_sum(a):
#    d = []
    
#    for i in a:
#        d.append(sum(a[:i]))
#    return d


#print(cumulative_sum(x))
#print(cumulative_sum([4,3,2,1])) 
#This reverse doesnt print out the way expected: [4, 7, 9, 10]

##32_ Write a function lensort to sort a list of strings based on length
languages = ["python", "perl", "java", "c", "haskell", "ruby"]
def lensort(a):
   return a.sort(key = lambda x: len(x))

#print(languages)
lensort(languages)
print(languages)

##35_ Write a function extsort to sort a list of files based on extension
extensions = ['a.c','a.py', 'foo.txt', 'bar.txt', 'b.py', 'x.c']
def extsort(a):
    i = 0
    while(i<len(a)):
        a[i] =a[i].split('.')
        i = i + 1
    a.sort(key = lambda x: x[1])
    #print(a)
    i = 0
    while(i<len(a)):
        a[i] ='.'.join(a[i])
        i = i + 1
    #print(a)
    return a
          
#print(extensions)
extsort(extensions)
print(extensions)

##Example: Word Count ##

def charcount(filename):
    return len(open(filename).read())

def wordcount(filename):
    return len(open(filename).read().split())

def linecount(filename):
    return len(open(filename).readlines())

def printLines(filename):
    i = 1
    for line in (open(filename).readlines()):
        print(line.strip('\n') + ' ['+ str(i) +']')
        i = i + 1

##36_
def reverseLines(filename):
    lineCount = len(open(filename).readlines())
    lines = open(filename).readlines()
    while(lineCount > 0):
        print(lines[lineCount-1].strip('\n') + ' ['+ str(lineCount) + ']')
        lineCount = lineCount - 1
    
print(charcount("sheShells.txt"))
print(wordcount("sheShells.txt"))
print(linecount("sheShells.txt"))
printLines("sheShells.txt")
print()
#reverseLines("sheShells.txt")

##37_
def reverseTheLine(filename):
    reverseLine = ""
    full = []
    file = open(filename)
    for line in file:
        for letter in line:
            if(letter != '\n'):
                reverseLine = letter + reverseLine
            elif(letter == '\n'):
                print(reverseLine)
                full.append(reverseLine)
                reverseLine = ""
    #probably a poor way to do this.    
    #This skips the last line if there is no newline at the end of it

reverseTheLine("sheShells.txt")

##38_ heads&tails unix commands to print first and last 10 lines
#def headTailLines(filename):
#    print("Maybe another time. not trying unix commands on windows today")

##39_ grep the string. Print the lines
#def grepTheString():
#    print("same. not trying unix commands on windows today")
print()
##40_ takes file name and width, then wraps lines longer than width
def wrapByWidth(filename, width):
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        i = 0
        for letter in line:
            if(i > width-1):
                print()
                i = 0
            print(letter, end="")
            i = i + 1
            #print(i)
            

wrapByWidth("sheShells.txt", 15)
print()

##41_ better word wrap that doesnt break words apart
def wrapByWidth2(filename, width):
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        i = 0
        for letter in line:
            if((i > width-1) & (letter == " ")):
                print(letter)
                i = 0
            else:
                print(letter, end="")
                i = i + 1
            
    
wrapByWidth2("sheShells.txt", 15)

##42_ center align all lines in a file
def center_align():
    print()
