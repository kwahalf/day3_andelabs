#function that returns a maximum and a min value in a given list
def find_max_min(x):
	max_min = []
	#case for list not being empty and list not having the same value
	if x!= [] and (max(x) != min(x)):
		max_value = max(x)
		min_value = min(x)
		max_min.append(min_value)
		max_min.append(max_value)
		return (max_min)
	    #case for list not being empty and list having the same value
	elif x!= [] and (max(x) == min(x)):
		z = [len(x)]
		#returns a list of one value
		return z
print find_max_min([4,4,4,4])






