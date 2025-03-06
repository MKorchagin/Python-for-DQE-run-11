original_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

#print ('original_text: ','\n',original_text)

#Calculating whitespaces:
spaces = sum(i.isspace () for i in original_text)
# print("The number of whitespaces - ", spaces, '\n')


#Use capitalize operator for reducing the text to a single letter form
norm = original_text.capitalize()
#print(norm)


#Create dict with changed, where item - what we change, value - to what we change
text_repl = {"\n": "", "  ": "\n", "iz ": "is ", "tex.": "text.", "x“iz": "x “iz" }

# creating function replaces: we get some test (names fix text) and provide changes that are mentioned in dict "text repl"
def replaces(fix,text_repl):
    for what, to_what in text_repl.items():
        fix = fix.replace(what, to_what)
    return fix
fix_text = replaces(norm, text_repl)
#print(fix_text)

#Creating new sentence, using last words
last_sentence = []

a = fix_text.split('.')
a.pop()
for word in a:
    w = word.split()[-1]
    last_sentence.append(w)

#new sentence = opening of list "last_sentence"
new_sentence = ' '.join(last_sentence) + "."
#print(new_sentence)


#insertinh capital letters:
def capitalizing (text):
    li = list (text)
    for i in range(len(li)-1):
        if li[i]==".":
            li[i+2] = li[i+2].upper()
        elif li[i]== "\n":
            li [i+1] = li[i+1].upper()
    fin = ''.join(li)
    return fin

#Final gathering of homework:
print ("The number of whitespaces - ", spaces, '\n')
print(capitalizing(fix_text), '\n')
print(new_sentence.capitalize())
