def transition_table(transition):
    # string "voiture"
    transition[("q21", "v")] = "q31"
    transition[("q0", "v")] = "q31"
    transition[("q31", "o")] = "q32"
    transition[("q32", "i")] = "q33"
    transition[("q33", "t")] = "q34"
    transition[("q34", "u")] = "q35"
    transition[("q35", "r")] = "q27"
    transition[("q27", "e")] = "q20"

    # string "plante"
    transition[("q21", "p")] = "q4"
    transition[("q0", "p")] = "q4"
    transition[("q4", "l")] = "q24"
    transition[("q24", "a")] = "q25"
    transition[("q25", "n")] = "q26"
    transition[("q26", "t")] = "q11"
    transition[("q11", "e")] = "q20"

    # string "bague"
    transition[("q21", "b")] = "q28"
    transition[("q0", "b")] = "q28"
    transition[("q28", "a")] = "q29"
    transition[("q29", "g")] = "q30"
    transition[("q30", "u")] = "q27"
    transition[("q27", "e")] = "q20"


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
