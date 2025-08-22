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
def get_user_word():
    valid_input = False
    while not valid_input:
        pre_translation = input("What word would you like " \
        "to translate? ").lower()
        valid_input = validate_input(pre_translation)

    return pre_translation

def validate_input(user_input):
    if not user_input.isalpha():
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
    return (word + "way").capitalize()

def consonant_not_cluster(word):
    translated_word = ""
    letter_list = []
    for i in range(1, len(word)):
        letter_list.append(word[i])
    letter_list.append(word[0] + "ay")
    return translated_word.join(letter_list)

def cluster_start_mod(word):
    translated_word = ""
    letter_list = []
    for i in range(2, len(word)):
        letter_list.append(word[i])
    letter_list.append(word[0] + word[1] + "ay")
    return translated_word.join(letter_list)

def pig_latin_translator():
    word = get_user_word()
    beginning_letter = start_of_word(word)
    translation = ""
    if beginning_letter in VOWELS:
        translation = vowel_start_mod(word)
    else:
        if len(beginning_letter) == 1:
            # move consonant to the end and add ay
            translation = consonant_not_cluster(word)
        else:
            # this is a cluster. move the cluster then add ay to end
            translation = cluster_start_mod(word)
    print(translation)

pig_latin_translator()