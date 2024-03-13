def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking!"
    
    elif "what's up?" in user_input:
        return "Not much,Just chatting with you"
    
    elif "Who made you?" in user_input:
        return "oh,I was created by a team"
    

    elif "bye" in user_input:
        return "Goodbye! Have a great day."

    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome!"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Main loop for chatting
print("Welcome! How can I assist you today?")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if "bye" in user_input:
        break