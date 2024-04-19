from g4f.client import Client

def answerGPT(promt:str)->str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
    )
    print(response.choices[0].message.content)