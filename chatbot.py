import re

def chatbot():
    print("Chatbot: Hello! How can I help you today? (Type 'exit' to quit)")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        elif re.search(r"hello|hi|hey", user_input):
            print("Chatbot: Hi there! How can I assist you?")
        
        elif re.search(r"how are you", user_input):
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        
        elif re.search(r"your name", user_input):
            print("Chatbot: I’m your assistant chatbot.")
        
        elif re.search(r"time", user_input):
            from datetime import datetime
            print(f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}")
        
        else:
            print("Chatbot: Sorry, I don’t understand.")

chatbot()
