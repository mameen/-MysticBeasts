#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import threading

def run_process(command):
    """ Function to run shell commands and return the process handle """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line.decode().strip())
    return process

def main():
    # Define the commands to run your backend and frontend
    backend_command = 'uvicorn backend.main:app --reload'
    frontend_command = 'python frontend/chat_interface.py'  # Adjust based on your Gradio setup

    # Start backend and frontend processes
    backend_process = run_process(backend_command)
    frontend_process = run_process(frontend_command)

    print("Application started. Press 'q' to quit.")
    while True:
        if input() == 'q':
            print("Shutting down...")
            # Terminate processes
            backend_process.terminate()
            frontend_process.terminate()
            break

    backend_process.wait()
    frontend_process.wait()
    print("Application has been terminated.")

if __name__ == "__main__":
    main()
