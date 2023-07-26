number = input("정수를 입력하세요: ")
base = int(input("변환할 진수를 입력하세요: "))

if base == 16 or base == 10 or base == 8 or base == 2:
    dap = int(number, base)
    print("To Dec: ", dap)
    print("To Hex: ", hex(dap))
    print("To Oct: ", oct(dap))
    print("To Bin: ", bin(dap))
else:
    print("not supported")