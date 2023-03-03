"""
how substitution cypher works(from wikipedia)

Substitution of single letters separately—simple substitution—can be demonstrated by writing out the alphabet in some 
order to represent the substitution. This is termed a substitution alphabet. The cipher alphabet may be shifted 
or reversed (creating the Caesar and Atbash ciphers, respectively) or scrambled in a more complex fashion, 
in which case it is called a mixed alphabet or deranged alphabet. Traditionally, mixed alphabets may be created by first
 writing out a keyword, removing repeated letters in it, then writing all the remaining letters in the alphabet in the usual order.
Using this system, the keyword "zebras" gives us the following alphabets:

Plaintext alphabet	ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphertext alphabet	ZEBRASCDFGHIJKLMNOPQTUVWXY

A message
flee at once. we are discovered!
enciphers to
SIAA ZQ LKBA. VA ZOA RFPBLUAOAR!
"""



def reverse_dict(my_dict:dict)->dict:
    my_reversed_dict={}
    for letter in my_dict.items():
        
        my_reversed_dict[letter[1]]=letter[0]
    return my_reversed_dict



def key_prep(text:str)->dict:
    text=text.upper()
    words=[]
    key_dict={}
    i=0
    words=text.split()
    for word in words:
        if not word[-1].isalpha():
            new_word=word.rstrip(word[-1])
        else:
            new_word=word
        for letter in new_word:
            key_dict.setdefault(letter,alphabet[i])
            i=len(key_dict.keys())
        
    

    for letter in alphabet:
        if not key_dict.get(letter, False):
            key_dict.setdefault(letter, alphabet[i])
            i+=1
 
    return key_dict

def mess_prep(text:str,key:dict)->list:
    text=text.upper()
    words=[]
    
    new_words=[]
    i=0
    words=text.split()
    for word in words:
       new_word=''
       for letter in word:
            
            if letter.isalpha():
                new_letter=key[letter]
            else:
                new_letter=letter
            
            new_word+=new_letter

        
       new_words.append(new_word)


    return new_words

    

def encode_decode(mess,key,toggle):
    if toggle:
        key_dict=reverse_dict(key_prep(key))
    else:
        key_dict=key_prep(key)

    return " ".join(mess_prep(mess,key_dict))


def main():
   global alphabet
   alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z"]
   switch=input("do you want to encode or decode? E/D")
   message=input("Your message please: ")
   key=input("the key:")

   if switch.upper()=="E":
       print(encode_decode(message,key,True))
   elif switch.upper()=="D":
       print(encode_decode(message,key,False))
       

      

if __name__=="__main__":
    main()