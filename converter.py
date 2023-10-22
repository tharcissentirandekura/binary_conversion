#make a program that takes a number and turn it into binary representation

def num_to_binary(num,mode):

    remainder = []

    while num >= mode:
        update_num = num % mode
        num = num // mode

        # print(update_number,":",number)
        remainder.append(update_num)

        if num < mode:

            remainder.append(num)

    remainder.reverse()
    return remainder

def binary_to_dec(binary):

    count = len(str(binary))
    update_bin = []
    while count >0:

        for i in str(binary):
            count -= 1
            update_bin.append(2**count*int(i))
        break

    total = 0

    for i in update_bin:
        total = total + i
    print("The decimal representation of:",binary,"is:",total)

print("Welocme to the binary and decimal conversion\n\n")
print("1.Binary to decimal\n2.Decimal to binary\n")
choice = int(input("Choose what to do:"))


if choice == 1:
    binary_num = int(input("Enter the binary number:"))
    function = binary_to_dec(binary_num)
    if function:
        for i in function:
            print(i)

elif choice == 2:
    number = int(input("Enter the number:"))
    print("Enter the mode(binary(2),octal(8),hexadecimal(16)")
    mode_base = int(input("Enter the mode of convertion:"))

    function = num_to_binary(number,mode_base)
    print("The representation of ",number,"in",mode_base,"is:")

    if function:
        for i in function:
            print(i,end=" ")
        print("\n")

    message = input("Message:")
    char_list = []
    bin_char_list = []
    output_list = []
    for j in message:
        a = ord(j)
        char_list.append(a)
    for i in char_list:
        dec = num_to_binary(i,mode_base)
        if dec:
            # print(dec,end="")
            bin_char_list.append(dec)

    total = 0
    for i in bin_char_list:
        print()
        for j in i:

            print(j,end =" ")
            output_list.append(j)

    print("This is the output:",output_list)
