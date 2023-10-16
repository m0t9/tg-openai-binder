# tg-openai-binder
a simple Telegram bot to interact with Open AI models

# Build

1. clone this repo via `git clone https://github.com/m0t9/tg-openai-binder`
2. set your parameters in `.cfg` file
   - OpenAI API key to `api_key`
   - Telegram bot token to `token`
   - list of Telegram IDs of users allowed to interact with bot to `allowed_ids`
   - other settings (commented out in `.cfg`).

     **There're also some important settings like used OpenAI `model`**
4. execute `docker build -t tg-openai-bind .` in root of the cloned repo to create a Docker image for bot
5. execute `docker run -d tg-openai-bind` to run your bot

# Interaction

`/start` to send an initial message (that you can modify in `.cfg`)

`/delete_context` command is intended to clear the dialogue context (start the discussion from the very beginning)

Any other message will be considered as a request to Open AI
