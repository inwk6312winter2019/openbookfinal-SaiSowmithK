def unique_words(file):
        opened_file = open(file, 'r')
        allWords = [line.split(',') for line in opened_file.readlines()]
        unique_list = list() 
        for i in allWords:
                if i in unique_list:
                        pass
                else:
                        unique_list.append(i);
        return tuple(unique_list)
print(unique_words("book1.txt"))
print(unique_words("book2.txt"))
print(unique_words("book3.txt"))
