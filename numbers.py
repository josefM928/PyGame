# EVEN function: is_even

def is_even(n):

    return n % 2 == 0


# ODD function: is_odd

def is_odd(n):

    return n % 2 == 1


# PRIME function: is_prime

def is_prime(n):

    # check for every number from 1 to n/2

    for i in range(2, n//2):

        # if factor found

        if n % i == 0:

            return False

    return True


# function to find sum of devisors

def sum_of_devisors(n):

    total = 0

    i = 1

    while n > 0:

        if n % i == 0:

            total += i

            n = n/i

        i += 1


# PERFECT function: is_perfect

def is_perfect(num):

    # find sum of devisors

    total = sum_of_devisors(num)

    if num == total:

        return True

    return False


# ABUNDANT function: is_abundant

def is_abundant(n):

    if sum_of_devisors(n) > n:

        return True

    return False


# function to display menu

def menu():

    print("\nMain Menu\n")

    print("1 - Find all prime numbers within a given range")

    print("2 - Find all perfect numbers within a given range")

    print("3 - Find all abundant numbers within a given range")

    print("4 - Chart all even, odd, prime, perfect and abundant numbers within a given range")

    print("5 - Quit")

    choice = int(input("\nYour choice: "))

    # till user enters valid choice

    if choice > 5 or choice < 1:

        print("Invalid, try again")

        return menu()

    return choice


# function to read 2 numbers

def get():

    start = int(input("Enter starting number (positive only): "))

    # read till +ve number

    while start<0:

        print("Invalid, try again")

        start=int(input("Enter starting number (positive only): "))

    end=int(input("Enter ending number: "))

    while end<start:

        print("Invalid, try again")

        end = int(input("Enter ending number: "))

    return (start, end)


# main

def main():

    choice = menu()

    while choice != 5:

        # read 2 numbers

        a, b = get()

        if choice == 1:

            print(f"\nAll prime numbers between {a} and {b}")

            print("#"*20)

            for i in range(a, b+1):

                if is_prime(i):

                    print(i)

            print("#"*20)

        elif choice == 2:

            print(f"\nAll perfect numbers between {a} and {b}")

            print("#"*20)

            for i in range(a, b+1):

                if is_perfect(i):

                    print(i)

            print("#"*20)

        elif choice == 3:

            print(f"\nAll abundant numbers between {a} and {b}")

            print("#"*20)

            for i in range(a, b+1):

                if is_abundant(i):

                    print(i)

            print("#"*20)

        elif choice == 4:

            print(f"\nAll prime numbers between {a} and {b}")

            print("#"*20)

            for i in range(a, b+1):

                if is_prime(i):

                    print(i)

            print("#"*20)

            print(f"\nAll perfect numbers between {a} and {b}")

            print("#"*20)

            for i in range(a, b+1):

                if is_perfect(i):

                    print(i)

            print("#"*20)

            print(f"\nAll abundant numbers between {a} and {b}")

            print("#"*20)

            for i in range(a, b+1):

                if is_abundant(i):

                    print(i)

            print("#"*20)

        choice = menu()

main()