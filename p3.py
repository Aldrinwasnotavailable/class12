def check_if_vowel(alphabet):
    # Check if the given alphabet is a vowel
    vowels = 'aeiouAEIOU'
    if alphabet in vowels:
        return True
    else:
        return False
    
alphabet = input("Enter an alphabet: ")