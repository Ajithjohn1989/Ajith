# Original list of words
words = ["apple", "banana", "orange", "umbrella", "grape", "avocado", "elephant"]

# Extract words starting with vowels
vowel_words = [word for word in words if word[0].lower() in "aeiou"]

# Display the new list
print("Words starting with vowels:", vowel_words)

