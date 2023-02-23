def has_five_letter_palindrome(s):
    """Check if a string s contains a 5-letter palindrome."""
    for i in range(len(s) - 4):
        if s[i:i+5] == s[i:i+5][::-1]:
            return True
    return False

def examine_strings(strings):
    """Examine a list of strings and identify any subsets that contain a 5-letter palindrome."""
    for s in strings:
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                subset = s[i:j]
                if len(subset) >= 5 and has_five_letter_palindrome(subset):
                    print(f"{subset} in string '{s}' contains a 5-letter palindrome")

strings = ""
with open("palindrome_str.txt") as file:
   strings = file.read()

print(strings)
examine_strings(strings)


