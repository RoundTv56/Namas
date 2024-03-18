import asyncio
import aiohttp
from highrise import BaseBot, User
import openai

# Configure sua chave de API da OpenAI
openai.api_key = "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"  # Substitua pela sua chave da API da OpenAI

class ResponseBot(BaseBot):
    async def on_chat(self, user: User, message: str):
        if message.startswith("!say"):
          # Remove the "!question" command and keep just the question
            question = message[len("!say "):]
            response = self.generate_response(question)
            await self.highrise.chat(response)

    def generate_response(self, input_text):
        # Use a API da OpenAI para gerar uma resposta
        response = openai.Completion.create(
            engine="davinci",
            prompt=input_text,
            max_tokens=50  # Limite o tamanho da resposta, se necessário
        )

        return response.choices[0].text

async def main():
    async with aiohttp.ClientSession() as session:
        # Configure a sessão do cliente HTTP para interagir com a API do Highrise Bot
        headers = {"Authorization": "Bearer 0aa8ee0e74a44bfed08923e09b193aa891ee35bbc9dc70427f74037ec481b1f6"}  # Substitua pelo seu token do bot

        # Substitua pela URL correta da API do Highrise para o chat
        chat_api_url = "https://webapi.highrise.game/"

        # Inicie a escuta de mensagens de chat
        async with session.ws_connect(chat_api_url, headers=headers) as ws:
            bot = ResponseBot(ws)
            await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
          