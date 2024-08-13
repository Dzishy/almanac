

# userInput = input('type your text\n')
# usersSymbol = input('input a symbol you want to count in your text\n')



# textStroke = list(userInput)
# symbolList = []
# for usersSymbol in textStroke:
#     symbolList.append(usersSymbol)
        
# print (f'Amount of the symbol "{usersSymbol}" in your text is: ', len(symbolList))


#Alex's method
    #inputString = "hello"
    #inputSymbol = "l"
    #result = 0
    #for i in range (len(inputString)):
    #    s = inputString[i]
    #    if s == inputSymbol:
    #       result+=1
    #print (result)     
    
text = input('type your text\n')
symbol = input('input a symbol you want to count in your text\n')
text = text.lower()
symbolCount = text.count(symbol)
                         
print (f'Amount of the symbol "{symbol}" in your text is: {symbolCount}')