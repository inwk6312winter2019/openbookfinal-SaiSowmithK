def count_the_article():
	reserve = []
	f = open('Book1.txt', 'r')
	w = f.readlines()

	for line in w:
		res = line.lower().strip(string.punctuation + string.whitespace).split()
		reserve = reserve + res

	count = {}
        for count, word in w:
		print(word + " : " + str(concat))

	print("Words " + str(total) + "\n" + "Different words: " + str(diff_word) + "\n" + "Vocab ratio: " + str(vocab))

count_the_article()
