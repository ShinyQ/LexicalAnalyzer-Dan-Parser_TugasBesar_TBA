import grammar.subject as subject
import grammar.object as object
import grammar.verb as verb

def analyze(sentence):
    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = ['S', 'SB', 'VB', 'OB']
    terminals = [
        'moi', 'mère', 'père', 'il', 'conduire', 'affleurer', 
        'porter', 'voiture', 'plante', 'bague'
    ]

    parse_table = {}
    
    # Non Terminal S
    parse_table[('S', 'moi')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'mère')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'père')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'il')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'conduire')] = ['error']
    parse_table[('S', 'affleurer')] = ['error']
    parse_table[('S', 'porter')] = ['error']
    parse_table[('S', 'voiture')] = ['error']
    parse_table[('S', 'plante')] = ['error']
    parse_table[('S', 'bague')] = ['error']
    parse_table[('S', 'EOS')] = ['error']

    # Non Terminal SB
    parse_table = subject.parse_table(parse_table)

    # Non Terminal VB
    parse_table = verb.parse_table(parse_table)

    # Non Terminal OB
    parse_table = object.parse_table(parse_table)

    stack = []
    stack.append('#')
    stack.append('S')

    token = 0
    symbol = tokens[token]

    while(len(stack) > 0):
        top = stack[len(stack)-1]

        print(f'Top    = {top}')
        print(f'Symbol = {symbol}')

        if top in terminals:
            if top == symbol:
                stack.pop()
                token += 1
                symbol = tokens[token]

                if symbol == 'EOS':
                    print('Isi Stack :', stack)
                    stack.pop() 
            else:
                print('error')
                break
        elif top in non_terminals:
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                push = parse_table[(top, symbol)]

                for i in range(len(push)-1, -1, -1):
                    stack.append(push[i])
            else:
                print('error')
                break
        else:
            print('error')
            break

        print(f'Isi Stack : {stack} \n')        
    
    if symbol == 'EOS' and len(stack) == 0:
        print(f'Input string {sentence}, diterima sesuai Grammar')
    else:
        print(f'Input string {sentence}, tidak diterima, tidak sesuai Grammar')
