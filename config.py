import configparser

parser = configparser.ConfigParser()
parser.read('.cfg')

OPEN_AI_API_KEY = parser.get('OPEN_AI', 'api_key')
MODEL = parser.get('OPEN_AI', 'model')

BOT_TOKEN = parser.get('BOT', 'token')
PLACEHOLDER = parser.get('BOT', 'placeholder')
CLEAR_CONTEXT_ANSWER = parser.get('BOT', 'clear_context_answer')
ALLOWED_IDS = list(map(lambda x: int(x.strip()), parser.get('BOT', 'allowed_ids').split(',')))
START_PLACEHOLDER = parser.get('BOT', 'start_placeholder')
OPEN_AI_ERROR_MESSAGE = parser.get('BOT', 'open_ai_error')
