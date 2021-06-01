import lexical
import gr_parser

words = [
    'moi', 'mère', 'père', 'il', 'conduire', 'affleurer',
    'porter', 'voiture', 'plante', 'bague'
]

for word in words:
    lexical.analyze(word)

subject = ['moi', 'mère', 'père', 'il']
verb = ['conduire', 'affleurer', 'porter']
object = ['voiture', 'plante', 'bague']

for x in subject:
    for y in verb: 
        for z in object:
            gr_parser.analyze(f'{x} {y} {z}')
