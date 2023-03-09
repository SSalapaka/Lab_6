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


def main():
    print('''Menu  
------------- 
1. Encode  
2. Decode  
3. Quit ''')
    option = int(input("Please enter an option: "))

    password = "None"
    if option == 1:
        password = input("Please enter your password to encode: ")
        enc = encode(password)
        print("Your password has been encoded and stored!")


if __name__ == "__main__":
    main()
