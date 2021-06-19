
sentence = input("Enter a sentence : ")
finding = input("Enter the word : ")
number = sentence.count(finding)
print(sentence, "%s is used  %d times in the sentence" % (finding, number))
dlt = sentence.replace(finding, "")
print() 
print(sentence, "New sentence(removed %s) :\n\t%s" % (finding, dlt))

