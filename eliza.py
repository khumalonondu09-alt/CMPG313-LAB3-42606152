import re
import random

RULES = [
    (
        r"hello|hi|hey|good morning|good afternoon",
        [
            "Hello! How are you feeling today?",
            "Hi there! What's on your mind?",
            "Hey! How can I help you today?",
        ]
    ),
    (
        r"my name is (.+)",
        [
            "Hello, {0}! It's nice to meet you. How are you feeling?",
            "Hi {0}! What brings you here today?",
            "Nice to meet you, {0}. What would you like to talk about?",
        ]
    ),
    (
        r"i feel (stressed|anxious|overwhelmed|nervous)",
        [
            "I'm sorry to hear you feel {0}. What do you think is causing that?",
            "Feeling {0} can be tough. Would you like to talk about what's going on?",
            "Why do you think you feel {0}?",
        ]
    ),
    (
        r"i am (tired|exhausted|sleepy|drained)",
        [
            "Why do you think you are {0}?",
            "It sounds like you need some rest. What's been keeping you so {0}?",
            "Being {0} can affect everything. What's been going on lately?",
        ]
    ),
    (
        r"because (.+)",
        [
            "Is that the real reason — {0}?",
            "Does it always come down to {0}?",
            "That's interesting. How does {0} make you feel?",
        ]
    ),
    (
        r"my (mother|father|brother|sister|parent|family) is (.+)",
        [
            "Tell me more about your {0}.",
            "How does it make you feel that your {0} is {1}?",
            "Has your {0} always been {1}?",
        ]
    ),
    (
        r"i need (.+)",
        [
            "Why do you need {0}?",
            "Would getting {0} really help you?",
            "What would change if you had {0}?",
        ]
    ),
    (
        r"i think (.+)",
        [
            "Do you really think {0}?",
            "Why do you believe {0}?",
            "What makes you say {0}?",
        ]
    ),
    (
        r"i want (.+)",
        [
            "What would it mean to you if you got {0}?",
            "Why do you want {0}?",
            "If you had {0}, how would things be different?",
        ]
    ),
    (
        r"quit|bye|goodbye|exit",
        [
            "Goodbye! Take care of yourself.",
            "It was nice talking to you. Farewell!",
            "Bye! I hope our conversation was helpful.",
        ]
    ),
    (
        r"^yes$|^yeah$|^yep$|^sure$",
        [
            "You seem quite certain. Can you elaborate?",
            "Are you sure about that?",
            "I see. Tell me more.",
        ]
    ),
    (
        r"^no$|^nope$|^not really$",
        [
            "Why not?",
            "Are you sure?",
            "That's interesting. Can you explain?",
        ]
    ),
]

FALLBACKS = [
    "I see. Tell me more.",
    "That's interesting. Please continue.",
    "Can you elaborate on that?",
    "How does that make you feel?",
    "Why do you say that?",
    "I'm not sure I understand. Could you rephrase?",
]


def get_eliza_response(user_input: str) -> str:
    text = user_input.strip().lower()
    for pattern, responses in RULES:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            for i, group in enumerate(match.groups()):
                response = response.replace(f"{{{i}}}", group if group else "")
            return response
    return random.choice(FALLBACKS)


if __name__ == "__main__":
    print("=" * 50)
    print("  ELIZA - Rule-Based Chatbot (Custom Version)")
    print("=" * 50)
    print("Type 'quit' to stop.\n")
    while True:
        user = input("You: ").strip()
        if not user:
            continue
        response = get_eliza_response(user)
        print(f"ELIZA: {response}\n")
        if re.search(r"quit|bye|goodbye|exit", user, re.IGNORECASE):
            break
