n=0
total=0
for i in range(0,5):
    n=int(input("enter the marks:"))
    total=total+n
mean=total/5
print("PERCENTAGE:",mean)
if(mean<35):
      print("FAIL")
else:
      print("PASS")
