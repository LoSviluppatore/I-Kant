import asyncio
from apis.chat_tts import ChatTTS

# My turn Emanuele

# Configura la tua chiave API di OpenAI
API_KEY = "YOUR-API-KEY"

async def main():
    # Inizializza la classe ChatTTS
    chat_tts = ChatTTS(api_key=API_KEY)

    # Chiedi all'utente un prompt
    prompt = input("Inserisci una domanda: ")

    # Genera e riproduce la risposta in tempo reale
    await chat_tts.ask_and_speak(prompt)

# Esegui il programma
if __name__ == "__main__":
    asyncio.run(main())
