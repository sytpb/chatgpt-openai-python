import openai
import gradio
#from transformers import pipeline

API_KEY = "your api key"
openai.api_key = API_KEY

#generator = pipeline('text-generation', model='gpt-3.5-turbo')
messages = [{"role": "system", "content": "You are my chat robot"}]

def generate(input):
    messages.append({"role": "user", "content": input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

# demo = gradio.Interface(
#     fn=generate,
#     inputs=gradio.inputs.Textbox(lines=5, label="Input Text"),
#     outputs=gradio.outputs.Textbox(label="Generated Text")
# )

def start():
    with gradio.Blocks() as demo:
        inputbox = gradio.Textbox(label="输入问题", placeholder="Type here...", lines=3)
        btnClear = gradio.Button("清空")
        btnSubmit = gradio.Button("提交")
        outputbox = gradio.Textbox(label="ChatGpt的回答", placeholder="", lines=5)
        
        
        # define what will run when the button is clicked, here the textbox is used as both an input and an output
        btnClear.click(lambda x: gradio.update(value=''), [],[inputbox])
        inputbox.submit(lambda x: gradio.update(value=''), [],[inputbox])

        btnSubmit.click(fn=generate, inputs=inputbox, outputs=outputbox, queue=False)

    demo.launch(share=True)

if __name__ == '__main__':
    start()