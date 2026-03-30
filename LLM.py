from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

def get_llm_response(user_input: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Reply in 2 sentences max."},
        {"role": "user", "content": user_input}
    ]

    response = chatbot(
        messages,
        max_new_tokens=50
    )

    return response[0]["generated_text"][-1]["content"].strip()

if __name__ == "__main__":
    print("Modern AI Chatbot")
    print("Type 'quit' to stop.\n")

    while True:
        user = input("You: ")

        if user.lower() == "quit":
            print("Bot: Goodbye!")
            break

        print("Bot:", get_llm_response(user))
