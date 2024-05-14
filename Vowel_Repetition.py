def most_frequent_vowels(s):
    vowels='aeiou'
    vowel_count={}
    for v in vowels:
        vowel_count[v]=0
    for char in s:
        if char in vowels:
            vowel_count[char]+=1
    most_frequent=None
    max_count=-1
    for vowel in vowels:
        if vowel_count[vowel]>max_count:
            most_frequent=vowel
            max_count=vowel_count[vowel]
    return most_frequent
s=input("Enter the string\n")
print(most_frequent_vowels(s))                   