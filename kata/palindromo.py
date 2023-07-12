def clean(phrase):
    cleanphrase = str(phrase).lower()
    '''
        looking for punctuation
    '''
    characters_to_remove = [",", ".", "!", "¡", "¿", "?"," "]
    for character in characters_to_remove:
        cleanphrase = cleanphrase.replace(character,"")
    
    return cleanphrase

def reverse(phrase):
    reversed_phrase = phrase[::-1]
    return reversed_phrase


def es_palindromo(phrase):
    '''' 
    cleaning the string
    '''
    phrase = clean(phrase)
    reversed_phrase = reverse(phrase)
    return (phrase == reversed_phrase)
    

print(es_palindromo('Amo la pacifica paloma...'))
    