# 1.find square matrix or not
def square_matrix(a):
    for i in a:
        for j in i:
          if len(a) == len(a[j]):
            return "square"
          else:
            return "not square"

a =[
[1,3],
[4,7]
]
print(square_matrix(a))

# 2. Take two dimensional array (square matrix) print diagnol values in list
def diagonal_matrix(a):
    b=()
    for i in a:
         if len(a) != len(i):
             return "not square"
    for i in range(len(a)):
        b+=(a[i][i],)
    return b
        

a =[
[1,3,4],
[4,7,6],
[3,5,8]
]
print(diagonal_matrix(a))


# 3. Print anti diagonal values inist 

def anti_diagonal_matrix(a):
    c=len(a)
    b=()
    for i in a:
         if c != len(i):
             return "not square"
    for i in range(c):
        b+=(a[i][c-1-i],)
    return b
        

a =[
[1,3,4],
[4,7,6],
[3,5,8]
]
print(anti_diagonal_matrix(a))
