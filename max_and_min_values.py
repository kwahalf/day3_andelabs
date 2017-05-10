def find_max_min(x):
	max_min = []
	if x!= [] and (max(x) != min(x)):
		max_value = max(x)
		min_value = min(x)
		max_min.append(min_value)
		max_min.append(max_value)
		return (max_min)
	elif x!= [] and (max(x) == min(x)):
		z = [len(x)]
		return z
print find_max_min([4,4,4,4])






