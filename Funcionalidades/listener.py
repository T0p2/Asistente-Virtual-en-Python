'''En resumen, este código proporciona una interfaz simple 
para realizar transcripción de voz a texto utilizando el servicio 
de OpenAI llamado Whisper, que es una tecnología de reconocimiento 
automático de habla (ASR). También utiliza speech_recognition para 
capturar audio desde el micrófono y otras bibliotecas para 
manipulación de audio'''



from Funcionalidades.talker import talk
import speech_recognition as sr
import io
from pydub import AudioSegment
import whisper
import tempfile
import os
import openai


listener = sr.Recognizer() 
name = "Alexa"

temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file, 'temp.wav')



#Captura audio desde el micrófono, lo almacena en un archivo 
# temporal y devuelve la ruta del archivo.
def listen_for_mic():
    try:
        with sr.Microphone() as source:
            print("Deci algo")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            talk(audio)
            data = io.BytesIO(audio.get_wav_data())
            audio_clip = AudioSegment.from_file(data)
            audio_clip.export(save_path, format='wav')
    except Exception as e:
            print(e)
    return save_path


#Realiza la transcripción de voz a texto utilizando la biblioteca 
# openai y devuelve el texto transcribido.
def recognize_audio(save_path):
    audio_file = open(save_path, "rb")
    transcription = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcription['text'])
    return transcription['text']


def listen():
    return recognize_audio(listen_for_mic()).lower()



