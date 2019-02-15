from collections import Counter
def top_20(file):
        d = dict()
        opened_file = open(file, 'r')
        allWords = [line.split(',') for line in opened_file.readlines()]
        c = Counter(allWords)
        for w, count in c.most_common(20):
                d[w] =  count
        return d
print(top_20("book1.txt"))
print(top_20("book2.txt"))
print(top_20("book3.txt"))
