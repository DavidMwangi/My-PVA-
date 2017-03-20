import wikipedia

print ("What is your preferred language? Below are some choices: ")

print ("1. Type en for English\n2. Type es for Spanish\n3. Type fr for French\n4. Type zh for Chinese\n5. Type de for German")

lang = str(input("Enter choice: "))

while True:
    
    user_input = input ("\nAsk  me a question: ")
    
    wikipedia.set_lang(lang)
    
    print (wikipedia.summary(user_input))
