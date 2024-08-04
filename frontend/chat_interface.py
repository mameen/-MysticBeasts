#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gradio as gr

def chat_interface():
    def send_message(message):
        return f"You said: {message}"

    with gr.Blocks() as chat_app:
        output_text = gr.Textbox(label="Conversation", lines=10, interactive=False)
        input_text = gr.Textbox(show_label=False)
        submit_button = gr.Button("Send")
        submit_button.click(fn=send_message, inputs=input_text, outputs=output_text)

    return chat_app

