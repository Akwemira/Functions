""" 
translator.py
"""
supported_languages = ["english", "french"]

french_to_english_dict = {
    "prune" : "african plum",  
    "belle" : "pretty", 
    "eglise" :"church",
    "meilleur" : "best",
    "frère" : "brother",
    "maman" : "mother"
}

english_to_french_dict = {
    "african plum" : "prune",
    "pretty" : "belle",
    "church" : "eglise",
    "best" : "meilleur",
    "brother" : "frère",
    "mother" : "maman"
    }


def translate_english_word(user_input_word):
    '''
    Description: this function translates a word from english to french
    Parameter: user_input_word
    Returns: english_to_french_dict.get(user_input_word)
    '''
    return english_to_french_dict.get(user_input_word)

def translate_french_word(user_input_word):
    '''
    Description: this function translates a word from french to english
    Parameter: user_input_word
    Returns: french_to_english_dict.get(user_input_word)
    '''
    return french_to_english_dict.get(user_input_word)
    
    
if __name__ == '__main__':
    while True:
        user_language_preference = input("Please enter a language to translate from?:\n")

        if user_language_preference in supported_languages:
            user_input_word = input(f"\nNow enter a word in {user_language_preference}\nOtherwise enter q to exit translator\n").lower() #word from user set to lowercase
            if user_input_word in french_to_english_dict: 
                english_word = french_to_english_dict.get(user_input_word)
                print(f"\nThe English equivalent of {user_input_word} is {english_word}\n")

            elif user_input_word in english_to_french_dict:
                french_word = english_to_french_dict.get(user_input_word)                    
                print(f"\nThe French equivalent of {user_input_word} is {french_word}\n")

            elif user_input_word == "q":
                    print('Exiting translator. Thank you')
                    break
            else:
                print (f"Your word does not exist in this dictionary\n")

        else:
            print (f"{user_language_preference} not a supported language. Choose english or french.\n")


    




