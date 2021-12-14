def translator(str):
    transation =""
    for letter in str:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transation = transation + "Z"
            else:
                transation = transation + "z"
        else:
            transation = transation +letter
    return transation

print(translator(input('enter a phrase : ')))                        

