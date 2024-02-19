#Functions
def MenuSystem():
    global menuchoice
    choice = [1,2,3,4]
    print("1) Binary\n2) Any Base\n3) Hex\n4) Quit")
    menuchoice = int(input("\nPlease input your selection: "))
    while menuchoice not in choice:
        menuchoice = int(input("Please input a valid choice: "))

def ArrayToString(my_array):
    array_string = ''.join(map(str, my_array))
    return array_string

def DecimalToBinary(n):
    quotient = n
    binary = []
    while quotient != 0:
        remainder = quotient % 2
        quotient = quotient // 2
        binary.append(remainder)
    binary.reverse()
    binary = ArrayToString(binary)
    return binary

def BinaryToDecimal(n):
    binary = []
    pos = 0
    decimal = 0
    n = str(n)
    for i in n:
        i = int(i)
        binary.append(i)
    for i in range(len(binary)):
        current = binary.pop()
        current = current * (2**pos)
        decimal = decimal + current
        pos += 1
    return decimal

def DecimalToAnyBase(n, base):
    quotient = n
    ans = []
    while quotient != 0:
        remainder = quotient % base
        quotient = quotient // base
        ans.append(remainder)
    ans.reverse()
    ans = ArrayToString(ans)
    return ans

def AnyBaseToDecimal(n, base):
    number = []
    pos = 0
    decimal = 0
    n = str(n)
    for i in n:
        i = int(i)
        number.append(i)
    for i in range(len(number)):
        current = number.pop()
        current = current * (base**pos)
        decimal = decimal + current
        pos += 1
    return decimal

def DecimalToHex(n):
    quotient = n
    Hex = []
    hexvalues = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while quotient != 0:
        remainder = quotient % 16
        quotient = quotient // 16
        if remainder in hexvalues:
            remainder = hexvalues[remainder]
        Hex.append(remainder)
    Hex.reverse()
    Hex = ArrayToString(Hex)
    return Hex

def HexToDecimal(n):
    Hex = []
    pos = 0
    decimal = 0
    hexvalues = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    n = str(n)
    for i in n:
        if i in hexvalues:
            number = hexvalues[i]
            Hex.append(number)
        else:
            i = int(i)
            Hex.append(i)
    for i in range(len(Hex)):
        current = Hex.pop()
        current = current * (16**pos)
        decimal = decimal + current
        pos += 1
    return decimal

#Input and Function calls
quitp = False
MenuSystem()

while quitp == False:
    while menuchoice == 1:
        print("Decimal -> Binary")
        decinput = int(input("Please input your decimal number: "))
        ans = DecimalToBinary(decinput)
        print(ans)

        print("Binary -> Decimal")
        binaryinput = int(input("Please input your binary number: "))
        ans = BinaryToDecimal(binaryinput)
        print(ans)

        goagain = input("Do you want to convert again? (y/n): ")
        if goagain != 'y':
            MenuSystem()

    while menuchoice == 2:
        print("Decimal -> Any Base")
        decinputinput = int(input("Please input your decimal number: "))
        base = int(input("Please input the base to convert to: "))
        ans = DecimalToAnyBase(decinputinput, base)
        print(ans)

        print("Any Base -> Decimal")
        numberinput = input("Please input your number: ")
        base = int(input("Please input the base of this number: "))
        ans = AnyBaseToDecimal(numberinput, base)
        print(ans)

        goagain = input("Do you want to convert again? (y/n): ")
        if goagain != 'y':
            MenuSystem()

    while menuchoice == 3:
        print("Decimal -> Hex")
        decinput = int(input("Please input your decimal number: "))
        ans = DecimalToHex(decinput)
        print(ans)

        print("Hex -> Decimal")
        hexinput = input("Please input your hex number: ")
        ans = HexToDecimal(hexinput)
        print(ans)

        goagain = input("Do you want to convert again? (y/n): ")
        if goagain != 'y':
            MenuSystem()

    if menuchoice == 4:
        quitp = True

print("\nGoodbye!\n")