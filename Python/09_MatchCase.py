a = int(input("Enter a num bw 1 to 10: \n"))

match a:
    case 1:
        print("hey you won a")
    case 2:
        print("hey you won b")
    case 3:
        print("hey you won c")
    case _:
        print("better luck next time")