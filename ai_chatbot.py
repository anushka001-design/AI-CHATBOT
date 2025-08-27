import tkinter as tk
from tkinter import scrolledtext
import openai

# ✅ Create OpenAI client with your API key
client = openai.OpenAI(api_key="AIzaSyCjWCz1Hk7Shyk0Z-ZQU1MOdCOsMFGlOTM")

# Get AI response using the client
def get_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use gpt-4 if your key supports it
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Send message and update GUI
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
    entry.delete(0, tk.END)

    response = get_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n", "bot")

# Setup GUI
root = tk.Tk()
root.title("AI Chatbot (OpenAI v1.97.1)")
root.geometry("500x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry = tk.Entry(root, width=80)
entry.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

root.mainloop()
