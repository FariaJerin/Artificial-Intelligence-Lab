# Lab Assignment 1:  
    
    
full_name = "Faria Khanam Jerin"
print("Full Name:",full_name)


# count & display the number of vowels and consonants in the name: 
    
vowel_count = 0
consonant_count = 0

vowels = "AEIOUaeiou"

for char in full_name:
    if ('A' <= char <= 'Z' or 'a' <= char <= 'z'):
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:",vowel_count,", ","Consonants:",consonant_count)



# display the ASCII value of each character: 

ascii_values = []

for character in full_name:
    ascii_values.append(ord(character))
    
print("ASCII Values: ",ascii_values)

       
  
# Create a reversed version of the name:

reversed_name = ""

if len(full_name) > 0:
    for i in range(len(full_name) - 1, -1, -1):
        reversed_name += full_name[i]
    print("Reversed Name: ",reversed_name)
else:
    print("Invalid")
  
   
    
# check if the name is a palindrome: 
    
name = full_name.lower().replace(" ", "")
reversed_name = ""

for i in range(len(name) - 1, -1, -1):
    reversed_name += name[i]

is_palindrome = (name == reversed_name)

print("Is Palindrome: ",is_palindrome)
      
   
 
# store each unique letter of the name in a python list and sort it alphabetically:

unique_letters = []

for char in full_name:
    if char != ' ':
        if char not in unique_letters:
            unique_letters.append(char)

unique_letters.sort()
print("Unique Letters (sorted): ",unique_letters)



#Display the first non-repeating character in the name: 
    
first_non_repeating = None

char_counts = {}

for char in full_name:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

for char in full_name:
    if char_counts[char] == 1:
        first_non_repeating = char
        break

if first_non_repeating:
    print("First Non-Repeating Character: ",first_non_repeating)
else:
    print("There are no Non-Repeating Characters.")
    
    
