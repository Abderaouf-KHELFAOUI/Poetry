# Number-to-Words Converter for Text
# https://open.kattis.com/problems/wordsfornumbers
#


from num2words import num2words

def numbers_to_words(line):
    tokens = line.split()
    new_tokens = []

    for i, token in enumerate(tokens):
        if token.isdigit():  # check if the token is a decimal number
            # convert number to words, hyphenated
            word = num2words(int(token), to='cardinal', lang='en').replace(' ', '-')
            if i == 0:  # capitalize first word if it's at start of line
                word = word.capitalize()
            new_tokens.append(word)
        else:
            new_tokens.append(token)

    return ' '.join(new_tokens)
