#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gradio as gr
from chat_interface import chat_interface
from left_pane import left_pane
from right_pane import right_pane

def main():
    with gr.Blocks() as app:
        with gr.Row():
            with gr.Column(scale=1):
                left_pane()
            with gr.Column(scale=3):
                chat_interface()
            with gr.Column(scale=1):
                right_pane()

    app.launch()

if __name__ == "__main__":
    main()
