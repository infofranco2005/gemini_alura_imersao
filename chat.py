from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv() #carrega as variaveis do arquivo .env
apikey = os.getenv("APIKEY")
client = genai.Client(api_key=apikey)
chat = client.chats.create(model="gemini-2.0-flash")

instrucao = input("Olá fala ai mano :) ")
print(instrucao)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction=instrucao),
    contents="Hello there"
)



# instrucao1 = input("Coloque a sua ideia neste campo que resolvemos para voce ")
response = chat.send_message_stream(instrucao)
for chunk in response:
     print(chunk.text, end="sim")

# instrucao2 = input("Coloque a sua ideia neste campo que resolvemos para voce ")
# response = chat.send_message_stream(instrucao2)
# for chunk in response:
#      print(chunk.text, end="")

# for message in chat.get_history():
#      print(f'role - {message.role}', end=": ")
#      print(message.parts[0].text)