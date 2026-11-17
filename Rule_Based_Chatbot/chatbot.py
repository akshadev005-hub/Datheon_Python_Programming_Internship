
import json
import os
import re


# Load FAQ dataset
def load_faq():

    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "faq.json"
    )

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("Error: faq.json file not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None


# Normalize user input
def normalize_input(message):

    message = message.lower().strip()

    message = re.sub(r"[^\w\s]", " ", message)

    message = re.sub(r"\s+", " ", message)

    return message


# Check greetings
def check_greeting(message, greetings):

    for greeting in greetings:

        pattern = r"\b" + re.escape(greeting) + r"\b"

        if re.search(pattern, message):
            return True

    return False


# Identify matching FAQs
def identify_intents(message, faqs):

    matched_answers = []

    for faq in faqs:

        question = normalize_input(faq["question"])

        # Extract keywords from FAQ question
        keywords = [
            word for word in question.split()
            if len(word) > 2
        ]

        # Match relevant keywords
        match_count = sum(
            1 for word in keywords
            if re.search(r"\b" + re.escape(word) + r"\b", message)
        )

        # Require at least two matching keywords
        if match_count >= 2:

            matched_answers.append(faq["answer"])

    return matched_answers


# Generate chatbot response
def chatbot_response(message, data):

    message = normalize_input(message)

    if not message:
        return "Please enter a question."

    # Greeting detection
    if check_greeting(message, data["greetings"]):
        return (
            "Hello! Welcome to Datheon Customer Support. "
            "How can I help you today?"
        )

    # FAQ matching
    answers = identify_intents(message, data["faqs"])

    if answers:

        if len(answers) == 1:
            return answers[0]

        return "\n".join(
            f"{index}. {answer}"
            for index, answer in enumerate(answers, start=1)
        )

    # Fallback response
    return (
        "Sorry, I couldn't understand your question. "
        "You can ask me about business hours, internship "
        "project submission, or certificate details."
    )


# Main chatbot function
def main():

    print("\n" + "=" * 55)
    print("          DATHEON CUSTOMER SUPPORT CHATBOT")
    print("=" * 55)

    print("\nBot: Hello! Welcome to Datheon Support.")
    print("Bot: How can I help you today?")
    print("Bot: Type 'bye', 'exit', or 'quit' to end the chat.")

    data = load_faq()

    if data is None:
        return

    if not isinstance(data.get("greetings"), list) or not isinstance(data.get("faqs"), list):
        print("Error: Invalid FAQ dataset structure.")
        return

    # Conversational loop
    while True:

        try:
            user_input = input("\nYou: ")

            message = normalize_input(user_input)

            # Exit commands
            if re.fullmatch(r"(bye|goodbye|exit|quit)", message):
                print("\nBot: Thank you for contacting Datheon!")
                print("Bot: Have a great day!")
                break

            # Generate response
            response = chatbot_response(user_input, data)

            print("\nBot:", response)

        except KeyboardInterrupt:
            print("\n\nBot: Chat ended. Goodbye!")
            break

        except (KeyError, TypeError):
            print("\nBot: There is an issue with the FAQ dataset.")
            break

        except Exception as error:
            print("\nBot: Something went wrong. Please try again.")
            print("Error:", error)


# Execute program
if __name__ == "__main__":
    main()
