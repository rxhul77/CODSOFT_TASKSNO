def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]:
        return "Hello! 👋 How can I help you today?"

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking. 😊"

    # Name / identity
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a rule-based chatbot created using Python."

    # Help
    elif user_input in ["help", "what can you do"]:
        return (
            "I can respond to greetings, tell you about myself, "
            "answer simple questions about Python and AI, and say goodbye."
        )

    # Python
    elif "python" in user_input:
        return (
            "Python is a popular programming language used for "
            "AI, data science, web development, and automation."
        )

    # Artificial Intelligence
    elif "artificial intelligence" in user_input or user_input == "ai":
        return (
            "Artificial Intelligence enables computers to perform "
            "tasks that normally require human intelligence."
        )

    # Internship
    elif "codsoft" in user_input or "internship" in user_input:
        return "This chatbot is developed as part of the CodSoft Artificial Intelligence Internship."

    # Thanks
    elif "thank" in user_input:
        return "You're welcome! 😊 Happy to help."

    # Goodbye
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"

    # Empty input
    elif not user_input:
        return "Please type something so I can respond."

    # Unknown input
    else:
        return (
            "I'm sorry, I don't understand that. "
            "Try typing 'help' to see what I can do."
        )


def main():
    print("=" * 55)
    print("             RULE-BASED CHATBOT")
    print("=" * 55)
    print("Type 'help' to see available topics.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print()

    while True:
        user_input = input("You: ")

        response = get_response(user_input)

        print("Bot:", response)
        print()

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()