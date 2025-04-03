#conditional statements
light = input("light color : ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#grades of students
marks = int(input("marks : "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D") 

#Question: print output for: A=5 & G=M
A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2 ) and G == "M" ):
    print("fees is 200") 
elif(A == 3 or A == 4 or G == "F"):
    print("fees is 200")
elif(A == 5 and G == "M"):
    print("fees is 300")
else:
    print("no fees") 

#If A = 2 and G = F
A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2 ) and G == "M" ):
    print("fees is 200") 
elif(A == 3 or A == 4 or G == "F"):
    print("fees is 200")
elif(A == 5 and G == "M"):
    print("fees is 300")
else:
    print("no fees") 





