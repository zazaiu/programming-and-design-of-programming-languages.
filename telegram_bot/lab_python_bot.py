import telebot
from telebot import types

API_TOKEN = '7071755957:AAFofQlSTFtXAkb0CV3RbnRWmzJ3tnYSUOE'

bot = telebot.TeleBot(API_TOKEN)

# Состояния пользователя
states = {
    'language_choice': 'language_choice',
    'language_selected': 'language_selected'
}

# Словарь для хранения состояний пользователей
users = {}

# Словарь с языками программирования и ссылками на их сайты
languages = {
    'Python': {
        'url': 'https://www.python.org/',
        'description': 'Python — высокоуровневый язык программирования, который широко используется в веб-разработке, научных исследованиях и других областях.'
    },
    'Java': {
        'url': 'https://www.java.com/ru/',
        'description': 'Java — объектно-ориентированный язык программирования, который широко используется в разработке корпоративных приложений и мобильных приложений.'
    },
    'JavaScript': {
        'url': 'https://learn.javascript.ru/',
        'description': 'JavaScript — язык программирования, который используется для создания интерактивных веб-сайтов и веб-приложений.'
    },
    'C++': {
        'url': 'https://isocpp.org/',
        'description': 'C++ — язык программирования, который широко используется в разработке игр, системного программирования и других высокопроизводительных приложений.'
    }
}

@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    users[user_id] = {'state': states['language_choice']}
    ask_language(message)

def ask_language(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for language in languages.keys():
        markup.add(language)
    bot.send_message(message.chat.id, "Здравствуйте, какой язык программирования вы хотите изучить?", reply_markup=markup)

@bot.message_handler(func=lambda message: users.get(message.from_user.id, {}).get('state') == states['language_choice'])
def handle_language_choice(message):
    user_id = message.from_user.id
    chosen_language = message.text
    if chosen_language in languages:
        url = languages[chosen_language]['url']
        description = languages[chosen_language]['description']
        url_button = types.InlineKeyboardButton(text=f"Ссылка на сайт для изучения {chosen_language}", url=url)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(url_button)
        bot.send_message(message.chat.id, f"Ваш выбор: {chosen_language}.\n\nОписание:\n{description}\n\nВот ссылка:", reply_markup=keyboard)
        users[user_id]['state'] = states['language_selected']
        users[user_id]['chosen_language'] = chosen_language
    else:
        bot.send_message(message.chat.id, 'Язык программирования не найден. Попробуйте снова.')
        ask_language(message)

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = "Доступны следующие языки программирования:\n"
    for lang, data in languages.items():
        help_text += f"{lang}: {data['url']}\n"
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: users.get(message.from_user.id, {}).get('state') == states['language_selected'])
def handle_language_selected(message):
    bot.send_message(message.chat.id, "Вы уже выбрали язык программирования. Если хотите выбрать другой, нажмите /start.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
