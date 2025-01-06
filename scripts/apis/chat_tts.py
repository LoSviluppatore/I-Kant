from openai import OpenAI
import simpleaudio as sa  # Per la riproduzione audio in tempo reale
import asyncio

class ChatTTS:
    def __init__(self, api_key, model="gpt-4o-mini", tts_model="tts-1", voice="alloy"):
        """
        Inizializza la classe con i parametri necessari.
        """
        self.client = OpenAI(api_key = api_key)
        self.chat_model = model
        self.tts_model = tts_model
        self.voice = voice

    async def speak_response(self, prompt):
        """
        Genera una risposta alla domanda e riproduce l'audio in tempo reale.
        """
        # Richiesta al modello di completamento in streaming
        response = self.client.chat.completions.create(model=self.chat_model,
        messages=[{"role": "user", "content": prompt}],
        stream=True)

        print("Generazione della risposta...\n")
        full_response = ""

        # Itera attraverso lo stream della risposta
        for chunk in response:
            if "choices" in chunk:
                delta = chunk.choices[0].get("delta", {})
                if "content" in delta:
                    text = delta["content"]
                    full_response += text
                    print(text, end="", flush=True)  # Stampa il testo in tempo reale

                    # Invia il frammento al TTS
                    audio_response = openai.Audio.speech.create(
                        model=self.tts_model,
                        voice=self.voice,
                        input=text
                    )

                    # Riproduci l'audio senza salvarlo su disco
                    audio_data = audio_response.get("audio", b"")
                    self._play_audio(audio_data)

    def _play_audio(self, audio_data):
        """
        Riproduce i dati audio in memoria utilizzando simpleaudio.
        """
        wave_obj = sa.WaveObject(audio_data, num_channels=1, bytes_per_sample=2, sample_rate=24000)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    async def ask_and_speak(self, prompt):
        """
        Wrapper per semplificare l'interfaccia di utilizzo.
        """
        await self.speak_response(prompt)

