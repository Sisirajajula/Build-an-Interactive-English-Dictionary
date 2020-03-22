import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(myWord):
    myWord = myWord.lower()
    if myWord in data:
        return data[myWord]
    elif myWord.title() in data:
        return data[myWord.title()]
    elif myWord.upper() in data:
        return data[myWord.upper()]
    elif len(get_close_matches(myWord, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(myWord, data.keys())[0]} instead? Enter Y if yes,or N if no: ")
        if yn == "Y":
            return data[get_close_matches(myWord, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist.Please double check it"
        else:
            return "we didn't understand your entry"
    else:
        return "The word doesn't exist.Please double check it"
while True:
    word = input("Enter word: ")
    if word != "end":
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
    
        else:
            print(output)
    else:
        print("End of entry")
        break

    


