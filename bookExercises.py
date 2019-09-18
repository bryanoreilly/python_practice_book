#Exercises from the book python_practice_book
#https://buildmedia.readthedocs.org/media/pdf/python-practice-book/latest/python-practice-book.pdf

#Skipping ahead to test new concepts...
def fxy(f, x, y):
    return f(x) + f(y)

cube = lambda x: x ** 3

print(fxy (cube, 2, 3))
print(fxy(lambda x: x**4 , 2, 3))