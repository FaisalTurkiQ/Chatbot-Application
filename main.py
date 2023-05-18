from tkinter import *
import openai

def toChatGPT(message):
    openai.api_key = "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"
    messages = [{"role": "system", "content": message}]
    #messages.append({"role": "system", "content": "You are an teacher"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = completion.choices[0].message.content
    print(wrap_text(chat_response))
    return wrap_text(chat_response)


def wrap_text(text, wrap_length=40):
    lines = []
    words = text.split()
    current_line = ""

    for word in words:
        if len(current_line + word) > wrap_length:
            lines.append(current_line)
            current_line = ""
        current_line += word + " "

    lines.append(current_line)  # Add the last line

    return "\n".join(lines)


class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self.window.title("Chatbot Application")

        # Create listbox to display messages
        self.message_listbox = Listbox(self.window, font=("Arial", 24))
        self.message_listbox.pack(side="top", fill="both", expand=True)
        # Create scrollbar for the listbox
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")
        self.message_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.message_listbox.yview)

        # Create input field and send button
        self.input_entry = Entry(self.window)
        self.input_entry.pack(side="left", fill="x", expand=True)
        self.input_entry.bind("<Return>", self.send_message)
        self.send_button = Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(side="right")

    def send_message(self,event):
        message = self.input_entry.get()
        if message:
            self.message_listbox.insert(END, "You: " + message)
            self.input_entry.delete(0, END)
            L=  ("ChatGPT: "+toChatGPT(message)).split("\n")
            for x in L:
                self.message_listbox.insert(END, x)
        else:
            messagebox.showwarning("Empty Message", "Please enter a message.")


    def run(self):
        self.window.mainloop()


# Instantiate the chat application and run it
app = ChatApplication()
app.run()
