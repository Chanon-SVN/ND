var1 = input("type word for checking palindrome: ")
length = len(var1)
first = 0
last = length - 1
result = True
for i in range (0, int(len(var1)/2)):
    if var1[i] != var1 [length - i - 1]:
        result = False
if result :
    print("It's palindrome")
else :
    print("it's not palindrome")




