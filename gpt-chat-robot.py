import gradio as gr
import openai
import random
import time

# Set up OpenAI API key
API_KEY = "your api key"
openai.api_key = API_KEY

system_message = {"role": "system", "content": "You are my AI assistant."}

with gr.Blocks(title="ChatGpt") as gpt:
    chatbot = gr.Chatbot(label="ChatGpt聊天区")
    clear = gr.Button("清空聊天")
    msg = gr.Textbox(label="输入问题<回车发送>", placeholder="Type here...")
    state = gr.State([])

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history, messages_history):
        user_message = history[-1][0]
        bot_message, messages_history = ask_gpt(user_message, messages_history)
        messages_history += [{"role": "assistant", "content": bot_message}]
        history[-1][1] = bot_message
        time.sleep(1)
        return history, messages_history

    def ask_gpt(message, messages_history):
        messages_history += [{"role": "user", "content": message}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_history
        )
        return response['choices'][0]['message']['content'], messages_history

    def init_history(messages_history):
        messages_history = []
        messages_history += [system_message]
        return messages_history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, [chatbot, state], [chatbot, state])

    clear.click(lambda: None, None, chatbot, queue=False).success(init_history, [state], [state])


if __name__ == '__main__':
    gpt.launch(share=True)
