while True:
    user_input = input("Type 'exit' to quit the program: ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program...")
        exit()
    else:
        print(f"You typed: {user_input}. Try again.")
