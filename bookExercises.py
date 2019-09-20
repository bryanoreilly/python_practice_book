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
x = [0, 1, [2]]
x[2][0] = 3
#print(x[2][0])
x[2].append(4)
#print(x)

#for i in range(10):
#    print (i, i*i, i*i*i)

