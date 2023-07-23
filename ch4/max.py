def maximum_number(list):
	if len(list) == 1:
		return list[0]
	if len(list) == 2:
		return list[0] if list[0] > list[1] else list[1]
	max = maximum_number(list[1:])
	return list[0] if list[0] > max else max

print(maximum_number([1, 5, 6, 13, 7]))
