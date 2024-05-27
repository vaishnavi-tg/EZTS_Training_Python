
def magic_string(s):
    char_count={}
    for char in s :
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    max_frq=0
    for count in char_count.values():
        if count>max_freq:
            max_freq=count
        min_steps=len(s)-max_freq    
        return min_steps

s='aaabbbccdddd' 
print(magic_string(s))               
