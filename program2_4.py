print('Lesson 2_4')

wordlist = list(input('Input list of words separated by space: ').split ())


for i, element in enumerate(wordlist):
    print(f"Word {i:02}: {element[:10]}")
