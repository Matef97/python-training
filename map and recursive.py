def cleanText(text) :
    if len(text) == 1 :
        return text
    if text[0]==text[1] :
        return  cleanText(text[1:])  
    return  text[0]+cleanText(text[1:])     

names = ["mmmmmmmmmmmooooooooooooossssssssssssstttttttttttaaaaaaaffffffaaaaa","mmmmmooooooonnnnnnaaaaaa","aahhhhhmeedddd"]  
format = map(cleanText,names)  
# print(format)
for i in format :
    print(i.capitalize())
    