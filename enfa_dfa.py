def add_epsilon_closure(epsilon_nfa, state, temp):
    # Add epsilon closure for a given state
    if state != '':
        temp.add(state)
        for i in epsilon_nfa.get((state, 'E'), []):
            add_epsilon_closure(epsilon_nfa, i, temp)

def calculate_epsilon_closure(epsilon_nfa, states):
    # Calculate epsilon closures for all states
    epsilon_closures = {}
    for state in states:
        temp = set()
        add_epsilon_closure(epsilon_nfa, state, temp)
        epsilon_closures[state] = temp
    return epsilon_closures

def calculate_transitions(epsilon_nfa, epsilon_closures, alphabet, states):
    # Calculate the transitions for NFA after removing epsilon transitions
    transitions = {}
    for state in states:
        transitions[state] = {}
        for symbol in alphabet:
            reachable_states = set()
            for s in epsilon_closures[state]:
                targets = epsilon_nfa.get((s, symbol), [])
                reachable_states.update(targets)

            closure = set()
            for s in reachable_states:
                if s in epsilon_closures:
                    closure.update(epsilon_closures[s])

            transitions[state][symbol] = closure
    return transitions

def convert_epsilon_nfa_to_nfa(epsilon_nfa, states, alphabet):
    # Convert Epsilon-NFA to NFA
    epsilon_closures = calculate_epsilon_closure(epsilon_nfa, states)
    transitions = calculate_transitions(epsilon_nfa, epsilon_closures, alphabet, states)
    return transitions

def fillStates(dfa, state, input_symbol):
    # Fill states in DFA after conversion
    new_entry = set()
    for i in dfa[state]:
        if (i, input_symbol) in dfa:
            new_entry.update(dfa[(i, input_symbol)])
    return new_entry

def convert_to_tuple_dict(input_dict):
    # Convert dictionary format for NFA/DFA transitions
    result = {}
    for state, transitions in input_dict.items():
        for symbol, targets in transitions.items():
            for target in targets:
                if (state, symbol) in result:
                    result[(state, symbol)].add(target)
                else:
                    result[(state, symbol)] = {target}
    return result

# Main logic

# E-NFA to NFA
epsilon_nfa = {}
n = int(input("Enter number of states in Epsilon-NFA: "))

s = []
states = []

alphabet = ['0', '1']

# Create states and add epsilon transitions
for i in range(n):
    s.append(('q' + str(i), 'E'))  # epsilon transitions
    s.append(('q' + str(i), '0'))  # '0' transitions
    s.append(('q' + str(i), '1'))  # '1' transitions
    states.append('q' + str(i))

# Read transitions from user
for state in s:
    transitions = list(map(str, input(f"Enter transitions for state {state}: ").split(' ')))
    epsilon_nfa[state] = transitions

print("Epsilon-NFA : ", epsilon_nfa)
print("\nTransition Diagram for Epsilon-NFA : ")
for i in epsilon_nfa:
    print(i, " : ", epsilon_nfa[i])

# Convert the Epsilon-NFA to NFA
nfa = convert_epsilon_nfa_to_nfa(epsilon_nfa, states, alphabet)

print("Transition Table for NFA:") 
for state, transitions in nfa.items():
    print(f"State {state}: {transitions}")

nfa = convert_to_tuple_dict(nfa)

# NFA to DFA
dfa = nfa
states = set()

# Generate states for the DFA
for i in dfa.keys():
    states.add(i[0])

new_dfa = {}

# Construct the DFA from the NFA
for i in dfa:
    new_state = ""
    for j in dfa[i]:
        new_state += j
    
    if new_state not in states and new_state != "":
        states.add(new_state)
        new_dfa[(new_state, '0')] = fillStates(dfa, i, '0')
        new_dfa[(new_state, '1')] = fillStates(dfa, i, '1')

# Update the DFA with new states and transitions
for i in new_dfa:
    dfa[i] = new_dfa[i]

print("\nTransition Diagram for DFA : ")

# Print transitions for DFA
for state, transitions in dfa.items():
    if isinstance(transitions, dict):
        for symbol, targets in transitions.items():
            target_string = ''.join(targets)
            print(f"({state[0]}, '{symbol}') : {target_string}")
    else:
        target_string = ''.join(transitions)
        print(f"({state[0]}, '{state[1]}') : {target_string}")
