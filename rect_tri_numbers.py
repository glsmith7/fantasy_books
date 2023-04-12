# rect_tri_numbers.py
"""

Calcs for book of Revelation numerology/gematria

1) Calculates rectangular numbers (n)(n+1) and 
2) triangular numbers (n)(n+1)/2

3) Sums even numbers
4) Squares numbers

"""

def rect_num (n):
    return n*(n+1)

def tri_num (n):
    return (int(rect_num(n)/2))

def print_rect(n):
    for i in range (n):
        print (str(i) + " --> " + str(rect_num(i)))

def print_tri(n):
    for i in range (n):
        print (str(i) + " --> " + str(tri_num(i)))

def sum_evens(n):
    x=0
    total=0
    while n >= x:
        total=total+x
        x=x+2
    return (total)

def square(x):
    return x**2

def print_evens(n):
    x=0
    while n >= x:
        print (str(x) + " --> " + str(sum_evens(x)))
        x=x+2
        
def print_squares(n):
    x=0
    while n>=x:
        print (str(x) + " --> " + str(square(x)))
        x=x+1


####################### Main ################################

# print_rect(52) 
# print_tri(52)
#print_evens(100)
# print_squares(100)
