alphabet = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]


def sentence_to_words(sentence, abeceda):
    slovo = ""
    znak = ""
    slova = []
    jine_znaky = []
    sentence = sentence + "."
    for k in sentence:
        if k in abeceda[0]:
            slovo = slovo + k
            if znak != "":
                jine_znaky.append(znak)
                znak = ""
        elif k in abeceda[1]:
            slovo = slovo + k
            if znak != "":
                jine_znaky.append(znak)
                znak = ""
        else:
            znak = znak + k
            if slovo != "":
                slova.append(slovo)
                slovo = ""
    posledni_znak = znak[:-1]
    jine_znaky.append(posledni_znak)
    return [slova, jine_znaky]


from math import floor, ceil
##floor - zaokrouhleni dolu
##ceil - zaokrouhleni nahoru


def makelist():
    words = open("words_alpha.txt", "r")
    words_list = []
    for word in words:
        words_list.append(word[:-1:])
    return words_list


def sorting_function(neroztrideny_seznam_slov):
    return sorted(neroztrideny_seznam_slov, key=str.lower)


def porovnani(slovo, seznam_slov):
    male_slovo = slovo.lower()
    if len(seznam_slov) < 1:
        return []
    elif len(seznam_slov) == 1:
        if male_slovo == seznam_slov[0]:
            return slovo
        else:
            return []
    elif len(seznam_slov) > 1:
        if male_slovo == seznam_slov[(floor((len(seznam_slov))/2))]:
            return slovo
        else:
            por = sorting_function([male_slovo, seznam_slov[floor((len(seznam_slov))/2)]])
            if male_slovo == por[0]:
                vys = porovnani(slovo, seznam_slov[:(floor(len(seznam_slov) / 2))])
                return vys
            elif male_slovo == por[1]:
                vys = porovnani(slovo, seznam_slov[((floor(len(seznam_slov) / 2))+1):])
                return vys


def choose(list):
    input_index = int(input("Zadejte pořadí slova, které byste chtěli využít: "))
    vyber = list[input_index - 1]
    return vyber


def two_lists_to_sentence(list_one, list_two):
    sentence = ""
    index = 0
    while index < (len(list_one) or len(list_two)):
        if index < len(list_one):
            sentence = sentence + list_one[index]
        if index < len(list_two):
            sentence = sentence + list_two[index]
        index = index + 1
    return sentence


def pridani_do_seznamu(co, kam):
    if co != []:
        if co not in kam:
            kam.append(co)


def divide_delete_function(slovo, knihovna, kam):
    index = 1
    while (index) < len(slovo):
        a = list(slovo)[:index]
        b = list(slovo)[index + 1 :]
        c = ""
        d = ""
        for k in a:
            c = c + k
        for l in b:
            d = d + l
        if (porovnani(c, knihovna) == c) and (porovnani(d, knihovna) == d):
            kam.append(c + " " + d)
        index = index + 1
    return kam


def dividing_function(slovo, knihovna, kam):
    index = 1
    while (index) < len(slovo):
        a = list(slovo)[:index]
        b = list(slovo)[index:]
        c = ""
        d = ""
        for k in a:
            c = c + k
        for l in b:
            d = d + l
        if (porovnani(c, knihovna) == c) and (porovnani(d, knihovna) == d):
            kam.append(c + " " + d)
        index = index + 1
    return kam


def one_letter_more(slovo, knihovna, kam):
    index = 0
    while index < len(slovo):
        t = list(slovo)
        t.pop(index)
        index = index + 1
        v = ""
        for k in t:
            v = v + k
        w = porovnani(v, knihovna)
        pridani_do_seznamu(w, kam)
    return kam


def one_letter_wrong(slovo, abeceda, knihovna, kam):
    index = 0
    while index < len(slovo):
        t = list(slovo)
        t.pop(index)
        for k in abeceda[0]:
            t.insert(index, k)
            v = ""
            for l in t:
                v = v + l
            w = porovnani(v, knihovna)
            pridani_do_seznamu(w, kam)
            t.pop(index)
        index = index + 1
    return kam


def two_letter_change(slovo, knihovna, kam):
    index = 0
    while (index + 1) < len(slovo):
        t = list(slovo)
        u = t.pop(index)
        t.insert(index + 1, u)
        v = ""
        for k in t:
            v = v + k
        w = porovnani(v, knihovna)
        pridani_do_seznamu(w, kam)
        index = index + 1
    return kam


def without_one_letter(slovo, abeceda, knihovna, kam):
    for k in abeceda[0]:
        index = 0
        while index < len(slovo):
            t = list(slovo)
            t.insert(index, k)
            index = index + 1
            v = ""
            for l in t:
                v = v + l
            w = porovnani(v, knihovna)
            pridani_do_seznamu(w, kam)
    return kam

def vyber_slov(seznam_slov, knihovna, abeceda):
    vybrana_slova = []
    for zadane_slovo in seznam_slov:
        vysledek = []
        pridani_do_seznamu(porovnani(zadane_slovo, knihovna), vysledek)
        if vysledek == []:
            print("I ty jeden! Slovo", zadane_slovo, "neexistuje!")
        divide_delete_function(zadane_slovo, knihovna, vysledek)
        dividing_function(zadane_slovo, knihovna, vysledek)
        one_letter_more(zadane_slovo, knihovna, vysledek)
        one_letter_wrong(zadane_slovo, abeceda, knihovna, vysledek)
        two_letter_change(zadane_slovo, knihovna, vysledek)
        without_one_letter(zadane_slovo, abeceda, knihovna, vysledek)
        if vysledek != []:
            index = 0
            vysledek_int = []
            while index < len (vysledek):
                vysledek_int.append([str(index + 1) + "." + str(vysledek[index])])
                index = index + 1
            print("Měl jsi na mysli: ", vysledek_int)
        vybrana_slova.append(choose(vysledek))
    return vybrana_slova


def main():
    zadany_text = input("Napište anglický text: ")
    knihovna = makelist()
    qwer = sentence_to_words(zadany_text, alphabet)
    zadana_slova = qwer[0]
    zadane_znaky = qwer[1]
    a = sorting_function(knihovna)
    zvolena_slova = vyber_slov(zadana_slova, a, alphabet)
    novy_text = two_lists_to_sentence(zvolena_slova, zadane_znaky)
    print(novy_text)


if __name__ == "__main__":
    main()
