import openai
from textblob import TextBlob
import random

openai.api_key = ''

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.2:
        return 'positive'
    elif sentiment_score < -0.2:
        return 'negative'
    else:
        return 'neutral'

def psychological_response(sentiment):
    if sentiment == 'positive':
        return random.choice(["That's great!", "I'm glad to hear that.", "You seem to be in a good mood."])
    elif sentiment == 'negative':
        return random.choice(["I'm sorry to hear that.", "That sounds tough.", "Do you want to talk more about it?"])
    else:
        return random.choice(["Interesting.", "Tell me more.", "I see."])


def ask_openai(user, question, chat_log=None):
    if chat_log is None:
        chat_log = "The following is a conversation between two users:\n\n"

    prompt = f"{chat_log}User {user}: {question}\nUser {3 - user}:"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are User {3 - user}."},
            {"role": "user", "content": question},
        ],
        max_tokens=150,
    )

    ai_response = completion.choices[0].message['content']

    user_sentiment = analyze_sentiment(question)
    ai_sentiment = analyze_sentiment(ai_response)

    psychological_response_user = psychological_response(user_sentiment)
    psychological_response_ai = psychological_response(ai_sentiment)

    chat_log += f"User {user}: {question}\nUser {3 - user}: {ai_response} ({ai_sentiment} sentiment)\n"

    return ai_response, chat_log, psychological_response_user, psychological_response_ai

chat_log = None
user = 1
# while True:
#     user_input = input(f"User {user}: ")
#     if user_input.lower() == 'exit':
#         print("Exiting...")
#         break
#     response, chat_log, psychological_response_user, psychological_response_ai = ask_openai(user, user_input, chat_log)
#     print(f"User {user}:", response)
#     print(f"User {user} Psychological Response:", psychological_response_user)
#     print(f"User {3 - user} Psychological Response:", psychological_response_ai)
#     user = 3 - user