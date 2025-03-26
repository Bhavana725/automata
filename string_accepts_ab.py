def is_accepted(input_string):
    current_state = 'Q0'

    for symbol in input_string:
        if current_state == 'Q0':
            if symbol == 'a':
                current_state = 'Q1'
            else:
                current_state = 'Q0'
        elif current_state == 'Q1':
            if symbol == 'a':
                current_state = 'Q1'
            else:
                current_state = 'Q2'
        elif current_state == 'Q2':
            if symbol == 'b':
                current_state = 'Q2'
            else:
                current_state = 'Q2'

    return current_state == 'Q2'


def main():
    input_string = input("Enter a string: ")

    if is_accepted(input_string):
        print("String is accepted.")
    else:
        print("String is not accepted.")


if __name__ == "__main__":
    main()
