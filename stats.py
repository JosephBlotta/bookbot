def get_num_words(words):
    return len(words.split())

def char_num_count(words):
    char_num_dic ={}
    chars = words.lower()
    for char in chars:
        if char in char_num_dic:
            char_num_dic[char] += 1
        else:
            char_num_dic[char] = 1
    return char_num_dic

def sort_on(items):
    return items["num"]

def sort_dic(dic):
    list_of_dic = []
    for d in dic:
        if d.isalpha():
            list_of_dic.append({"char":d,"num": dic[d]})

    list_of_dic.sort(reverse=True, key=sort_on)
    return list_of_dic