import os, requests, json
from dotenv import load_dotenv

load_dotenv()

class Chatbot:
    def __init__(self):
        self.APIKEY = os.getenv('KEY')
        self.headers = {"Authorization": f"Bearer {self.APIKEY}", "Content-Type": "application/json"}
        self.link = "https://api.openai.com/v1/chat/completions"
        self.id_module = "gpt-3.5-turbo"

    def enviar_requisicao(self, valor):
        message_gpt = {
            "model": self.id_module,
            "messages": [{"role": "user", "content": f"{valor}"}]
        }

        body_message = json.dumps(message_gpt)

        try:
            request = requests.post(self.link, headers=self.headers, data=body_message)
            response = request.json()
            message = response["choices"][0]["message"]["content"]
            return message
        except Exception as e:
            print("Ocorreu um erro na requisição à API:", e)
            return None

    def exibir_resposta(self, resposta):
        print(resposta)

    def executar_chat(self):
        while True:
            value = input("Olá seja bem-vindo, o que você deseja perguntar? (Digite 'sair' para encerrar)\n")

            if value.lower() == "sair":
                print("Até logo!")
                break

            resposta = self.enviar_requisicao(value)
            if resposta:
                self.exibir_resposta(resposta)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.executar_chat()