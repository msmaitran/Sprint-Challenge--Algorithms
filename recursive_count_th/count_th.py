'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case
    if len(word) < 2:
        return 0
    # check to see if the word contains 'th'
    # if contains 'th' add to count_th, remove and cycle through
    elif word [:2] == "th":
        return 1 + count_th(word[2:])
    # remove first character and cycle through
    return count_th(word[1:])