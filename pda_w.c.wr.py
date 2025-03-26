def is_accepted_by_pda(string):
    stack = []
    found_C = False
    index = 0

    while index < len(string):
        char = string[index]

        if not found_C:
            if char == 'C':
                found_C = True
            else:
                stack.append(char)
        else:
            if not stack or stack.pop() != char:
                return False

        index += 1

    return len(stack) == 0 and found_C

input_string = input("Enter a string: ")

if is_accepted_by_pda(input_string):
    print("String is accepted.")
else:
    print("String is not accepted.")
