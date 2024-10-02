def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = nmb_of_words_in_string(file_contents)
    words = words_apperances(file_contents)
    
    dict_list = []
    for w in words:
        new_dict = {"letter" : w, "num" : words[w]}
        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_dictionary)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n\n")
    for d in dict_list:
        print("The '" + d["letter"] + "' character was found " + str(d["num"]) + " times")
    print("--- End report ---")


    


    

def nmb_of_words_in_string(words):
        new_words = words.split()
        return len(new_words)

def words_apperances(text):
    unique_letter = {}
    for t in text.lower():
        counter = 1
        if t not in unique_letter and t.isalpha() == True:
            unique_letter[t] = 1
        elif t in unique_letter and t.isalpha() == True:
            unique_letter[t] += 1
    return unique_letter

def sort_dictionary(dict):
    return dict["num"]


main()