print("enter marks obtained in 5 tests")
one=int(input())
two=int(input())
three=int(input())
four=int(input())
five=int(input())
total=one+two+three+four+five
avg=total/5
if avg>=91 and avg<100:
    print("your grade is A1")
elif avg>=81 and avg<91:
    print("your grade is A2")   
elif avg>=71 and avg<81:
    print("your grade is A3") 
else:
    print("invalid input") 
            