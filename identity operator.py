X=5
if(type(X)is int):
    print("true")
else:
    print("false")
X=5.0
if(type(X)is not float):
    print("true")
else:
    print("false") 
X=20
Y=20
if(X is Y):

    print("X&Y SAME identity")
Y=30
if(X is not Y): 
    print("X&Y DIFFERENT identity")              