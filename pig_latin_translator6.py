original = input("Please enter a sentence: ").strip().lower()

# Split sentence into words
words = original.split()

# Loop through words and convert to Pig Latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# Stick words back together
output = " ".join(new_words)

# Output the final string
print(output)

# Output 
# Please enter a sentence: I like to play games  
# iyay ikelay otay ayplay amesgay