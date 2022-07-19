from StorageClient import Storage
from telebot import types


def create_keyboard_from_expenses(storage_client: Storage, chat_id: int, user_name: str, prefix="expense"):
    expenses = storage_client.getNamesExpenses(chat_id, user_name)

    if expenses is None:
        return None

    markup = types.InlineKeyboardMarkup()

    for name_expense in expenses.keys():
        button = types.InlineKeyboardButton(f"{name_expense}: {round(expenses[name_expense], 2)}",
                                            callback_data=f"{prefix}:{name_expense}")
        markup.add(button)

    return markup

