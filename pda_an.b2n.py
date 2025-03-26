class PDA:
    def __init__(self):
        self.stack = []  
        self.state = 'q0' 
        self.i = 0
        
    def reset(self):
        self.stack = []  
        self.state = 'q0'  
        self.i = 0

    def process_input(self, input_string):
        self.stack.append('Z0')  # Initial stack symbol
        
        while self.i < len(input_string):
            symbol = input_string[self.i]
            
            if self.state == 'q0':
                if symbol == 'a':
                    self.stack.append('a')  # Push 'a' for each 'a'
                    self.i += 1
                elif symbol == 'b':
                    # Transition to state q1 when encountering the first b
                    self.state = 'q1'  
                    if self.stack and self.stack[-1] == 'a':  # Pop 'a' for the first 'b'
                        self.stack.pop()
                        self.i += 2
                    else:
                        return False  # Reject if no matching 'a' to pop for 'b'
                else:
                    return False  # Reject if invalid symbol

            elif self.state == 'q1':
                if symbol == 'b':
                    if self.stack and self.stack[-1] == 'a':  # Pop 'a' for the second 'b'
                        self.stack.pop()
                        self.i += 2
                    else:
                        return False  # Reject if no matching 'a' to pop for 'b'
                else:
                    return False  # Reject if invalid symbol

        # At the end, the stack should only contain the initial symbol 'Z0'
        return self.stack == ['Z0']  and len(input_string) == self.i

def test_pda():
    pda = PDA()

    # Test cases
    test_strings = [
        "abb",        # Rejected
        "aaabbb",     # Accepted
        "ab",         # Rejected
        "aaabbbab",   # Rejected
        "aabbbb",     # Rejected
        "abc",        # Rejected
        "aaabbbbbb",  # Rejected
    ]

    for test_string in test_strings:
        pda.reset()  # Reset the PDA before each test
        result = pda.process_input(test_string)
        print(f"Input: {test_string} - {'Accepted' if result else 'Rejected'}")


# Run the test
if __name__ == "__main__":
    test_pda()
