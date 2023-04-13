import openai
import gradio

API_KEY = "your api key"
openai.api_key = API_KEY

messages = [{"role": "system", "content": "You are my chat robot"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

#demo = gradio.Interface(fn=CustomChatGPT, inputs = "text",label = "提问", outputs = "text", title = "My chatGpt")

demo = gradio.Interface(
    fn=CustomChatGPT,
    inputs=gradio.Textbox(lines=3, label="输入问题"),
    outputs=gradio.Textbox(lines=5, label="ChatGpt的回答"))

demo.launch(share=True)