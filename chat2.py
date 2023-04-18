import os
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "user",
                                                     "content": "Write an essay about Barbados using 30 characters, sounding like a bajan, that even a child can understand"}])
print(response.choices[0].message.content)