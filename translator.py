""" 
This function translates user_input_word to french or english.

Args:
 Uses 2 dictionaries: french_to_english and english_to_french. We collect user_input_word and call translator()
 function and use .get() method to extract value of user_input_word from both dictionaries.
 Returns:
 Equivalent of user_input_word in other language. Also prints "word does not exist" if user_input_word not in both dictionaries
"""

def translator(word):

    if user_input_word in french_to_english_dict : 
        english_word = french_to_english_dict.get(user_input_word)
        print(f"The English equivalent of {user_input_word} is {english_word}")

    elif user_input_word in english_to_french_dict:
        french_word = english_to_french_dict.get(user_input_word)                    
        print(f"The French equivalent of {user_input_word} is {french_word}")

    else:
        print (f"Your word does not exist in this dictionary")

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

user_input_word = input("Give me a word in French or English\n").lower() #word from user set to lowercase
translator(user_input_word) # calling translator() function defined at the begining




