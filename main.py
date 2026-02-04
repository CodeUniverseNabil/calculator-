while True:
    try:
        while True:
            num1 = float(input("Input the value of num1 => "))
            num2 = float(input("Input the value of num2 => "))
            lis = [num1, num2]

            if len(lis) == 2:
                sign = input("Input the sign (+, -, *, /) => ")

                if sign == "+":
                    ans = num1 + num2
                elif sign == "-":
                    ans = num1 - num2
                elif sign == "*":
                    ans = num1 * num2
                elif sign == "/":
                    ans = num1 / num2
                else:
                    print("Sign not recognized")
                    break

            while True:
                more_command = input("Input only sign (+, -, *, /) or '=' to show result => ")

                if more_command == "=":
                    print(f"The answer is: {ans}")
                    break
                else:
                    add_more = float(input("Input the value to operate => "))
                    if more_command == "+":
                        ans += add_more
                    elif more_command == "-":
                        ans -= add_more
                    elif more_command == "*":
                        ans *= add_more
                    elif more_command == "/":
                        ans /= add_more
                    else:
                        print("Something is wrong")
    except:
        print("Program crashed")
