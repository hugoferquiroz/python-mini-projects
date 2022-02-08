#palindromes


def is_palindrome(words):
    words = words.replace(' ', '')
    words = words.lower()
    reverse_word = words[::-1]
    if words == reverse_word:
        return  True
    else:
        return False
    

def run():
    words = input('Write your words: ')
    palindrome = is_palindrome(words)
    if palindrome == True:
        print('It\'s palindrome')
    else:
        print('It\'s not palindrome')


if __name__ == '__main__':
    run()

