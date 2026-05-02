from config import MODEL_PROVIDER
from gemini_client import ask_gemini
from openai_client import ask_openai

print("🤖 Multi-Model Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        if MODEL_PROVIDER == "gemini":
            reply = ask_gemini(user_input)
        else:
            reply = ask_openai(user_input)

        print("\nAI:", reply, "\n")

    except Exception as e:
        print("Error:", e)
