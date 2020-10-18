def printAllCombinations(pattern, i=0):

	if i == len(pattern):
		print(''.join(pattern), end =" ")
		return

	# if the current character is '?'
	if pattern[i] == '?':
		for ch in "01":

			# replace '?' with 0 and 1
			pattern[i] = ch

			# recur for the remaining pattern
			printAllCombinations(pattern, i + 1)

			# backtrack
			pattern[i] = '?'

	else:
		printAllCombinations(pattern, i + 1)

a = int(input())

#pattern = "1?11?00?1?"
pattern = input()
printAllCombinations(list(pattern))
