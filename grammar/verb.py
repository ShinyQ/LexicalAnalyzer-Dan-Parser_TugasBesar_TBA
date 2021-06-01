def transition_table(transition):
    # string "conduire"
    transition[("q21", "c")] = "q5"
    transition[("q0", "c")] = "q5"
    transition[("q5", "o")] = "q6"
    transition[("q6", "n")] = "q7"
    transition[("q7", "d")] = "q8"
    transition[("q8", "u")] = "q9"
    transition[("q9", "i")] = "q10"
    transition[("q10", "r")] = "q11"
    transition[("q11", "e")] = "q20"

    # string "affleurer"
    transition[("q21", "a")] = "q12"
    transition[("q0", "a")] = "q12"
    transition[("q12", "f")] = "q13"
    transition[("q13", "f")] = "q14"
    transition[("q14", "l")] = "q15"
    transition[("q15", "e")] = "q16"
    transition[("q16", "u")] = "q17"
    transition[("q17", "r")] = "q18"
    transition[("q18", "e")] = "q19"
    transition[("q19", "r")] = "q20"

    # string "porter"
    transition[("q21", "p")] = "q22"
    transition[("q0", "p")] = "q22"
    transition[("q22", "o")] = "q23"
    transition[("q23", "r")] = "q24"
    transition[("q24", "t")] = "q18"
    transition[("q18", "e")] = "q19"
    transition[("q19", "r")] = "q20"

    return transition


def parse_table(parse):
    parse[('VB', 'moi')] = ['error']
    parse[('VB', 'mère')] = ['error']
    parse[('VB', 'père')] = ['error']
    parse[('VB', 'il')] = ['error']
    parse[('VB', 'conduire')] = ['conduire']
    parse[('VB', 'affleurer')] = ['affleurer']
    parse[('VB', 'porter')] = ['porter']
    parse[('VB', 'voiture')] = ['error']
    parse[('VB', 'plante')] = ['error']
    parse[('VB', 'bague')] = ['error']
    parse[('VB', 'EOS')] = ['error']
    
    return parse
