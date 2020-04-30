alphabet = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]


def sentence_to_words(sentence, abeceda):
    slovo = ""
    slova = []
    jine_znaky = []
    sentence = sentence + "."
    for k in sentence:
        if k in abeceda[0]:
            slovo = slovo + k
        elif k in abeceda[1]:
            slovo = slovo + k
        else:
            jine_znaky.append(k)
            if slovo != "":
                slova.append(slovo)
                slovo = ""
    return [slova, jine_znaky]


from math import floor, ceil
##floor - zaokrouhleni dolu
##ceil - zaokrouhleni nahoru


def makelist():
    words = open("words_alpha.txt", "r")
    words_list = []
    for word in words:
        words_list.append(word[:-2:])
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


def pridani_do_seznamu(co, kam):
    if co != None:
        if co != []:
            if co not in kam:
                kam.append(co)


def divide_delete_function(slovo, knihovna, kam):
    index = 1
    while (index) < len(slovo):
        a = list(slovo)[:index]
        b = list(slovo)[index+1:]
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


def main():
    zadany_text = input("Napište anglický text: ")
    knihovna = makelist()
    qwer = sentence_to_words(zadany_text, alphabet)
    zadana_slova = qwer[0]
    zadane_znaky = qwer[1]
    print(zadana_slova)
    print(zadane_znaky)
    for zadane_slovo in zadana_slova:
        print(zadane_slovo)
        vysledek = []
        a = sorting_function(knihovna)
        pridani_do_seznamu(porovnani(zadane_slovo, a), vysledek)
        if vysledek == []:
            print("I ty jeden! Takove slovo neexistuje!")
        divide_delete_function(zadane_slovo, a, vysledek)
        dividing_function(zadane_slovo, a, vysledek)
        one_letter_more(zadane_slovo, a, vysledek)
        one_letter_wrong(zadane_slovo, alphabet, a, vysledek)
        two_letter_change(zadane_slovo, a, vysledek)
        without_one_letter(zadane_slovo, alphabet, a, vysledek)
        if vysledek != []:
            print("Měl jsi na mysli: ", vysledek)


if __name__ == "__main__":
    main()
