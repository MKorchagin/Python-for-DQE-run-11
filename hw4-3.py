#Function for fixing gram.errors
def replaces(fix,text_repl):
    for what, to_what in text_repl.items():
        fix = fix.replace(what, to_what)
    return fix

#Function for formatting the text
def capitalizing (text):
    li = list (text)
    for i in range(len(li)-1):
        if li[i]==".":
            li[i+2] = li[i+2].upper()
        elif li[i]== "\n":
            li [i+1] = li[i+1].upper()
        elif li[i]==li[0]:
            li[i]=li[i].upper()
    fin = ''.join(li)
    return fin

#Function for gathering new sentence.
def create_sentence_from_last_words(text):
    last_words = []

    sentences = text.split(".")
    sentences.pop()
    for sentence in sentences:
        last_word = sentence.split()[-1]
        last_words.append(last_word)

    return (" ".join(last_words) + ".").capitalize()


#Execution
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

#Reducing the text to a lower form
norm = original_text.lower()
#print(norm)

#Create dict with changed, where item - what we change, value - to what we change
text_repl = {"\n": "", "  ": "\n", "iz ": "is ", "tex.": "text.", "x“iz": "x “iz" }

# creating function replaces: we get some test (names fix text) and provide changes that are mentioned in dict "text repl"
fix_text = replaces(norm, text_repl)
#print(fix_text)

#new sentence = opening of list "last_sentence"
new_sentence = create_sentence_from_last_words(fix_text)
#print(new_sentence)


#Final gathering of homework:
print(capitalizing(fix_text), '\n')
print(capitalizing(new_sentence), '\n', '\n',)
print( "The number of whitespaces - ", spaces, '\n')
