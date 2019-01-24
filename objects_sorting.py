type1 = [0,0,0]
type2 = [0,0,0]
fault = [0]
process = []
j = 0
while(j<5):
	i = input("Type\n")
	process.append(i)
	i = input("weight\n")
	process.append(i)
	i = input("color\n")
	process.append(i)

	# checkinig for type
	if process[0] == "nm":
		if process[1] == "w2":
			if process[2] == "red":
				type2[0] += 1
			elif process[2] == "green":
				type2[1] += 1
			elif process[2] == "blue":
				type2[2] += 1
			else:
				fault[0] += 1
		elif process[1] == "w1":
			if process[2] == "red":
				type1[0] += 1
			elif process[2] == "green":
				type1[1] += 1
			elif process[2] == "blue":
				type1[2] += 1
			else:
				fault[0] += 1
		else:
			fault[0] += 1
	else:
		fault[0] += 1

	j += 1
	process = []

print(type1)
print(type2)
print(fault)