import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(query):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a great assistant."},
        {"role": "user", "content": query}
    ],
    #max_tokens = 30,
    temperature = 0.4 # vary b/w 0 to 2 for diffrent outputs
    )

    return completion.choices[0].message["content"]
