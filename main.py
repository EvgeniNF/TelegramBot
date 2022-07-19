import telebot
from telebot import types
from StorageClient import Storage
import Expencese
import json


def read_token():
    with open("parameters.json") as file:
        json_file = json.load(file)
        return json_file["token"]


token = read_token()

bot = telebot.TeleBot(token)

client_storage = Storage()


def add_expense_value(message, expense):
    value = 0.0
    try:
        value = float(message.text)
    except Exception as error:
        bot.send_message(message.chat.id, "Введеное значение не является числом")
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=format_start_keyboard())
        return None

    result = client_storage.addValueExpense(message.chat.id, message.chat.username, expense, value)
    if not result:
        bot.send_message(message.chat.id, "Нет возможности записать расход, попробуйте еще раз")
    else:
        bot.send_message(message.chat.id, f"Расход записан: {expense}: {value}")

    bot.send_message(message.chat.id, "Выберите действие", reply_markup=format_start_keyboard())


def format_start_keyboard():
    markup = types.InlineKeyboardMarkup()
    add_new_expense = types.InlineKeyboardButton("Создать новый расход", callback_data="create_expense")
    info = types.InlineKeyboardButton("Получить информацию о расходах", callback_data="info")
    write_expense = types.InlineKeyboardButton("Записать новый расход", callback_data="write_expense")
    add_money_to_balance = types.InlineKeyboardButton("Добавить денег на баланс", callback_data="add_money_balance")
    remove_expense = types.InlineKeyboardButton("Удалить расход", callback_data="remove_expense")
    clear = types.InlineKeyboardButton("Очистить расходы", callback_data="clear")
    markup.add(add_new_expense)
    markup.add(info)
    markup.add(write_expense)
    markup.add(add_money_to_balance)
    markup.add(clear)
    markup.add(remove_expense)
    return markup


def add_expense(message):
    result = client_storage.addNewExpense(message.chat.id, message.chat.username, message.text)

    if result:
        bot.send_message(message.chat.id, f"Добавлен новый расход: {message.text}")
    else:
        bot.send_message(message.chat.id, f"Невозможно добавть новый расход попробуйте еще раз: {message.text}")

    bot.send_message(message.chat.id, "Выберите действие", reply_markup=format_start_keyboard())


def create_expense(chat_id, user_name):
    bot.send_message(chat_id, "Введите имя расхода")
    bot.register_next_step_handler_by_chat_id(chat_id, add_expense)


def add_balance(message):
    value = 0.0
    try:
        value = float(message.text)
    except Exception as error:
        bot.send_message(message.chat.id, "Не возможно конвертировать значение попробуйте еще раз")
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=format_start_keyboard())
        return None

    result = client_storage.addValueBalance(message.chat.id, message.chat.username, value)
    if result:
        bot.send_message(message.chat.id, "Значение записано")
    else:
        bot.send_message(message.chat.id, "Не возможно записать значение попробуйте еще раз")

    bot.send_message(message.chat.id, "Выберите действие", reply_markup=format_start_keyboard())


@bot.message_handler(commands=['start'])
def get_message(message):
    client_storage.addNewUser(message.chat.id, message.chat.username)
    bot.send_message(message.chat.id,
                     "Выберите действие",
                     reply_markup=format_start_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "create_expense":
        create_expense(call.message.chat.id, call.message.chat.username)
    elif call.data == "write_expense":
        markup = Expencese.create_keyboard_from_expenses(client_storage,
                                                        call.message.chat.id,
                                                        call.message.chat.username)
        if len(markup.to_dict()["inline_keyboard"]) > 0:
            bot.send_message(call.message.chat.id, "Выберите расход",
                             reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, "У вас не создано ни одного расхода")
            bot.send_message(call.message.chat.id, "Выберите действие", reply_markup=format_start_keyboard())
    elif call.data == "info":
        expenses = client_storage.getNamesExpenses(call.message.chat.id, call.message.chat.username)
        money = client_storage.getMoney(call.message.chat.id, call.message.chat.username)
        if money is None or expenses is None:
            bot.send_message(call.message.chat.id, "Не возможно получить данные")
        else:
            message = f"Баланс: {str(money)}"
            if len(expenses) > 0:
                for key in expenses:
                    message += f"\n {key}: {expenses[key]}"
            bot.send_message(call.message.chat.id, message)
        bot.send_message(call.message.chat.id, "Выберите действие", reply_markup=format_start_keyboard())
    elif call.data == "add_money_balance":
        bot.send_message(call.message.chat.id, "Введите значение")
        bot.register_next_step_handler_by_chat_id(call.message.chat.id, add_balance)
    elif call.data.find("expense:") != -1:
        bot.send_message(call.message.chat.id, "Введите значение")
        bot.register_next_step_handler_by_chat_id(call.message.chat.id, add_expense_value, call.data.split(":")[1])
    elif call.data == "remove_expense":
        bot.send_message(call.message.chat.id, "Выберите расход")
        bot.send_message(call.message.chat.id, "Выберите действие",
                         reply_markup=Expencese.create_keyboard_from_expenses(client_storage,
                                                                              call.message.chat.id,
                                                                              call.message.chat.username,
                                                                              "remove"))
    elif call.data == "clear":
        expenses = client_storage.getNamesExpenses(call.message.chat.id, call.message.chat.username)

        if expenses is None:
            bot.send_message(call.message.chat.id, "Не возможно получить доступ к расходам")
        else:
            for key in expenses:
                result = client_storage.clearValueExpense(call.message.chat.id, call.message.chat.username,
                                               key, -expenses[key])

                if not result:
                    bot.send_message(call.message.chat.id, f"Не возможно обнулить расход {key}")
        bot.send_message(call.message.chat.id, f"Расходы очищены")
        bot.send_message(call.message.chat.id,
                         "Выберите действие",
                         reply_markup=format_start_keyboard())
    elif call.data.find("remove:") != -1:
        value = call.data.split(":")[1]
        result = client_storage.removeExpense(call.message.chat.id, call.message.chat.username, value)
        if result:
            bot.send_message(call.message.chat.id, f"Расход {value} удален")
        else:
            bot.send_message(call.message.chat.id, f"Невозможно удалить расход {value}, попробуйте снова")
        bot.send_message(call.message.chat.id,
                         "Выберите действие",
                         reply_markup=format_start_keyboard())
    else:
        bot.send_message(call.message.chat.id, "Введите значение", reply_markup=format_start_keyboard())


if __name__ == "__main__":
    bot.polling(True)

