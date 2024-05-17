string = input("Enter string: ")

split_string = string.split()
print(split_string)
longest = 0

for i in split_string:
    if len(i)>longest:
        longest = len(i)

print(longest)
