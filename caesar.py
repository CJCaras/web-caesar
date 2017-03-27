def alphabet_position(letter):
    #This function provides a value of 0 - 25, depending on the letter, without changing or creating anything
    l = "abcdefghijklmnopqrstuvwxyz"
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in l:
        return l.index(letter)
    else:
        return u.index(letter)

def rotate_character(char, rot):

    #if char is not from the alphabet, return the char as it is
    if char.isalpha() == False:
        return char

    #get the new character index by adding the rot value to the alphabet position of the char parameter
    newCharIdx = (alphabet_position(char) + rot) % 26

    l = "abcdefghijklmnopqrstuvwxyz"
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #return new character plus rot# from l/u
    if char.islower() is True:
        return l[newCharIdx]
    else:
        return u[newCharIdx]

def encrypt(text, rot):

    newText = ""
    for char in text:
        newText = newText + rotate_character(char, rot)
    return newText
