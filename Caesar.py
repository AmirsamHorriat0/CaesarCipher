def encrypt(text , shift) :
    # to store the result
    result = ""

    # Caesar main logic 
    for i in text :
        if 'A' <= i <= 'Z' :
            
            '''mod 26 to wrap around the alphabet
            Example : letter -> Y , shift -> 3 
            ord('Y') - 65 = 24 -> 24 + 3 = 27 -> 27 % 26 = 1 ('B')
            '''
            # A in ASCII table is 65
            result += chr((ord(i) - 65 + shift) % 26 + 65)
        elif 'a' <= i <= 'z' :
            #a in ASCII table is 97
            result += chr((ord(i) - 97 + shift ) %26 + 97)
        else :
            result += i
    return result
print('''
_________                                             .__       .__                  
╲_   ___ ╲_____    ____   ___________ _______    ____ │__│_____ │  │__   ___________ 
╱    ╲  ╲╱╲__  ╲ _╱ __ ╲ ╱  ___╱╲__  ╲╲_  __ ╲ _╱ ___╲│  ╲____ ╲│  │  ╲_╱ __ ╲_  __ ╲
╲     ╲____╱ __ ╲╲  ___╱ ╲___ ╲  ╱ __ ╲│  │ ╲╱ ╲  ╲___│  │  │_> >   Y  ╲  ___╱│  │ ╲╱
 ╲______  (____  ╱╲___  >____  >(____  ╱__│     ╲___  >__│   __╱│___│  ╱╲___  >__│   
        ╲╱     ╲╱     ╲╱     ╲╱      ╲╱             ╲╱   │__│        ╲╱     ╲╱       
      ''')

choice = input("Encrypt with e and Dicrypt with d ")


def decrypt(text , shift) :
    return encrypt(text , -shift)

if choice == "e" :

    text = input("Enter your text : ")
    shift = int(input("Enter the shift : "))
    print("Result : " , encrypt(text , shift)) 

elif choice == "d" :
    text = input("Enter your encrypted text ")
    shift = int("Enter the shift ")
    print("Result :" , decrypt(text , shift))

else :
    raise ValueError
