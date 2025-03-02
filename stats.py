def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def get_char_count(text):
    text = text.lower()
    char_count = {}
    char_list = []
    for char in text:
        if char in char_count:
            char_count[char] +=1
        else: 
            char_count[char] = 1

    for char, count in char_count.items():
        char_list.append({"char":char, "count": count})
    
    char_list.sort(reverse=True, key=lambda d: d["count"])
    for char_dict in char_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")


