# подключение библиотеки telebot
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'
from telebot import TeleBot, types
import random

bot = TeleBot(token='тут размещается токен', parse_mode='html') # создание бота


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    sti = open('sticker2.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Нужно принять важное решение? Задавай мне вопрос, но учти, вопрос должен быть общим (я ведь не энциклопедия, в конце концов).', # текст сообщения
    )
# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
  
  answers = ("Это определенно так", "Без сомнения.", "Насколько я понимаю, да.", "Да, безусловно.", "Скорее всего.", "Прогноз хороший.", "Да.", "Знаки указывают на да.", "Спросите еще раз позже.", "Сконцентрируйтесь и спросите еще раз.", "Не могу предсказать сейчас.", "Не рассчитывайте на это.", "Мой ответ - нет.", "Мои источники говорят, что нет.", "Перспективы не очень хорошие.")
  choice = random.choice(answers)
  mess = "{}".format(choice)   
  bot.send_message(
      chat_id=message.chat.id,
      text= mess
    )



# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()