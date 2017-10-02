def kmp():
    word = str(input()).title() #title so no capital letter between first, middle and last name will be printed
    for letter in word:
        if letter.isupper() and "-" in word:#checks for capital letter in the beginning of each name.
            print(letter, end="")#prints in one line
kmp()
