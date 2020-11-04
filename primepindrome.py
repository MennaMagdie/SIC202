def show_menu():
    operation = int(input("CHOOSE AN OPERTION\n(1)Palindrome   (2)Prime   (3)Exit"))
    return operation

def is_prime(number):
    if number == 2 :
        print("It's a prime number")
    elif number > 1:
        for i in range(2,number):
            if number % i == 0:
               print("It's not a prime number")
               break
            else:
               print("It's a prime number")
               break
    else:
        print("It's not a prime number")

def is_palindrome():
    word = input("Enter the word/number you want to check")
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

operation=0
while operation!=3:
    print("")
    operation = show_menu()
    if operation == 3:
        break
    elif operation == 1:
        is_palindrome()
    elif operation == 2:
        n = int(input("Enter the number you want to check"))
        is_prime(n)
    else:
        print("INVALID :)")

