
def starts_with_vow(file):
        opened_file = open(file, 'r')
        allWords = [line.split(',') for line in opened_file.readlines()]
        vowel_count = {"a":0,"e":0,"i":0,"o":0,"u":0} 
        vowel_list = ["a","e","i","o","u"]
        for i in allWords:
                for vow in vowel_list:
                        if i[0] ==vow:
                                vowel_count[vow] = vowel_count[vow] + 1
                                break
        return vowel_count
print(starts_with_vow("book1.txt"))
print(starts_with_vow("book2.txt"))
print(starts_with_vow("book3.txt"))
