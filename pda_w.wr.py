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
        self.stack.append('Z0')
        
        for symbol in input_string:
            l = len(input_string)
                
            if self.state == 'q0':
                if symbol == 'a' or symbol == 'b':
                    self.stack.append(symbol)
                else:
                    return False  
            elif self.state == 'q1':
                if self.stack and self.stack[-1] == symbol:
                    self.stack.pop()
                else:
                    return False 
            self.i += 1
            if self.i >= l/2:
                self.state = 'q1'    

        if self.stack == ['Z0']:
            return True
        else:
            return False

def test_pda():
    pda = PDA()

    # Test cases
    test_strings = [
        "abba",    # Accepted
        "aabb",      # Rejected
        "abab",      # Rejected
        "aaabbaaa",  # Rejected
        "ab",        # Accepted
        "aaaabbbb",  # Rejected
    ]

    for test_string in test_strings:
        pda.reset()  
        result = pda.process_input(test_string)
        print(f"Input: {test_string} - {'Accepted' if result else 'Rejected'}")

# Run the test
if __name__ == "__main__":
    test_pda()
