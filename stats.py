def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count_dict = {}
    for char in text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict


def sort_on(items):
    return items["num"]


def get_sorted_char_count(char_count_dict):
    char_dict_list = []
    for char, count in char_count_dict.items():
        #print(f"Character: {char}, Count: {count}")
        char_dict = {"char": char, "num": count}
        char_dict_list.append(char_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

