def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char_dict.get(char) == None:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(chars):
    return chars['num']

def sort_char_dict(char_dict):
    char_list = []
    for key in char_dict:
        if key.isalpha():
            char_list.append({"char":key,'num':char_dict[key]})
    char_list.sort(key=sort_on,reverse=True)
    return char_list