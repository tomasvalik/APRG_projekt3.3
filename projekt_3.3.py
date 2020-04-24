
from math import floor, ceil
##floor - zaokrouhleni dolu
##ceil - zaokrouhleni nahoru


def sorting_function(neroztrideny_seznam_slov):
    return sorted(neroztrideny_seznam_slov, key=str.lower)


def porovnani(slovo, seznam_slov):
    if len(seznam_slov) < 1:
        return []
    elif len(seznam_slov) == 1:
        if slovo == seznam_slov[0]:
            return seznam_slov[0]
    elif len(seznam_slov) > 1:
        if slovo == seznam_slov[(floor((len(seznam_slov))/2))]:
            return seznam_slov[(floor((len(seznam_slov))/2))]
        else:
            por = sorting_function([slovo, seznam_slov[floor((len(seznam_slov))/2)]])
            if slovo == por[0]:
                vys = porovnani(slovo, seznam_slov[:(floor(len(seznam_slov) / 2))])
                return vys
            elif slovo == por[1]:
                vys = porovnani(slovo, seznam_slov[((floor(len(seznam_slov) / 2))+1):])
                return vys


def main():
    zadane_slovo = input("Zadejte slovo: ")
    with open("words_alpha.txt", encoding='utf-8') as file_name:
        words_dictionary = file_name.read()
    

if __name__ == "__main__":
    main()
