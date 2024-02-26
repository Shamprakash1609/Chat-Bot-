import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Great marketer ."},
    {"role": "user", "content": "write a slogan for lamborghini Hypercar"}
  ],
  max_tokens = 30,
  temperature = 1.9 # vary b/w 0 to 2 for diffrent outputs
  )

print(completion.choices[0].message)
