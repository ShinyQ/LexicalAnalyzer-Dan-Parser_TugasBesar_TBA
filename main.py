import lexical, gr_parser

print("""\
-----------------------------------------------------------------------
                    Lexical Analyzer Dan Parser                       |
-----------------------------------------------------------------------
  Oleh Kelompok 1 IF-43-09: Hanvito Michael Lee   (1301190090)        |  
                            Kurniadi Ahmad Wijaya (1301194024)        |
                            Naufal Haritsah Lutfi (1301194073)        |  
                                                                      |
  Grammar (Perancis):                                                 |      
  -----------------------------------                                 | 
  | subject |   verb    |  object   |                                 |         
  -----------------------------------                                 |           
  |   moi   | conduire  | voiture   |                                 |   
  |   mère  | affleurer | plante    |                                 | 
  |   père  | porter    | bague     |                                 |           
  |   il    |           |           |                                 |   
  -----------------------------------                                 |   
                                                                      |   
  Format Masukkan : <subject> <verb> <object>                         |   
  Contoh Masukkan : moi conduire plante                               |           
-----------------------------------------------------------------------
""")

kalimat = input("Masukkan Kalimat / Kata Yang Ingin Diperiksa: ")

print("""\
----------------------------------
    Proses Lexical Analyzer
----------------------------------""")
is_valid = lexical.analyze(kalimat)

print("""\
----------------------------------
          Proses Parser
----------------------------------""")
if is_valid:
   gr_parser.analyze(kalimat)
else :
   print(f'Input string {kalimat}, tidak diterima, tidak ada pada Grammar')
