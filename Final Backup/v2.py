#Caliope 13
Zähler = 0
Bestätigen =0
Senden = False
wort = [" "]
vorübergehend = ""
l=0
alphabet = [
  " ",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'," ",
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
  'w', 'x', 'y', 'z',
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
  ':', '!', '"', '#', '$', '%', '&', '\'', '(', ')',
   '+', ',', '.', '/',':', ';', '<', '=','?', '@', 
   '[', '\\', ']', '^', '_', '`',  '{', '|', '}', '~'
]; 

def event_a():
        
    global Zähler
    Zähler += 1

    basic.show_string(alphabet[Zähler])
    basic.show_string(" ")
input.on_button_event(Button.A, input.button_event_click(), event_a)
def event_b():
   
    global Bestätigen
    Bestätigen = Bestätigen + 1
    
    
input.on_button_event(Button.B, input.button_event_click(), event_b)

def on_gesture_shake():
    global Senden
    Senden = True
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

speed = 0.5*1000  #angabe in sekunden


def on_forever():
    global Zähler
    global Bestätigen
    global l
    global Senden
    global wort
    global vorübergehend


    
    
    
    
    if Senden == False:
        z0()
    if Bestätigen==1:
        gesuchter_buchstabe = alphabet[Zähler]
        wort[l]=gesuchter_buchstabe
        l = l+ 1
        Bestätigen= Bestätigen + 1
       

    if Bestätigen==2:
        for i in range(len(wort)):
            vorübergehend += wort[i]
        
        
        basic.show_string(vorübergehend)
        vorübergehend=""
        
        Zähler = 0
        Bestätigen=0
        
        
        
    
    
    
   
        
        

    

    
 

    
    if Senden == True :
        
        connection()
        basic.show_string(vorübergehend)
        vorübergehend=""


        for i in range(len(wort)):
            
            if wort[i] == "!":
                z0()
                z1()
                z0()
                z0()
                z0()
                z0()
                z1()

            elif wort[i] == '"':
                z0()
                z1()
                z0()
                z0()
                z1()
                z0()
                z0()
                
            elif wort[i] == ' ':
                z0()
                z0()
                z0()
                z1()
                z1()
                z1()
                z1()

            elif wort[i] == '#':
                z0()
                z1()
                z0()
                z0()
                z1()
                z0()
                z1()

            elif wort[i] == '$':
                z0()
                z1()
                z0()
                z0()
                z1()
                z0()
                z0()

            elif wort[i] == '%':
                z0()
                z1()
                z0()
                z0()
                z1()
                z0()
                z1()

            elif wort[i] == '&':
                z0()
                z1()
                z0()
                z0()
                z1()
                z1()
                z0()

            elif wort[i] == '\'':
                z0()
                z1()
                z0()
                z0()
                z1()
                z1()
                z1()

            elif wort[i] == '(':
                z0()
                z1()
                z0()
                z1()
                z0()
                z0()
                z0()

            elif wort[i] == ')':
                z0()
                z1()
                z0()
                z1()
                z0()
                z0()
                z1()

            elif wort[i] == '+':
                z0()
                z1()
                z0()
                z1()
                z0()
                z1()
                z1()

            elif wort[i] == ',':
                z0()
                z1()
                z0()
                z1()
                z1()
                z0()
                z0()

            elif wort[i] == '.':
                z0()
                z1()
                z0()
                z1()
                z1()
                z1()
                z0()

            elif wort[i] == '/':
                z0()
                z1()
                z0()
                z1()
                z1()
                z1()
                z1()
            elif wort[i] == "0":
                z0()
                z1()
                z1()
                z0()
                z0()
                z0()
                z0()

            elif wort[i] == "1":
                z0()
                z1()
                z1()
                z0()
                z0()
                z0()
                z1()

            elif wort[i] == "2":
                z0()
                z1()
                z1()
                z0()
                z0()
                z1()
                z0()

            elif wort[i] == "3":
                z0()
                z1()
                z1()
                z0()
                z0()
                z1()
                z1()

            elif wort[i] == "4":
                z0()
                z1()
                z1()
                z0()
                z1()
                z0()
                z0()

            elif wort[i] == "5":
                z0()
                z1()
                z1()
                z0()
                z1()
                z0()
                z1()

            elif wort[i] == "6":
                z0()
                z1()
                z1()
                z0()
                z1()
                z1()
                z0()

            elif wort[i] == "7":
                z0()
                z1()
                z1()
                z0()
                z1()
                z1()
                z1()

            elif wort[i] == "8":
                z0()
                z1()
                z1()
                z1()
                z0()
                z0()
                z0()

            elif wort[i] == "9":
                z0()
                z1()
                z1()
                z1()
                z0()
                z0()
                z1()
            elif wort[i] == ":":
                z0()
                z1()
                z1()
                z1()
                z0()
                z1()
                z0()

            elif wort[i] == ";":
                z0()
                z1()
                z1()
                z1()
                z0()
                z1()
                z1()

            elif wort[i] == "<":
                z0()
                z1()
                z1()
                z1()
                z1()
                z0()
                z0()

            elif wort[i] == "=":
                z0()
                z1()
                z1()
                z1()
                z1()
                z0()
                z1()

            elif wort[i] == "?":
                z0()
                z1()
                z1()
                z1()
                z1()
                z1()
                z1()

            elif wort[i] == "@":
                z1()
                z0()
                z0()
                z0()
                z0()
                z0()
                z0()
            elif wort[i] == "A":
                z1()
                z0()
                z0()
                z0()
                z0()
                z0()
                z1()

            elif wort[i] == "B":
                z1()
                z0()
                z0()
                z0()
                z0()
                z1()
                z0()

            elif wort[i] == "C":
                z1()
                z0()
                z0()
                z0()
                z0()
                z1()
                z1()

            elif wort[i] == "D":
                z1()
                z0()
                z0()
                z0()
                z1()
                z0()
                z0()

            elif wort[i] == "E":
                z1()
                z0()
                z0()
                z0()
                z1()
                z0()
                z1()

            elif wort[i] == "F":
                z1()
                z0()
                z0()
                z0()
                z1()
                z1()
                z0()

            elif wort[i] == "G":
                z1()
                z0()
                z0()
                z0()
                z1()
                z1()
                z1()

            elif wort[i] == "H":
                z1()
                z0()
                z0()
                z1()
                z0()
                z0()
                z0()

            elif wort[i] == "I":
                z1()
                z0()
                z0()
                z1()
                z0()
                z0()
                z1()

            elif wort[i] == "J":
                z1()
                z0()
                z0()
                z1()
                z0()
                z1()
                z0()

            elif wort[i] == "K":
                z1()
                z0()
                z0()
                z1()
                z0()
                z1()
                z1()

            elif wort[i] == "L":
                z1()
                z0()
                z0()
                z1()
                z1()
                z0()
                z0()
            elif wort[i] == "M":
                z1()
                z0()
                z0()
                z1()
                z1()
                z0()
                z1()

            elif wort[i] == "N":
                z1()
                z0()
                z0()
                z1()
                z1()
                z1()
                z0()

            elif wort[i] == "O":
                z1()
                z0()
                z0()
                z1()
                z1()
                z1()
                z1()

            elif wort[i] == "P":
                z1()
                z0()
                z1()
                z0()
                z0()
                z0()
                z0()

            elif wort[i] == "Q":
                z1()
                z0()
                z1()
                z0()
                z0()
                z0()
                z1()

            elif wort[i] == "R":
                z1()
                z0()
                z1()
                z0()
                z0()
                z1()
                z0()

            elif wort[i] == "S":
                z1()
                z0()
                z1()
                z0()
                z0()
                z1()
                z1()

            elif wort[i] == "T":
                z1()
                z0()
                z1()
                z0()
                z1()
                z0()
                z0()

            elif wort[i] == "U":
                z1()
                z0()
                z1()
                z0()
                z1()
                z0()
                z1()

            elif wort[i] == "V":
                z1()
                z0()
                z1()
                z0()
                z1()
                z1()
                z0()

            elif wort[i] == "W":
                z1()
                z0()
                z1()
                z0()
                z1()
                z1()
                z1()

            elif wort[i] == "X":
                z1()
                z0()
                z1()
                z1()
                z0()
                z0()
                z0()

            elif wort[i] == "Y":
                z1()
                z0()
                z1()
                z1()
                z0()
                z0()
                z1()

            elif wort[i] == "Z":
                z1()
                z0()
                z1()
                z1()
                z0()
                z1()
                z0()

            elif wort[i] == "[":
                z1()
                z0()
                z1()
                z1()
                z0()
                z1()
                z1()

            elif wort[i] == "\\":
                z1()
                z0()
                z1()
                z1()
                z1()
                z0()
                z0()

            elif wort[i] == "]":
                z1()
                z0()
                z1()
                z1()
                z1()
                z0()
                z1()

            elif wort[i] == "^":
                z1()
                z0()
                z1()
                z1()
                z1()
                z1()
                z0()

            elif wort[i] == "_":
                z1()
                z0()
                z1()
                z1()
                z1()
                z1()
                z1()

            elif wort[i] == "`":
                z1()
                z1()
                z0()
                z0()
                z0()
                z0()
                z0()

            elif wort[i] == "a":
                z1()
                z1()
                z0()
                z0()
                z0()
                z0()
                z1()

            elif wort[i] == "b":
                z1()
                z1()
                z0()
                z0()
                z0()
                z1()
                z0()

            elif wort[i] == "c":
                z1()
                z1()
                z0()
                z0()
                z0()
                z1()
                z1()

            elif wort[i] == "d":
                z1()
                z1()
                z0()
                z0()
                z1()
                z0()
                z0()

            elif wort[i] == "e":
                z1()
                z1()
                z0()
                z0()
                z1()
                z0()
                z1()

            elif wort[i] == "f":
                z1()
                z1()
                z0()
                z0()
                z1()
                z1()
                z0()

            elif wort[i] == "g":
                z1()
                z1()
                z0()
                z0()
                z1()
                z1()
                z1()

            elif wort[i] == "h":
                z1()
                z1()
                z0()
                z1()
                z0()
                z0()
                z0()

            elif wort[i] == "i":
                z1()
                z1()
                z0()
                z1()
                z0()
                z0()
                z1()

            elif wort[i] == "j":
                z1()
                z1()
                z0()
                z1()
                z0()
                z1()
                z0()

            elif wort[i] == "k":
                z1()
                z1()
                z0()
                z1()
                z0()
                z1()
                z1()

            elif wort[i] == "l":
                z1()
                z1()
                z0()
                z1()
                z1()
                z0()
                z0()

            elif wort[i] == "m":
                z1()
                z1()
                z0()
                z1()
                z1()
                z0()
                z1()

            elif wort[i] == "n":
                z1()
                z1()
                z0()
                z1()
                z1()
                z1()
                z0()
                
            elif wort[i] == "o":
                z1()
                z1()
                z0()
                z1()
                z1()
                z1()
                z1()

            elif wort[i] == "p":
                z1()
                z1()
                z1()
                z0()
                z0()
                z0()
                z0()

            elif wort[i] == "q":
                z1()
                z1()
                z1()
                z0()
                z0()
                z0()
                z1()

            elif wort[i] == "r":
                z1()
                z1()
                z1()
                z0()
                z0()
                z1()
                z0()

            elif wort[i] == "s":
                z1()
                z1()
                z1()
                z0()
                z0()
                z1()
                z1()

            elif wort[i] == "t":
                z1()
                z1()
                z1()
                z0()
                z1()
                z0()
                z0()

            elif wort[i] == "u":
                z1()
                z1()
                z1()
                z0()
                z1()
                z0()
                z1()

            elif wort[i] == "v":
                z1()
                z1()
                z1()
                z0()
                z1()
                z1()
                z0()

            elif wort[i] == "w":
                z1()
                z1()
                z1()
                z0()
                z1()
                z1()
                z1()

            elif wort[i] == "x":
                z1()
                z1()
                z1()
                z1()
                z0()
                z0()
                z0()

            elif wort[i] == "y":
                z1()
                z1()
                z1()
                z1()
                z0()
                z0()
                z1()

            elif wort[i] == "z":
                z1()
                z1()
                z1()
                z1()
                z0()
                z1()
                z0()

            elif wort[i] == "{":
                z1()
                z1()
                z1()
                z1()
                z0()
                z1()
                z1()

            elif wort[i] == "|":
                z1()
                z1()
                z1()
                z1()
                z1()
                z0()
                z0()

            elif wort[i] == "}":
                z1()
                z1()
                z1()
                z1()
                z1()
                z0()
                z1()

            elif wort[i] == "~":
                z1()
                z1()
                z1()
                z1()
                z1()
                z1()
                z0()
        l= 0
        Senden= False
        Wort=[""]
    
    
    


        
            
            



                
            





def z0():
    basic.set_led_color(Colors.RED)
    #basic.turn_rgb_led_off()
    basic.pause(speed)

def z1():
    basic.set_led_color(Colors.WHITE)
    basic.pause(speed)
    

def connection():
    z1()
    z1()
    z1()
    z1()
    z1()
    z1()
    z1()
    z1()
    
    
basic.forever(on_forever)


