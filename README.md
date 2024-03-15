# tg-openai-binder

![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A simple Telegram bot to interact with Open AI models

# Build

1. clone this repo via
   ```bash
   git clone https://github.com/m0t9/tg-openai-binder
   ```
2. set your parameters in `.env` file

   | Parameter              | Meaning                                                                                                               |
   |------------------------|-----------------------------------------------------------------------------------------------------------------------|
   | `API_KEY`              | Your OpenAI API key                                                                                                   |
   | `MODEL`                | Name of used OpenAI model                                                                                             |
   | `PROXY`                | _Optional. Proxy server for OpenAI queries processing_                                                                |
   | `TOKEN`                | Telegram bot token                                                                                                    |
   | `START_PLACEHOLDER`    | Message that bot will send as response to `/start` command                                                            |
   | `PLACEHOLDER`          | Message that bot will show while request processing                                                                   |
   | `CLEAR_CONTEXT_ANSWER` | Message that bot will send as response to `/delete_context` command                                                   |
   | `CONTEXT_SIZE`         | Number of the last messages in the dialogue with bot that will be considered as context. High values affect RAM usage |
   | `OPEN_AI_ERROR`        | Message that bot will send if something goes wrong during OpenAI query processing                                     |
   | `ALLOWED_IDS`          | List of Telegram users (separated by comma) IDs that are allowed to interact with bot                                 |
   | `ENABLE_RENDER`        | True or False. Exposes the web-server on :10000 (required for render.com free-tier web-service deployment)            |

3. execute this command in repo root directory
    ```bash
    docker-compose up -d --build
    ```

# Interaction

| Command           | Meaning                                                             |
|-------------------|---------------------------------------------------------------------|
| `/start`          | Start dialogue with bot. As response it sends `START_PLACEHOLDER`   |
| `/delete_context` | Clears the dialogue context with user. Sends `CLEAR_CONTEXT_ANSWER` |
| any other text    | Will be considered as a query to OpenAI                             |

<img width="900" alt="image" src="https://github.com/m0t9/tg-openai-binder/assets/60100612/92b90a80-e34a-4e51-8551-2071c55e3cf5">

