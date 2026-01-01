"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-22

                                                Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."

"""
def wise_speak(sentence):
    org_punct = sentence[-1]

    sentence = sentence.replace(org_punct, ',')

    sentence = sentence[0].lower() + sentence[1:]
    word_lst = sentence.split()
    #determine the position of special word
    special_index = None

    for i in range(len(word_lst)):
        if word_lst[i] in ["have", "must", "are", "will", "can"]:
            special_index = i
            break
    
    # Make the new order
    word_lst = word_lst[special_index+1:] + word_lst[:special_index+1]
    word_lst[-1] = word_lst[-1] + org_punct
    word_lst[0] = word_lst[0][0].upper() +word_lst[0][1:]
    print(word_lst)
    return ' '.join(word_lst)

print(wise_speak("You must speak wisely."))