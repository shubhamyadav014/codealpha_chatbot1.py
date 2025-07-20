def chatbot():
    print("Hello! I'm your chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hi" or user_input == "hello":
            print("Bot: Hello! How can I help you?")
        elif user_input == "how are you":
            print("Bot: I'm just a bot, but I'm doing great! Thanks.")
        elif user_input == "exit":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()



