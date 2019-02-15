def count_the_article(l):
	mylist=["a","the","at","run","to","and","or","for","an","this"]
	c=0
	for word in l:
		if word in mylist:
			c=c+1
		else:
			
