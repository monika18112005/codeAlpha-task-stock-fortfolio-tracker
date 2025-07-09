def z():  # Function named z
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:  # Loop for continuous chat
        user_input = input("You: ").lower()
        
        if user_input == "hello":
            print("Chatbot: hi")
        elif user_input == "how are you":
            print("Chatbot: I am fine")
        elif user_input == "thanks":
            print("Chatbot: You're welcome!")
        elif user_input == "bye":
            print("Chatbot: goodbye")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")

# Call the function to start the chatbot
z()
