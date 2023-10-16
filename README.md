# tg-openai-binder
a simple Telegram bot to interact with Open AI models

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

`/start` to send an initial message (that you can modify in `.env`)

`/delete_context` command is intended to clear the dialogue context (start the discussion from the very beginning)

Any other message will be considered as a request to Open AI
