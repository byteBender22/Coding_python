n=int(input("Enter the number of terms:"))
a,b = 0,1

#check if number of terms is valid
if n<= 0:
    print("please enter a positive integer.")
elif n ==1:
    print("Fibonacci Series:")
    Print(a)
else:
    print("fibonacci series :")
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
