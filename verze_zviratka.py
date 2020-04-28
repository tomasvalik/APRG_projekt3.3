knihovna = ["pes", "kocka", "krava", "zajic", "kos", "tygr", "krokodyl", "medved", "kun", "straka", "veverka", "prase", "slepice", "delfin", "nosorozec", "kralik", "had", "pavouk", "zaba", "snek", "krtek", "klokan", "hroch", "jelen", "ryba"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
zadane_slovo = "zajic"

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


def pridani_do_seznamu(co, kam):
    if co != None:
        if co != []:
            if co not in kam:
                kam.append(co)


def pridani_do_seznamu_main(co, kam):
    if co != None:
        if co != []:
            for k in co:
                kam.append(k)


def divide_delete_function(slovo, knihovna, kam):
    vysledek_divide_delete_function = []
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
    return vysledek_divide_delete_function



def dividing_function(slovo, knihovna, kam):
    vysledek_dividing_function = []
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
    vysledek_one_letter_more = []
    u = 0
    while u < len(slovo):
        t = list(slovo)
        o = t.pop(u)
        u = u + 1
        v = ""
        for k in t:
            v = v + k
        w = porovnani(v, knihovna)
        pridani_do_seznamu(w, kam)
    return kam


def one_letter_wrong(slovo, abeceda, knihovna, kam):
    vysledek_one_letter_wrong = []
    index = 0
    while index < len(slovo):
        t = list(slovo)
        t.pop(index)
        for k in alphabet:
            t.insert(index, k)
            s = ""
            for l in t:
                s = s + l
            w = porovnani(s, knihovna)
            pridani_do_seznamu(w, kam)
            t.pop(index)
        index = index + 1
    return kam


def two_letter_change(slovo, knihovna, kam):
    vysledek_two_letter_change = []
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


def without_one_letter(slovo, knihovna, kam):
    vysledek_without_one_letter = []
    for k in alphabet:
        y = 0
        while y < len(slovo):
            r = list(slovo)
            r.insert(y, k)
            y = y + 1
            v = ""
            for l in r:
                v = v + l
            w = porovnani(v, knihovna)
            pridani_do_seznamu(w, kam)
    return kam


def main():
    vysledek = []
    a = sorting_function(knihovna)
    porovnani(zadane_slovo, a)
    divide_delete_function(zadane_slovo, a, vysledek)
    dividing_function(zadane_slovo, a, vysledek)
    one_letter_more(zadane_slovo, a, vysledek)
    one_letter_wrong(zadane_slovo, alphabet, a, vysledek)
    two_letter_change(zadane_slovo, a, vysledek)
    without_one_letter(zadane_slovo, a, vysledek)
    if len(vysledek) == 1:
        vysledek = vysledek[0]
    print(vysledek)


if __name__ == "__main__":
    main()