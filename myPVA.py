import wolframalpha
import wikipedia

while True:
    

    userInput = input("Ask me a question: ")

    try:
        

        app_id = "W496W7-7W9WWWTAGR"

        client = wolframalpha.Client(app_id)

        result = client.query(userInput)

        answer = next(result.results).text

        print (answer)

    except:

        print (wikipedia.summary(userInput))
