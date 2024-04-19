from g4f.client import Client

def answerGPT(promt):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
        stream=True
    )

    full_text = "" 
    for chunk in response:
        if chunk.choices[0].delta.content:
            full_text += chunk.choices[0].delta.content 
    return full_text