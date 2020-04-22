

def sorting_function(neroztrideny_seznam_slov):
    return sorted(neroztrideny_seznam_slov, key=str.lower)


def main():
    zadane_slovo = input("Zadejte slovo: ")
    with open("words_alpha.txt", encoding='utf-8') as file_name:
        words_dictionary = file_name.read()
    

if __name__ == "__main__":
    main()
