def is_palindrome(word):
    # Convert the word to lowercase and remove any spaces
    word = word.lower().replace(" ", "")
    
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False
