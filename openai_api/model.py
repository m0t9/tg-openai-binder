from typing import List, Dict

import openai

import config

openai.api_key = config.OPEN_AI_API_KEY


class Model:
    """
    Entity to describe the context of certain user
    """

    def __init__(self) -> None:
        self.user_context: List[Dict[str, int]]
        self.user_context = list()

    def generate_answer(self, query: str) -> str:
        """
        Method to extend the user's context by new query
        :param query: incoming query
        :return: answer based on the entire context
        """
        self.user_context.append(
            {"role": "user",
             "content": query}
        )
        self.update_context()
        try:
            completion = openai.ChatCompletion.create(
                model=config.MODEL,
                messages=self.user_context
            )
            return completion["choices"][0]["message"]["content"]
        except Exception as AnyOpenAIError:
            return config.OPEN_AI_ERROR_MESSAGE

    def update_context(self) -> None:
        """
        Maintain a context as a list of no more than 10 messages
        :return: None
        """
        if len(self.user_context) > 10:
            self.user_context.pop(0)
