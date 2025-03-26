class PDA:
    def __init__(self):
        self.stack = []  
        self.state = 'q0' 

    def reset(self):
        self.stack = []
        self.state = 'q0'

    def process_input(self, input_string):
        self.stack.append('Z0')
        
        for symbol in input_string:
            if self.state == 'q0':
                if symbol == 'a':
                    self.stack.append('A')
                elif symbol == 'b':
                    if self.stack and self.stack[-1] == 'A':
                        self.stack.pop()  
                        self.state = 'q1'
                    else:
                        return False  
                else:
                    return False  

            elif self.state == 'q1':
                if symbol == 'b':
                    if self.stack and self.stack[-1] == 'A':
                        self.stack.pop()  
                    else:
                        return False  
                else:
                    return False  
        if self.stack == ['Z0']:
            return True
        else:
            return False

def test_pda():
    pda = PDA()

    # Test cases
    test_strings = [
        "aabb",      
        "aaabbb",    
        "ab",        
        "aaabbbab",  
        "aab",       
        "abc",
        "abab"
    ]

    for test_string in test_strings:
        pda.reset()  # Reset the PDA before each test
        result = pda.process_input(test_string)
        print(f"Input: {test_string} - {'Accepted' if result else 'Rejected'}")


# Run the test
if __name__ == "__main__":
    test_pda()
