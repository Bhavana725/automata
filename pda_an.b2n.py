def is_accepted_by_pda(string):
    stack = []
    count_b = 0

    for symbol in string:
        if symbol == 'a':
            stack.append('a')
        elif symbol == 'b':
            count_b += 1
            if stack:
                stack.pop()
            elif count_b > 2 * len(stack):  # Fix the incorrect check
                return False
        else:
            return False  # Reject if the character is not 'a' or 'b'

    return len(stack) == 0 and count_b == 2 * (count_b + len(stack))  # Ensure 2n 'b's

input_string = input("Enter a string: ")

if is_accepted_by_pda(input_string):
    print("String is accepted.")
else:
    print("String is not accepted.")
