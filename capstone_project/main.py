#!/usr/bin/env python3

from brain_module import ChatGPT

# Doing the following makes python open the folder as a file. Need to investigate way to iterate over several files
# audio_files = open("./audio_messages/", "rb")
audio_files = open("./audio_messages/WhatsApp Ptt 2023-12-08 at 10.12.57.ogg", "rb")

if  __name__ == "__main__": 
  bot = ChatGPT()


  
  
  try:
    #a part where it validates if there was as successful response if not, an error message stating why. Maybe here using a try
    response = bot.request_transcription(audio_files)
    print(response)

  #move the file to the 'processed' folder

  #ask if you would like to further process the message, 1)summarize or 2)create bullet points

  #Im bored, how about we create an image from this text message and see what happens, send it with a random numer for temperature


  except:
    print("Please make sure the file path is correct and that it is in one of the following formats:  flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm")
  


  #failed try checks: 1) if there is no audio file or its not compatible, 2)Cannot connect to openAI, check your API key

  
 
  
