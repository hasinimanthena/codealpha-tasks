# chatbot function
def chatbot():

    print("Simple Chatbot")
    print("Type 'bye' to stop the chat")

    while True:

        # user input
        user = input("You: ").lower()

        # chatbot replies
        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a simple chatbot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

# function call
chatbot()