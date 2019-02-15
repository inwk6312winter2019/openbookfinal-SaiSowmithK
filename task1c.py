import string

def sorted_words():
 
 reserve = []
        f = open('Book1.txt', 'r')
        w = f.readlines()

        for line in w:
                res = line.lower().strip(string.punctuation + string.whitespace$
                reserve = reserve + res

        words = my_str.split()
        words.sort()
        print("The sorted words are:")
        for word in w:
sorted_words(word)
