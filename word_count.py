import collections
def words(x):
	word_count = dict()
	sentence = x.split()
	for x in sentence:
		if x in word_count:
			word_count[x]+= 1
		else:
			word_count[x]= 1
	return (word_count)
print (words("haa boo 4 6"))




