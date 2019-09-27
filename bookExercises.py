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

##16_ Write a function extsort to sort a list of files based on extension
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

##17_
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

##18_
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

##19_ heads&tails unix commands to print first and last 10 lines
#def headTailLines(filename):
#    print("Maybe another time. not trying unix commands on windows today")

##20_ grep the string. Print the lines
#def grepTheString():
#    print("same. not trying unix commands on windows today")
print()
##21_ takes file name and width, then wraps lines longer than width
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

##22_ better word wrap that doesnt break words apart
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
print()

##23_ center align all lines in a file
def center_align(filename):
    f = open(filename)
    lines = f.readlines()
    line = f.readline()
    longest = 0
    for l in lines:
        if (len(l) > longest):
            longest = len(l)
    print(longest)
    
    for l in lines:
        if(len(l) < longest):
            s = (longest - len(l))/2
            s = int(s)
            for i in range(0, s):
                print(" ", end="")
            print(l)
        else:
            print(l)

center_align("sheShells.txt")

## 2.6 List Comprehensions
#a = range(10)
#print([x for x in a if x%2 == 0])

#apparently
#filter() and map() dont work normally in python3
def even(x): return x %2 == 0

##27_  returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n.
def triplets(n):
    return [(x, y,z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if (x+y) == z]

print(triplets(5))
print()

##28_ enumerate(): takes list and returns a tuple of (index, value) for each item
def enumerate(l):
    index = []
    cnt = 0
    for i in l:
        index.append(cnt)
        cnt += 1
    print(index)
    
    for index, value in zip(index, l):
        print(index, value)
        
enumerate(["a","b","c"])

#another solution found online. but it doesnt print out as example
def enumerate2(l):
    return[(index, l[index]) for index in range(len(l))]


print(enumerate2(["a","b","c"]))
print()

##29_ array(): create a 2 dimensional array. values init as None
def array2d(x , y):
    xa = []
    ya = []
    z= []
    for i in range(0, x):
        xa.append("None")
    print(xa)
    for j in range(0, y):
        ya.append("None")
    print(ya)
    #z = [["None" for i in range(x)] ["None" for j in range(y)]]
    z.append(xa)
    z.append(ya)
    return z
    
a2 = array2d(2, 3)
print(a2)
print()

##30_ parse_csv
#not really parsing by commas at this point.. but it works close enough to requirements
def parse_csv(file):
    f = open(file)
    p = []
    for line in f.readlines():
        p.append([line])
    print(p)

new_csv_path = 'C:\\polap_dev\\winshuttle\\sapTcodeCsv.csv'
#parse_csv(new_csv_path)

##31_Generalize 30 to take any deliminator as an argument, plus skip comments
#This solution was found online. It uses 'r' and follows the list comprehension as the example requested
def parse(file, delimiter, c):
    lines = open(file, 'r', encoding='utf-8').readlines()
    return [line.strip().split(delimiter) for line in lines if line.strip()[0] != c]

   
print(parse(new_csv_path, ',', '#'))
print()

##32_ mutate(): computes all words generated by a single mutation on a given word
#A mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string
#seems a bit grandiose and obtuse...

##33_ nearly_equal(): Tests if Two strings a and b are nearly equal when a can be generated by a single mutation on b.
#same as 32..

## 2.7 Dictionaries ##
