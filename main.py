### This program is written with recursive and none recursive functions for university purpose.
def combination_recursive(n, r):
    if n == r or r == 0:
        return 1
    return combination_recursive(n - 1, r) + combination_recursive(n - 1, r - 1)

def factorial_recursive(number):
    if number <= 1:
        return 1
    return number * factorial_recursive(number - 1)

def factorial(number):
    fact = 1
    numb = number + 1
    for item in range(1,numb):
        fact *= item
    return fact

def combination(n, r):
    number = factorial(n)
    rcombinations = factorial(r)
    difference = factorial(n - r)
    result = number / (rcombinations * difference)
    return result

def main():
    print("___Welcome to factorial and combination program___")
    print("Pick one of the available options : ")
    print(R"""
        1. Recursive Factorial
        2. Factorial
        3. Recursive Combination
        4. Combination
    """)

    answer = int(input(" your choice : "))
    if answer == 1:
        number = int(input("Please enter a number : "))
        result = factorial_recursive(number=number)
        print(result)

    elif answer == 2:
        number = int(input("Please enter a number : "))
        result = factorial(number=number)
        print(result)

    elif answer == 3:
        first_number = int(input("Please enter a Number : "))
        second_number = int(input("Please eneter k-combination : "))
        result = combination_recursive(n=first_number, r=second_number)
        print(result)

    elif answer == 4:
        first_number = int(input("Please enter a Number : "))
        second_number = int(input("Please eneter k-combination : "))
        result = combination(n=first_number, r=second_number)
        print(result)
    else:
        print('___Wrong Input!___')

if __name__ == "__main__":
    main()