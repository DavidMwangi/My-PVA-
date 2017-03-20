import wikipedia

while True:
    
    user_input = input ("Ask  me a question: ")

    print (wikipedia.summary(user_input))
