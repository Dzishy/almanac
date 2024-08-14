
#1
words = ['sugar', 'flour', 'rice', 'milk', 'water', 'juice', 'salt', 'pepper']
sortedWords = sorted(words, key=lambda word: (len(word), word))
print (sortedWords)


#2
numbers = [1, 6, 8, 12, 15, 22, 24, 30, 35, 42]
newNumbers = filter(lambda number: number%2 == 0 and number%3 == 0, numbers)
print (list(newNumbers))


#3
words = ['sugar', 'flour', 'rice', 'milk', 'water', 'juice', 'salt', 'pepper']
newWords = map(lambda word: word.upper(), words)
print (list(newWords))


#4
letters = ['a', 'o', 'u', 'e', 'i']
otherWords = ["apple", "banana", "grape", "kiwi", "orange", "blueberry"]
newOtherWords = max(otherWords, key=lambda word: sum(word.count(letter)for letter in letters))
print (newOtherWords)