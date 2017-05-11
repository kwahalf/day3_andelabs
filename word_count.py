import collections
# defines the function that will convert string element in the list to integers
def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x
# define the functon the number of occurance of a word in a sentence 
#and retuns a dictionary containing the word as the index and the numebr 
#of occurance as value
def words(x):
	word_count = dict()
	sentence = x.split()
	# converts all integers 1, 2, 3... written as string back to integers
	sentence =[try_int(x) for x in sentence]
	for x in sentence:
		if x in word_count:
			word_count[x]+= 1
		else:
			word_count[x]= 1
	return (word_count)





