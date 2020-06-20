txt = str(input())

delete_punctuations = txt.strip(",.!?")
remove_comma = delete_punctuations.replace(",", "")
remove_period = remove_comma.replace(".", "")
remove_exclaim = remove_period.replace("!", "")
remove_question = remove_exclaim.replace("?", "")
lower_txt = remove_question.lower()

print(lower_txt)
