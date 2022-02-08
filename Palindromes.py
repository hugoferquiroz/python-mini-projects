#palindromes


def is_palindrome():
    your_word = your_words.replace(' ', '')
    your_word = your_word.lower()
    your_reverse_word = your_word[::-1]
    if your_word == your_reverse_word:
        return  True
    else:
        return False
    

def run():
    your_words = input('Write your words: ')
    palindrome = is_palindrome(your_words)
    if is_palindrome == True:
        print('It\'s palindrome')
    else:
        print('It\'s not palindrome')


if __name__ == '__main__':
    run()
