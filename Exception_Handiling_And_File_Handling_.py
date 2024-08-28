#To Read the file
"""
f = open("file.txt","r")
content = f.read()
print(content)
f.close()
"""
#To Write the file
"""
f = open("file.txt","w")
f.write("Hey! This is the new line")
f.close()
"""
#To append the text
"""
f = open("file.txt","a")
add_text = f.write("Hey! This is the new line using append")
print(add_text)
f.close()
"""
#To count the charcter using len
"""
f = open("file.txt","r")
content = f.read()
count = len(content)
print(count)
f.close()
"""
#Read line function
"""
f = open("file.txt","r")
content = f.read()
print(f.readline())
f.close()
"""
#Try and Except
"""
a = input("Enter the number 1 : ")
b = input("Enter the number 2 : ")

try:
    c = int(a) + b
    print(c)
except Exception as e:
    print(e)
"""
#Try with Else clause
"""
a = int(input("Enter the number 1: "))

try:
    if a % 2 == 0:
        print( f"{b}is the number is even") # type:  {b} should be {a}
    else:
        print( f"{b}is the number is odd") # type:  {b} should be {a}
except Exception as e:
    print(e)
else:
    print("Else clause got executed")
    """
#Finnaly keyword
"""
a = int(input("Enter your Number "))
b = int(input("Enter the number "))

try:
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
except Exception as e:
    print(e)
else:
print("Else is got executed")
finally:
    print("Finnaly Keyword is used")
"""
