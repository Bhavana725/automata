def is_accepted_by_pda(string):
    stack = []
    
    for symbol in string:
        if symbol == 'a':
            stack.append('a')
        elif symbol == 'b':
            if stack:
                stack.pop()
            else:
                return False
        else:
            return False

    return len(stack) == 0

input_string = input("Enter a string: ")

if is_accepted_by_pda(input_string):
    print("String is accepted.")
else:
    print("String is not accepted.")
