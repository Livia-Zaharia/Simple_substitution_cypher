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



def reverse_dict(my_dict):
    my_reversed_dict={}
    for letter in my_dict.items():
        
        my_reversed_dict[letter[1]]=letter[0]
    return my_reversed_dict



def key_prep(text):
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
    

    i=len(key_dict.keys())-1

    for letter in alphabet:
        key_dict.setdefault(letter, alphabet[i])
        i+=1
        
    return key_dict

def mess_prep(text):
    pass

def encoded(mess,key):
    key_dict=reverse_dict(key_prep(key))

def decoded(mess,key):
    key_dict=key_prep(key)


def main():
   global alphabet
   alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z"]
   encode_decode=input("do you want to encode or decode? E/D")

   if encode_decode.upper()=="E":
       message_to_be_encoded=input("Your message to be encoded please: ")
       key_to_encode=input("the key to encode with:")
       print(encoded(message_to_be_encoded,key_to_encode))
   elif encode_decode.upper()=="D":
        message_to_be_decoded=input("Your message to be decoded please: ")
        key_to_decode=input("the key to decode with:")
        print(decoded(message_to_be_decoded,key_to_decode))
       





       

if __name__=="__main__":
    main()