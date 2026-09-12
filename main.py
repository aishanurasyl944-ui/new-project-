def ai_assistant(text):
    text = text.lower()

    if "сәлем" in text:
        return "Сәлем! Қалай көмектесе аламын?"
    elif "қалайсың" in text:
        return "Жақсымын, рақмет!"
    elif "ai" in text:
        return "AI — жасанды интеллект."
    else:
        return "Кешіріңіз, сұрағыңызды түсінбедім."


print("AI Assistant")
question = input("Сұрақ: ")

print("AI:", ai_assistant(question))