
import gradio as gr


def infra(x):
    print("sample printing...........")
    print(x)
    # my_dict={"abc":"456"}
    return str(x)

def combine(a, b):
    return a + " " + b

with gr.Blocks() as demo:
    gr.Markdown("You can use first tab for select default and other for receiving custom config.")

    with gr.Tab("Default Config"):
        text_input = gr.Dropdown(["bert", "gpt", "etc"])
        text_output = gr.Textbox(value="", label="Output")
        text_button = gr.Button("Recommend")
    #     txt = gr.Textbox(label="Input", lines=2)
    #     txt_2 = gr.Textbox(label="Input 2")
    #     txt_3 = gr.Textbox(value="", label="Output")
    #     btn = gr.Button(value="Submit")
    # btn.click(combine, inputs=[txt, txt_2], outputs=[txt_3])
    with gr.Tab("Custom Config"):
        with gr.Row():
            image_input = gr.Image()
            print(image_input)
            image_output = gr.Image()
        image_button = gr.Button("Flip")

    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")

    text_button.click(infra, inputs=[text_input], outputs=[text_output])


demo.launch()
