dict = {
    'A' : '.-' , 'B' : '-...' , 'C' : '-.-.' , 'D' : '-..' , 'E' : '.' , 'F' : '..-.' , 'G' : '--.' , 'H' : '....' ,
    'I' : '..' , 'J' : '.---' , 'K' : '-.-' , 'L' : '.-..' , 'M' : '--' , 'N' : '-.' , 'O' : '---' , 'P' : '.--.' ,
    'Q' : '--.-' , 'R' : '.-.' , 'S' : '...' , 'T' : '-' , 'U' : '..-' , 'V' : '...-' , 'W' : '.--' , 'X' : '-..-' ,
    'Y' : '-.--' , 'Z' : '--..' ,
    '0' : '-----' , '1' : '.----' , '2' : '..---' , '3' : '...--' , '4' : '....-' , '5' : '.....' , '6' : '-....' ,
    '7' : '--...' , '8' : '---..' , '9' : '----.' ,
    '.' : '.-.-.-' , ',' : '--..--' , '?' : '..--..' , "'" : '.----.' , '!' : '-.-.--' , '/' : '-..-.' ,
    '(' : '-.--.' , ')' : '-.--.-' , '&' : '.-...' , ':' : '---...' , ';' : '-.-.-.' , '=' : '-...-' ,
    '+' : '.-.-.' , '-' : '-....-' , '_' : '..--.-' , '"' : '.-..-.' , '$' : '...-..-' , '@' : '.--.-.' ,
    '¿' : '..-.-' , '¡' : '--...-' ,
}


# -------------  To get key from Dictionary --------------------#


def return_key(val):
    for key , value in dict.items():
        if val == value:
            return key


def text_to_morse(text):
    morse_code = ''
    text1 = " ".join(text.split())
    text1 = text1.split(" ")
    for char in text1:
        if text1.index(char) >= 1:
            morse_code += '/'
        for i in char:
            try :
                morse_code += dict[i] + ' '
            except KeyError :
                morse_code = "Please provide valid input"
    return morse_code


def morse_to_text(input_text):
    text_list = input_text.split("/")
    text = ''
    for text_in_list in text_list:
        code = text_in_list.split(" ")
        if text_list.index(text_in_list) > 0:
            text += " "
        for i in code :
            value = i.strip()
            if len(value) > 0:
                key = return_key(value)
                if key is not None:
                    text += key
                else:
                    text = "Please provide valid input"
                    break
    sngl_whtspce = ' '.join(text.split())
    return sngl_whtspce


def check(input_text):
    text = input_text.replace(" ", "")
    if text[0] == '/':
        return True
    text = text.replace("/", "")
    condition = True
    a = ['.', '-']
    for i in text:
        if i in a:
            condition = False
        else:
            condition = True
    return condition

input_string = input("Enter text or Morse code: ").upper()

if check(input_string):
    print(f"Morse code: {text_to_morse(input_string)}")
else:
    print(f"Text: {morse_to_text(input_string)}")
