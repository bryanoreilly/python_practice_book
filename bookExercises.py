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

##Example: Word Count

def wordcount(filename):
    return len(open(filename).read().split())

def linecount(filename):
    return len(open(filename).readlines())

def printLines(filename):
    i = 1
    for line in (open(filename).readlines()):
        print(line.strip('\n') + ' ['+ str(i) +']')
        i = i + 1

def reverseLines(filename):
    lineCount = len(open(filename).readlines())
    lines = open(filename).readlines()
    while(lineCount > 0):
        print(lines[lineCount-1].strip('\n') + ' ['+ str(lineCount) + ']')
        lineCount = lineCount - 1
    

print(wordcount("sheShells.txt"))
print(linecount("sheShells.txt"))
printLines("sheShells.txt")
print()
reverseLines("sheShells.txt")
