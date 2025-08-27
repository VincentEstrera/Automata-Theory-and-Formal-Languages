#Automata Theory and Formal Languages
#Estrera, Vincent Patrick O.
#Laboratory 1
#1. Provide three(3) examples of accepted and three (3) rejected.

# Simulator for Laboratory 1

class Simulator:
    def __init__(self, states, alphabet, transition, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start = start
        self.accept = accept

    def run(self, s):
        state = self.start
        for ch in s:
            if ch not in self.alphabet:
                return False
            state = self.transition[state][ch]
        return state in self.accept


# Problem 1 Simulator
Simulator1 = Simulator(
    states={'a', 'b', 'f'},
    alphabet={'0', '1'},
    transition={
        'a': {'0': 'a', '1': 'b'},
        'b': {'0': 'f', '1': 'a'},
        'f': {'0': 'f', '1': 'f'}
    },
    start='a',
    accept={'f'}
)

# Problem 2 Simulator
Simulator2 = Simulator(
    states={'q0', 'q1', 'q2', 'q3'},
    alphabet={'a', 'b'},
    transition={
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q3', 'b': 'q0'},
        'q2': {'a': 'q0', 'b': 'q3'},
        'q3': {'a': 'q2', 'b': 'q1'}
    },
    start='q0',
    accept={'q3'}
)

# Testing
print("Problem 1")
for w in ["100", "1011", "0", "11", "1"]:
    print(w, "Accepted" if Simulator1.run(w) else "Rejected")

print("\nProblem 2")
for w in ["aa", "bb", "ab", "a", "b", "aaa"]:
    print(w, "Accepted" if Simulator2.run(w) else "Rejected")
