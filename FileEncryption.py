codes = {'A' : '%',
         'a' : '9',
         'B' : '@',
         'b' : '%+',
         'C' : '^',
         'c' : '$',
         'D' : '#',
         'd' : '&',
         'E' : '*',
         'e' : '(',
         'F' : ')',
         'f' : '_',
         'G' : '-',
         'g' : '6',
         'H' : '+',
         'h' : '1',
         'I' : '=',
         'i' : '`',
         'J' : '~',
         'j' : '!',
         'K' : '2',
         'k' : '3',
         'L' : '4',
         'l' : '5',
         'M' : '7',
         'm' : '8',
         'N' : '99',
         'n' : '[',
         'O' : ']',
         'o' : '{',
         'P' : '}',
         'p' : '--',
         'Q' : '|',
         'q' : ':',
         'R' : ';',
         'r' : '"',
         'S' : '<',
         's' : '>',
         'T' : ',',
         't' : '.',
         'U' : '?',
         'u' : '/',
         'V' : '~~',
         'v' : '&*',
         'W' : 'r',
         'w' : 'O',
         'X' : 'I',
         'x' : '7!',
         'Y' : '9x',
         'y' : 'oa',
         'Z' : 'l',
         'z' : '**',}

encrypt = open('encrypted.txt', 'w')

with open('info_security.txt', 'r') as file:
    file1 = file.read()

with open('encrypted.txt', 'w') as encrypt:
    for char in file1:
        if char in codes:
            encrypt.write(codes[char])
        else:
            encrypt.write(char)

