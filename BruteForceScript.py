from string import digits
from string import ascii_letters

def pin():
    for i in digits:
        for j in digits:
            for k in digits:
                for l in digits:
                    print(i, j, k, l)

def ascii_combinations():
    for i in ascii_letters:
        for j in ascii_letters:
            for k in ascii_letters:
                for l in ascii_letters:
                    print(i, j, k, l)

if __name__ == "__main__":
    print("How would you like to Brute Force?\n1)Digits Only\n2)Using Ascii")

    choice = input("")

    if choice == "1":
        pin()
    elif choice == "2":
        ascii_combinations()
    else:
        print("Invalid options chosen :(")