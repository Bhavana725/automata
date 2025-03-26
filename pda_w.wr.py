def is_accepted_by_pda(string):
    stack = []
    length = len(string)

    if length % 2 != 0:
        return False  

    mid = length // 2

    for i in range(mid):
        stack.append(string[i])

    for i in range(mid, length):
        if not stack or stack.pop() != string[i]:
            return False  

    return len(stack) == 0

input_string = input("Enter a string: ")

if is_accepted_by_pda(input_string):
    print("String is accepted.")
else:
    print("String is not accepted.")
