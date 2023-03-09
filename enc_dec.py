# Suhas Salapaka
def encode(password):
    res = [int(x) for x in str(password)]
    enc = ""
    for char in res:
        table = {0: '3', 1: '4', 2: '5', 3: '6',
                 4: '7', 5: '8', 6: '9', 7: '0',
                 8: '1', 9: '2'}
        enc += table[char]
    return enc


def decode(enc):
    i = [int(y) for y in str(enc)]
    password = ''
    for num in i:
        table = {3: '0', 4: '1', 5: '2', 6: '3',
                 7: '4', 8: '5', 9: '6', 0: '7',
                 1: '8', 2: '9'}
        password += table[num]
    return password


def menu():
    print('''Menu  
    ------------- 
    1. Encode  
    2. Decode  
    3. Quit ''')
    option = int(input("Please enter an option: "))
    return option


def main():
    option = menu()
    password = "None"
    enc = ''
    while option != 3:
        if option == 1:
            print("Please enter your password to encode: ", end='')
            password = input()
            enc = encode(password)
            print("Your password has been encoded and stored!")
            option = menu()
        elif option == 2:
            decoded_password = decode(enc)
            print("The encoded password is", encode(password), "and the original password is", decoded_password)
            option = menu()


if __name__ == "__main__":
    main()
