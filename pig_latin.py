"""
Move first consonant(s) to end + "ay" or add "yay" for vowels.

split on whitespace; for each word, move consonant cluster to 
end + “ay” (or “yay” if vowel); preserve capitalization and punctuation.

"""

VOWELS = "aeiou"
CONSONANT_CLUSTERS = [
    "bl", "br", "ch", "cl", "cr", "dr", "fl", "fr",
    "gl", "gr", "pl", "pr", "qu", "sc", "sh", "sk",
    "sl", "sm", "sn", "sp", "st", "sw", "th", "tr",
    "tw", "wh", "wr"
]

def get_user_input():
    valid_input = False
    while not valid_input:
        pre_translation = input("What word would you like " \
        "to translate? ").lower()
        valid_input = validate_input(pre_translation)
    # print(pre_translation.split())
    return pre_translation.split()

def validate_input(user_input):
    words_in_list = user_input.split()
    for word in words_in_list:
        if not word.isalpha():
            print("Please enter only letters!")
            return False
        else:
            return True

def start_of_word(word):
    first_letter = word[0].lower()
    if first_letter in VOWELS:
        return first_letter
    else:
        for cluster in CONSONANT_CLUSTERS:
            if word.startswith(cluster):
                return cluster
        else:
            return first_letter

def vowel_start_mod(word):
    return (word + "way")

def consonant_start_mod(word, beginning_letter):
    translated_word = ""
    letter_list = []
    if beginning_letter == 1:
        for i in range(1, len(word)):
            letter_list.append(word[i])
        letter_list.append(word[0] + "ay")

    elif beginning_letter == 2:
        for i in range(2, len(word)):
            letter_list.append(word[i])
        letter_list.append(word[0] + word[1] + "ay")
    
    return translated_word.join(letter_list)

def pig_latin_translator(word):

    beginning_letter = start_of_word(word)
    translation = ""
    if beginning_letter in VOWELS:
        translation = vowel_start_mod(word)
    else:
        translation = consonant_start_mod(word, len(beginning_letter))

    return translation

def pig_latin_sentence():
    sentence = get_user_input()
    translated_sentence = ""
    for word in sentence:
        if word == sentence[0]:
            translated_sentence += pig_latin_translator(word).capitalize() + " "

        elif word == sentence[-1]:
            translated_sentence += pig_latin_translator(word)

        else:
            translated_sentence += pig_latin_translator(word) + " "
    print(translated_sentence)
    return translated_sentence

pig_latin_sentence()