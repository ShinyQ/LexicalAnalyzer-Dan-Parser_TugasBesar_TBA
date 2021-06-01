from collections import defaultdict

import grammar.subject as subject
import grammar.object as object
import grammar.verb as verb

def analyze(input_string):

    # Inisialisasi State [q0, q1 ...]
    state_list = []; list(state_list.append(f'q{i}') for i in range(32))

    # Inisialisasi Seluruh State Menjadi ERROR
    transition_table = defaultdict(lambda: "ERROR", {})

    """
    Context Free Grammar
    S  ::= SB VB OB
    SB ::= (saya) moi | (ibu) mère | (bapak) père | (dia sebagai laki-laki) il
    VB ::= (mengendarai) conduire | (menyiram) affleurer | (memakai) porter
    OB ::= (mobil) voiture | (tanaman) plante | (cincin) bague
    """

    # Initial State (q0)
    transition_table[("q0", " ")] = "q0"

    # Finish state
    transition_table[("q20", "#")] = "ACCEPT"
    transition_table[("q20", " ")] = "q21"

    transition_table[("q21", "#")] = "ACCEPT"
    transition_table[("q21", " ")] = "q21"

    transition_table = subject.transition_table(transition_table)
    transition_table = object.transition_table(transition_table)
    transition_table = verb.transition_table(transition_table)

    # lexical Analysis
    idx_char = 0
    state = "q0"
    current_token = ""

    while state != "ACCEPT":
        current_char = input_string[idx_char]
        current_token += current_char

        print(state, current_char)
        state = transition_table[(state, current_char)]

        if state == "q20":
            print("current token: {} is valid".format(current_token))
            current_token = ""
        if state == "ERROR":
            print("error")
            break

        idx_char += 1

    # Conclusion
    if state == "ACCEPT":
        print("\nsemua token yang di input: {} valid".format(input_string))

    return state == "ACCEPT"
