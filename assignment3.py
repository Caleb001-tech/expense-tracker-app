print("Welcome to my sentence analyser")
sentence = input("Enter a sentence: ")
lower = sentence.lower()
print(lower)
counted = sentence.count('a')
print("The number of a is", counted)
if "python" in sentence:
    print("sentence contains python")
else:
    print("sentence does not contain python")
print("The first word is", sentence.strip()[0])
print("The last word is", sentence.strip()[-1])
convert = sentence.split()
middle = convert[1:-1]
final = " ".join(middle)
print("the middle word is", final)