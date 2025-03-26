def is_accepted_by_pda(string):
    stack1 = []
    stack2 = []
    stage = 1

    for symbol in string:
        if stage == 1:
            if symbol == '0':
                stack1.append('0')
            elif symbol == '1':
                stack2.append('1')
                stage = 2
            else:
                return False

        elif stage == 2:
            if symbol == '1':
                stack2.append('1')
            elif symbol == '2':
                if stack2:
                    stack2.pop()
                else:
                    return False
                stage = 3
            else:
                return False

        elif stage == 3:
            if symbol == '2':
                if stack2:
                    stack2.pop()
                else:
                    return False
            elif symbol == '3':
                if stack1:
                    stack1.pop()
                else:
                    return False
                stage = 4
            else:
                return False

        elif stage == 4:
            if symbol == '3':
                if stack1:
                    stack1.pop()
                else:
                    return False
            else:
                return False

    return len(stack1) == 0 and len(stack2) == 0

input_string = input("Enter a string: ")

if is_accepted_by_pda(input_string):
    print("String is accepted.")
else:
    print("String is not accepted.")
