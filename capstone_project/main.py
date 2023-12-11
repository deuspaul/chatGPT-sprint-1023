#!/usr/bin/env python3

from brain_module import ChatGPT
import shutil
import os

if  __name__ == "__main__": 
  bot = ChatGPT()

  try:
    #The downloaded audio message from whatsapp
    folder_path = "./audio_messages"
    for filename in os.listdir(folder_path):
      if filename.endswith((".flac", ".ogg", ".mp4", ".mpeg", ".mp3", ".m4a")):
        file_path = os.path.join(folder_path, filename)
    audio_files = open(file_path, "rb")

    #Transcribing the audio message with the OpenAI audio endoint API
    response = bot.request_transcription(audio_files)
    print("\nEl texto del mensaje de audio es:\n\n"+response)

    audio_files.close()

    #Moving the file to the 'processed_audio_messages' folder
    shutil.move(audio_files.name, "./audio_messages/processed_audio_messages/")

    #Additional options to work with the audio file
    options = ['resumir', 'crear una lista con los puntos importantes', 'exit']
    user_input = ''
    input_message = "\nMas opciones:\n"
    
    for index, item in enumerate(options):
      input_message += f'{index+1}) {item}\n'
      
    input_message += 'Tu seleccion: '
    
    while user_input != '3':
      user_input = input(input_message)

      match user_input:
        case '1':
          resumen = "puedes hacer un resumen del sigiente mensaje en un renglon?: "+response
          respuesta_resumen = bot.request_openai(resumen)
          print("\nEl resumen del mensaje es:\n"+respuesta_resumen)

        case '2':
          lista = "puedes hacer una lista con los 3 puntos mas importantes del siguiente mensaje?: "+response
          respuesta_lista = bot.request_openai(lista)
          print("\nAqui va la lista de puntos importantes:\n"+respuesta_lista)

    print("Gracias, vuelve pronto!")
 
  except:
    print("Por favor asegurate de que el archivo de audio se encuentra en la carpeta 'audio_messages' y que el formato del archivo sea alguno de los siguientes: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm")
  




  
 
  
