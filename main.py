def countWords(string):
    return len(string.split())
def countChars(string):
    my_dict = {}
    for s in string.lower():
        if s in my_dict:
            my_dict[s]  +=1
        else:
            my_dict[s] = 1
    return my_dict

def dictToList(dict):
    lista = []
    for key in dict:
        if key.isalpha():
            lista.append({'char':key,'num':dict[key]})
    return lista

def printReport(lista):
    print("--- Begin report of books/frankenstein.txt ---")
    for l in lista:
        print(f"The '{l['char']}' character was found {l['num']} times")
    print("--- End report ---")
    
def main():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        print(countWords(file_contents))
        lista = dictToList(countChars(file_contents))
        lista.sort(reverse=True, key=lambda x: x['num'])
        printReport(lista)
main()