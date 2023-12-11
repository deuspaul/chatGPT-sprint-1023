#TLDL: Too Long Didnt Listen!


# Table of Contents

1.  [TLDL](#org544b433)
    1.  [What is this tool?](#orgcbe7844)
    2.  [Requirements](#org9c4e782)
    3.  [How to set up](#org6f6550d)
    4.  [How to use](#orgf8323f5)



<a id="org544b433"></a>

# TLDL: Too long didnt listen

The whatsapp audio message transcriber

Me automatically whenever I receive a whastapp audio message with a monumental length:
“Look, I aint listening to all that. I am happy for you though or sorry that it happened…”

Some audio messages are just too long for my liking a.k.a. attention span. If they want to talk, why not just call?. 

Some audio messages have also contained important steps/instructions and having to listen to the message many times until I document all the notes is annoying, which is something a text message would be much better for...


<a id="orgcbe7844"></a>

## What is this tool?

A tool that will transcribe, summarize and provide bullet points from downloaded whatsapp audio messages


<a id="org9c4e782"></a>

## Requirements:

- Python 3.10 or higher
- OpenAI API key


<a id="org6f6550d"></a>

## How to set up:

1. Clone the repository:

```git clone https://github.com/deuspaul/chatGPT-sprint-1023.git```

2. Install the required packages:

```pip install -r requirements.txt```

3. Create the .env file in the 'capstone_project folder', and add your OpenAI API Key:

```OPENAI_API_KEY="<Replace with your API key>"```


<a id="orgf8323f5"></a>

## How to use:

Download your WhatsApp audio message to the 'audio_messages' folder and run the 'main.py' file with python.
The processed audio messages will be moved to the 'audio_messages/processed' folder.
