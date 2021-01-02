import nltk
import random

BOT_CONFIG = {
    "intents": { #намерение
        "hello": { # намерение поздороваться
            "examples": ["Здравствуйте", "Добрый день", "Привет"] ,
            "responses": ["Привет, гость", "Здравствуй", "Добрый день"]
        },
        "bye": {
            "examples": ["Пока", "До свидания", "До встречи", "Прощай"] ,
            "responses": ["Пока", "Возвращайся", "Прощай"] 
        },
        "howdoyoudo" : {
            "examples": ["Как дела", "Как сам"] ,
            "responses": ["Всё отлично", "Потихоньку"] 
        },
        "whatareyoudoing" : {
            "examples": ["Что делаешь", "Чем маешся"] ,
            "responses": ["Отвечаю на дурацкие вопросы", "Маюсь фигней"] 
        },
    },
    "failure_phrases": [
        "Я ничего не понял",
        "Что-то непонятно",
        "Я всего лишь бот, сформулируйте попроще"
    ]
}

def filter_text(text):
    text = text.lower()         #Приведение текста к нижнему регистру
    text = [c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя -']
    return ' '.join(text)

def match(text, example):      #Сравнение введенного текста
    text = filter_text(text)
    example = filter_text(example)
    
    distance = nltk.edit_distance(text, example) / len(example)
    
    if distance < 0.4:
        return True     #Текст совпадает
    else:
        return False     #Текст не совпадает
    
def get_intent(text):
    for intent, data in BOT_CONFIG['intents'].items():
        for example in data['examples']:
            if match(text, example):
                return intent
                
def get_answer_by_intent(intent):
    phrases = BOT_CONFIG['intents'][intent]['responses']
    return random.choice(phrases)
    
def bot(text):
    # 1. Пытаемся понять намерение
    intent = get_intent(text)
    if intent:
        return get_answer_by_intent(intent)
        
    # 2. Пытаемся сгенерировать ответ по контексту
    
    
    # 3. Отвечаем "заглушкой"
    failure_phrases = BOT_CONFIG["failure_phrases"]
    return random.choice(failure_phrases)

question = " "
while question not in ["Выход", "Отстань"]:
    question = input()
    answer = bot(question)
    print (answer)
