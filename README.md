# Simple_substitution_cypher
encodes and decodes a message based on a phrase

main ideea is that encryption and decryption in this case are strongly related
for encrytion we build a dict using the letters from whatever key we have given taken once, followed by the rest of the
letters in the alphabet take once, without those already used. However, if we were to use such a dict we could not encrypt because
for any "normal" letter in the message we want to modify we need to have the corresponding letter from our key. this is why we reverse the dict we built
And the transformation from uncoded word to coded word is done in place

for decryption- we already had the def to obtain the keys and values- so it is basically the same path, without swapping the dict

in the example copied from wiki it might be clearer

Plaintext alphabet	ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphertext alphabet	ZEBRASCDFGHIJKLMNOPQTUVWXY

so if we want to encode A->Z in whatever text we put into, but if we were to decode A->E to get something readable- 
this is why i said for encryption we need to reverse the dict keys become values and values become keys
