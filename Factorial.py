def factorial(n):
  return 1 if n==0 else n*factorial(n-1)
  
num = int(input("Enter the number:"))
print(f"factorial of {num} is {factorial(num)}")
