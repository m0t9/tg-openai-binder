# tg-openai-binder
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A simple Telegram bot to interact with Open AI models

# Build

1. clone this repo via `git clone https://github.com/m0t9/tg-openai-binder`
2. set your parameters in `.env` file
   - OpenAI API key to `API_KEY`
   - Telegram bot token to `TOKEN`
   - list of Telegram IDs of users allowed to interact with bot to `ALLOWED_IDS`
   - other settings

     **There are also some important settings like used OpenAI `MODEL`**
3. execute `docker-compose -f docker-compose.yml -p tg-openai-binder up -d bot` in repo root directory

# Interaction

- `/start` to send an initial message (that you can modify in `.env`)

- `/delete_context` command is intended to clear the dialogue context (start the discussion from the very beginning)

- Any other message will be considered as a request to Open AI

<img width="900" alt="image" src="https://github.com/m0t9/tg-openai-binder/assets/60100612/92b90a80-e34a-4e51-8551-2071c55e3cf5">

