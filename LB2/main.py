# def fib(num):
#     if num==0 or num==1 or num==2:
#         return 1
#     else:
#         return fib(num - 1) + fib(num - 2)

# print(fib(20))

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("FizzBuzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)

fizz_buzz(7)