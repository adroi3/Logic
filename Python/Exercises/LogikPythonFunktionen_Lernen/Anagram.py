def anagram(word):
	if(len(word) <= 1):
		return {word}

	char = word[0]
	newWord = word[1:]
	
	subAna = anagram(newWord)
	anas = {w[:x] + char + w[x:] for w in subAna for x in range(len(w)+1)}
	return anas
	
ana = anagram("eta")

print(ana)
print(len(ana))
