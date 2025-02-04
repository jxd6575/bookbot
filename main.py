def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    
    #print(text)
    #print(word_count)
    #print (char_count)
    book_report(char_count, word_count, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    text_in_string = text
    text =  text_in_string.split()
    text_count = len(text)
    return text_count

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if (char in char_dict) == False:
            char_dict[char] =  1
            #print("In here")
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(d):
    return d["num"]

def book_report(char_dict, word_count, path):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            temp = {"char": char, "num": char_dict[char]}
            char_list.append(temp)

    char_list.sort(reverse=True, key=sort_on)
    print(f"---- Begin Report of {path} ---")
    print(f"{word_count} words was found in the document\n")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
main()