import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

SAMPLE_TEXT = """
Привет! Приходите работать к нам на должность {name}. 
Платим {price} в месяц. Находимся в городе {city}.
Нужно уметь {tags}
Если интересно, ознакомтесь полностью с описанием вакансии:
{description}
"""
