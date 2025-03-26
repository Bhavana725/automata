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
            if self.state == 'q0':  
                if symbol == '0':
                    self.stack.append('0')
                elif symbol == '1':
                    self.stack.append('1')
                    self.state = 'q1'  
                else:
                    return False  
            elif self.state == 'q1': 
                if symbol == '1':
                    self.stack.append('1')  
                elif symbol == '2'and self.stack[-1] == '1':
                    self.state = 'q2'  
                    self.stack.pop()
                else:
                    return False  
                    
            elif self.state == 'q2':  
                if symbol == '2':
                    if self.stack and self.stack[-1] == '1':  
                        self.stack.pop()
                    else:
                        return False  
                elif symbol == '3' and self.stack[-1] == '0':  
                    self.stack.pop()
                    self.state = 'q3' 
                else:
                    return False
                    
            elif self.state == 'q3':  
                if symbol == '3':
                    if self.stack and self.stack[-1] == '0':  
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
        "011223",
        "011233",   
        "012233",   
        "00112233", 
        "011223",   
        "0001112233", 
        "0123"
    ]

    for test_string in test_strings:
        pda.reset()  
        result = pda.process_input(test_string)
        print(f"Input: {test_string} - {'Accepted' if result else 'Rejected'}")

# Run the test
if __name__ == "__main__":
    test_pda()
