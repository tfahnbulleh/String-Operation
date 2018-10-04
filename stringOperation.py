def countCharacter(phrase,characterToCount):
    total=0
    for cha in phrase:
        if cha == characterToCount:
            total=total+1
    return total

def convertToLower(phrase):
    return str(phrase).lower()


def convertToUpper(phrase):
    return str(phrase).upper()


def totalCharacters(phrase):
    return len(phrase)


def removeCharacter(phrase,charaterToRemove, newCharacter):
    str(phrase).replace(charaterToRemove,newCharacter)

#reverse string
def reverseString(phrase):
    lastCharacterIndex=len(phrase)-1
    newPhrase=''
    while lastCharacterIndex>=0:
        newPhrase=newPhrase+phrase[lastCharacterIndex]
        lastCharacterIndex=lastCharacterIndex-1
    return newPhrase

print(reverseString('Tamu'))