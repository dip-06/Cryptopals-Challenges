import string

def from_text(text):
    #convert the text into raw binary
    binary=[]
    for char in text:
        decimal = ord(char)
        clean_binary = f"{decimal:08b}"
        binary.append(clean_binary)
        
    #Combine all binary numbers into one single string
    large_binary_string = "".join(str(num) for num in binary)
    convert(large_binary_string)

def from_hex(hex_string):
    decimal = (int(hex_string,16))
    large_binary_string = "0"+f"{decimal:08b}"
    convert(large_binary_string)

def convert(large_binary_string):
    #Create alphabetlist
    base64_alphabets = [strings for strings in string.ascii_uppercase]+[strings for strings in string.ascii_lowercase]+[numbers for numbers in string.digits]+['+','/']

    #Add extra 0s
    if (len(large_binary_string)%6 != 0):
        extra = len(large_binary_string)%6
        large_binary_string = large_binary_string + (6-extra)*'0'
    
    #Now break that giant string into pieces of 6
    six_together = [large_binary_string[i:i+6] for i in range(0,len(large_binary_string),6)]
    
    #Convert the binary into Decimal

    final_decimal = [int(num,2) for num in six_together]

    while (len(final_decimal)%4 != 0):
        final_decimal.append(404)

    #Create encoded text
    encoded_text=[]
    for last_dec in final_decimal:
        if last_dec != 404:
            encoded_text.append(base64_alphabets[last_dec])
        else:
            encoded_text.append('=')
    encoded_text="".join(encoded_text)
    print(f"Encoded: {encoded_text}")

print("---------------Base64 Encoder---------------\nChoose Converter :\n1)Text to base64.\n2)Hexadecimal to base64.\n")
choice = int(input("Your Choice(1/2): "))

match choice:
    case 1:
        plaintext = input("\nEnter text: ")
        from_text(plaintext)
    case 2:
        plaintext = input("\nEnter text: ")
        from_hex(plaintext)
