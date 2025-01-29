def main():
    text = book_text(choose_book_path())
    word_count = word_counter(text)
    chars_count_dict = char_count(text)
    chars_count_list_sorted = char_count_sorted_list(chars_count_dict)
    chars_count_list_sorted_alphaonly = char_count_sorted_list_alphaonly(chars_count_list_sorted)

    #Begin Report Function

    print("--- Begin report of books/frankenstein.txt --- \n")
    print(word_count, "words found in the document")
    print(chars_count_list_sorted_alphaonly)
    print("--- End report ---")

def choose_book_path():
    file_path = "books/frankenstein.txt"
    return file_path

def book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_book():
    # prints the output of the open book to the console
    print(file_contents)

def word_counter(word_count_text_input):
    # counts the total number of words in the book
    words = word_count_text_input.split() # splits the book-as-string to a list
    count_of_words = len(words) # counts the number of strings in variable $words and stores as an integer
    return count_of_words # returns the variable count_of_words

def char_count(char_count_text_input):
    chars = {}
    for c in char_count_text_input:
        lowered_text = c.lower() # ensures every char in variable_contents is lowercase to prevent counting both upper and lowercase as separate charachters
        if lowered_text in chars:
            chars[lowered_text] += 1 # if the charachter is already in the dictionary of charachters, it will add one to the tally
        else:
            chars[lowered_text] = 1 # if the charachter is not in the dictionary of characters, it will set the tally to '1'
    return chars

def sort_on(d):
    return d["num"]

def char_count_sorted_list(char_count_sorted_list_dict):
    sorted_list = []
    for ch in char_count_sorted_list_dict:
        sorted_list.append({"char": ch, "num": char_count_sorted_list_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def char_count_sorted_list_alphaonly(char_count_sorted_list_alphaonly_input):
    alpha_only_sorted_string = ""
    for ch in char_count_sorted_list_alphaonly_input:
        if not ch["char"].isalpha():
            continue
        alpha_only_sorted_string += f"The '{ch['char']}' character was found {ch['num']} times \n"
#        alpha_only_sorted_string.append(f"The '{ch['char']}' character was found {ch['num']} times \n")
    return alpha_only_sorted_string
        
main ()