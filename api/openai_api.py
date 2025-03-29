# from openai import OpenAI
#
# from settings import OPENAI_API_KEY
#
# client = OpenAI(api_key=OPENAI_API_KEY)
#
#
# def ask_chatgpt(prompt: str) -> str:
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "developer",
#              "content": "you are my friend, communicate like the best friend, joke, ask strange questions"},
#             {"role": "user", "content": prompt}
#         ]
#     )
#
#     return completion.choices[0].message.content
