from stats import count_words, count_chars, sort_char_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content
def print_char_list(list):
    for item in list:
        print(f"{item["char"]}: {item["num"]}")
def print_opening_statemant(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
def print_intermediate_word_count_headline():
    print("----------- Word Count ----------")

def print_intermediate_char_count():
    print("--------- Character Count -------")

def print_end_row():
    print("============= END ===============")

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        
    
    filepath = sys.argv[1]  
    book_text = get_book_text(filepath)
    words_count = count_words(book_text)
    char_dict = count_chars(book_text)
    print_opening_statemant(filepath)
    print_intermediate_word_count_headline()
    print(f"Found {words_count} total words")
    print_intermediate_char_count()
    sorted_char_list = sort_char_dict(char_dict)
    print_char_list(sorted_char_list)
    print_end_row()

main()