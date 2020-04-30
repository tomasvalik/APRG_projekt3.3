def stringtolist():
##udělá ze zadané věty seznam, každé slovo je zároveň v seznamu

    input_task = input("Zadejte větu: ")
    input_list = []
    
    slice = input_task.split(" ")
    chars = [",", ".", "-", "/", "?", "!"]
    
    for word in slice:
        if word[-1] in chars:
            word = word[:-1]
        
        input_list.append(word)

    return input_list

def makelist():
##udělá z textového souboru seznam a odstraní "\n" ze stringu

    words = open("words_alpha.txt", "r")
    words_list = []

    for word in words:
        words_list.append(word[:-1:])

    return words_list


def difference(correct, guess):
    ##levenshteinova vzdálenost, vrátí rozdílnost porovnávaných slov
    ##pokud vrátí 0, slovo je totožné

    rows = len(correct) + 1
    collumns = len(guess) + 1
    distance = [[0 for x in range(collumns)] for x in range(rows)]

    for i in range(1, rows):
        distance[i][0] = i

    for i in range(1,collumns):
        distance[0][i] - i

    for collumn in range(1, collumns):
        for row in range(1, rows):
            if correct[row - 1] == guess[collumn - 1]:
                cost = 0
            else:
                cost = 1
            distance[row][collumn] = min(distance[row - 1][collumn] + 1,                ##chybějící písmeno
                                         distance[row][collumn - 1] + 1,                ##navíc písmeno
                                         distance[row - 1][collumn - 1] + cost)         ##nahrazené písmeno
   

    return distance[row][collumn]


def sort():
##mělo by roztřídit slova knihovny podle levenshteinovy vzdálenosti, pokud je stejné, tj == 0, tak vyhledávání
##přeskočí, pokud je vyšší než 2, tak ho taky přeskočí
##má dlouhou výpočetní dobu a vyhodí to zpravidla krátká slovas podobnými písmeny
   
    words_list = makelist()
    input_list = stringtolist()

    similar = []

    for list in input_list:
        for word in words_list:
            if difference(word, list) > 1:
                continue
            elif difference(word, list) == 0:
                break
            else:
                print("Nechtěli jste napsat: ", similar)

            
def main():
    sort()

if __name__ == "__main__":
    main()
