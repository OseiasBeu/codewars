# Dicionario do codigo morse
MORSE_CODE_DICT = {'A': '.-',   'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..',   'J': '.---','K': '-.-',
                   'L': '.-..', 'M': '--',  'N': '-.',
                   'O': '---',  'P': '.--.','Q': '--.-',
                   'R': '.-.',  'S': '...', 'T': '-',
                   'U': '..-',  'V': '...-','W': '.--',
                   'X': '-..-', 'Y': '-.--','Z': '--..',
                   '1': '.----','2': '..---','3': '...--',
                   '4': '....-','5': '.....','6': '-....',
                   '7': '--...','8': '---..','9': '----.',
                   '0': '-----',',': '--..--','.': '.-.-.-',
                   '?': '..--..','/': '-..-.','-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '|-|'}

CODE_REVERSED = {value:key for key,value in MORSE_CODE_DICT.items()}

def decodeMorse(morse_code):
    morse_code_space_Corr = morse_code.replace('   ',' |-| ')
    morse_code_arr = morse_code_space_Corr.split()
    
    print(morse_code_arr)
    decipher = ''
    for l in morse_code_arr:
        print(l)
        l_decrypt = CODE_REVERSED.get(l)
        decipher += l_decrypt    
    return decipher


def test_and_print(got, expected):
    print('output: {}'.format(got))
    print('expect: {}'.format(expected))
    if got == expected:
        return True
    else:
        print("<pre style='display:inline'>Got {}, expected {}</pre>".format(got, expected))
        return False

test_and_print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
testAndPrint(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')