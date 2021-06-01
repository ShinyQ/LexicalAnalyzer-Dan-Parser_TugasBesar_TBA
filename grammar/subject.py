def transition_table(transition):
    # string "moi"
    transition[("q21", "m")] = "q2"
    transition[("q0", "m")] = "q2"
    transition[("q2", "o")] = "q3"
    transition[("q3", "i")] = "q20"

    # string "mère"
    transition[("q21", "m")] = "q2"
    transition[("q0", "m")] = "q2"
    transition[("q2", "è")] = "q10"
    transition[("q10", "r")] = "q11"
    transition[("q11", "e")] = "q20"

    # string "père"
    transition[("q21", "p")] = "q4"
    transition[("q0", "p")] = "q4"
    transition[("q4", "è")] = "q10"
    transition[("q10", "r")] = "q11"
    transition[("q11", "e")] = "q20"

    # string "il"
    transition[("q21", "i")] = "q1"
    transition[("q0", "i")] = "q1"
    transition[("q1", "l")] = "q20"


    return transition


def parse_table(parse):
    parse[('SB', 'moi')] = ['moi']
    parse[('SB', 'mère')] = ['mère']
    parse[('SB', 'père')] = ['père']
    parse[('SB', 'il')] = ['il']
    parse[('SB', 'conduire')] = ['error']
    parse[('SB', 'affleurer')] = ['error']
    parse[('SB', 'porter')] = ['error']
    parse[('SB', 'voiture')] = ['error']
    parse[('SB', 'plante')] = ['error']
    parse[('SB', 'bague')] = ['error']
    parse[('SB', 'EOS')] = ['error']

    return parse
