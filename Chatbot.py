import openai

openai.api_key = "api_key"

while (True):
    msg = input("ME : ")

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", # specifies the model to use for the chat completion
        messages = [{"role": "system", "content": msg}],
        #max_tokens = 1,# maximum number of tokens in the response.
        temperature = 1, # controls the randomness of the model's output 0.8 more random ,0.2 make it more focused
        n = 2, #determines the number of completions to generate
    )

    chat_response = completion.choices[0].message.content
    print(completion)
    print("GPT : ",chat_response)
