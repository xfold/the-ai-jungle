from src.cv_gpt import CVGPT as cvgpt
import warnings

# Suppress specific UserWarning related to ChatVectorDBChain
warnings.simplefilter("ignore", category=UserWarning)


# config
# Also make sure you have an OPEN_API_KEY set!
pdf_path = "data/08.23 resume.pdf"
model_name = "gpt-3.5-turbo"
temperature = 0.9
cv_gpt = cvgpt(pdf_path, model_name, temperature)

# Start the chat loop
while True:
    user_input = input("You: ")
    
    # Check if the user wants to leave the chat
    if user_input.lower() == "leave":
        print("Exiting the chat. Goodbye!")
        break
    
    # Query the CVGPT model with the user's input
    response = cv_gpt.query_cvgpt(user_input)
    
    # Print the response from CVGPT
    print("CVGPT:", response)