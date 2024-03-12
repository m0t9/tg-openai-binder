import logging
from typing import List, Dict

import openai

import config

openai.api_key = config.OPEN_AI_API_KEY
if config.PROXY is not None:
    openai.proxy = config.PROXY


class Model:
    """
    Entity to describe the context of certain user
    """

    def __init__(self) -> None:
        self.user_context: List[Dict[str, int]]
        self.user_context = list()

    def extend_context(self, message: str, sender: str) -> None:
        """
        Extend context by new message
        :param message: content of the message
        :param sender: "user" or "assistant"
        :return: None
        """
        self.user_context.append({
            "role": sender,
            "content": message
        })
        if len(self.user_context) > config.CONTEXT_SIZE:
            self.user_context.pop(0)

    def generate_answer(self, query: str) -> str:
        """
        Method to extend the user's context by new query
        :param query: incoming query
        :return: answer based on the entire context
        """
        self.extend_context(query, "user")
        try:
            answer = openai.ChatCompletion.create(
                model=config.MODEL,
                messages=self.user_context
            )["choices"][0]["message"]["content"]
            self.extend_context(answer, "assistant")
            return answer
        except Exception as AnyOpenAIError:
            logging.error(f"OpenAI API exception: {AnyOpenAIError}")
            return config.OPEN_AI_ERROR_MESSAGE
