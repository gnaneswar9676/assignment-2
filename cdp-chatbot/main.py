from chatbot import CDPChatbot

def main():
    chatbot = CDPChatbot()
    print("Welcome to the CDP Chatbot!")
    print("Ask me 'how-to' questions or comparisons about Segment, mParticle, Lytics, or Zeotap.")
    print("Type 'exit' to quit.")
    while True:
        question = input("> ")
        if question.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot.process_question(question)
        print(response)

if __name__ == "__main__":
    main()