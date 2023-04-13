import openai

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

API_KEY = "your api key"

openai.api_key = API_KEY


def start():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "who are you"}])
    print(completion.choices[0].message.content)


if __name__ == '__main__':
    start()


