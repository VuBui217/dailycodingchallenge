"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-12

                                                    Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.

"""
def get_word_value(word):
        value = 0
        for ch in word:
            value += (ord(ch) - ord('A') + 1) * 2 if ch.isupper() else (ord(ch) - ord('a') + 1)
        return value
def battle(our_team, opponent):

    win_count = 0
    my_team = our_team.split(' ')
    opponent_team = opponent.split(' ')
    
    n = len(my_team)
        
    for i in range(n):
        if get_word_value(my_team[i]) > get_word_value(opponent_team[i]):
            win_count+=1
        elif get_word_value(my_team[i]) < get_word_value(opponent_team[i]):
            win_count-=1
        else:
            continue
    print(win_count)
    if win_count > 0:
        return 'We win'
    elif win_count == 0:
        return 'Draw'
    else:
        return 'We lose'
    

