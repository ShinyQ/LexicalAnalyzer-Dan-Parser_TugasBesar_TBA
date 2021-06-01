def transition_table(transition):
    # string "voiture"
    transition[("q21", "v")] = "q32"
    transition[("q0", "v")] = "q32"
    transition[("q32", "o")] = "q33"
    transition[("q33", "i")] = "q34"
    transition[("q34", "t")] = "q35"
    transition[("q35", "u")] = "q36"
    transition[("q36", "r")] = "q28"
    transition[("q28", "e")] = "q20"

    # string "plante"
    transition[("q21", "p")] = "q22"
    transition[("q0", "p")] = "q22"
    transition[("q22", "l")] = "q25"
    transition[("q25", "a")] = "q26"
    transition[("q26", "n")] = "q27"
    transition[("q27", "t")] = "q28"
    transition[("q28", "e")] = "q20"

    # string "bague"
    transition[("q21", "b")] = "q29"
    transition[("q0", "b")] = "q29"
    transition[("q29", "a")] = "q30"
    transition[("q30", "g")] = "q31"
    transition[("q31", "u")] = "q28"
    transition[("q28", "e")] = "q20"

    return transition

def parse_table(parse):
    parse[('OB', 'moi')] = ['error']
    parse[('OB', 'mère')] = ['error']
    parse[('OB', 'père')] = ['error']
    parse[('OB', 'il')] = ['error']
    parse[('OB', 'conduire')] = ['error']
    parse[('OB', 'affleurer')] = ['error']
    parse[('OB', 'porter')] = ['porter']
    parse[('OB', 'voiture')] = ['voiture']
    parse[('OB', 'plante')] = ['plante']
    parse[('OB', 'bague')] = ['bague']
    parse[('OB', 'EOS')] = ['error']
    
    return parse
