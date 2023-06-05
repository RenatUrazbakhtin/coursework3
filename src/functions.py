import json
import datetime
from operator import itemgetter



def read_json(filename):
    """
    перевод файла с читаемый для Python формат
    :param filename:
    :return: читаемый файл из Json
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def check_executed(data:list[dict]):
    """
    Проверка словарей по статусу выполнения executed
    :param data:
    :return: список словарей со статусом executed
    """
    executed_list = []
    for item in data:
        if "state" in item.keys():
            if item["state"] == "EXECUTED":
                executed_list.append(item)
        else:
            continue
    return executed_list


def mask_from(input_from_account: str):
    """
    форматирует строку в формат: первые 6 цифр читаемые, последние 4 цифры читаемые, остальные символы "*", разделены по пробелам
    :param input_from_account:
    :return: форматированную строку
    """
    from_account_split = input_from_account.split(" ")
    if len(from_account_split) == 2:
        if len(from_account_split[1]) == 16:
            str = " " + from_account_split[-1][0:4] + " " + from_account_split[-1][4:6] + "** " + "**** " + from_account_split[-1][12:]
        elif len(from_account_split[1]) == 20:
            str = " " + from_account_split[-1][0:4] + " " + from_account_split[-1][4:6] + "** " + "**** " + "**** " + from_account_split[-1][16:]
        else:
            return "Cannot identify account from"
        return from_account_split[0] + str
    if len(from_account_split) == 3:
        if len(from_account_split[2]) == 16:
            str = ' ' + from_account_split[-1][0:4] + ' ' + from_account_split[-1][4:6] + '** ' + '**** ' + from_account_split[-1][12:]
        elif len(from_account_split[2]) == 20:
            str = " " + from_account_split[1][0:4] + " " + from_account_split[1][4:6] + "** " + "**** " + "**** " + from_account_split[1][16:]
        else:
            return "Cannot identify account from"
        return from_account_split[0] + " " + from_account_split[1] + str

def mask_to(input_to_account):
    """
    форматирует строку в формат: ** с 4 последними цифрами карты
    :param input_to_account:
    :return: форматированную строку
    """
    to_account_split = input_to_account.split(" ")
    if len(to_account_split) == 2:
        if len(to_account_split[-1]) == 16:
            str = ' **' + to_account_split[-1][12:16]
        elif len(to_account_split[-1]) == 20:
            str = ' **' + to_account_split[-1][16:20]
        else:
            return "Cannot identify account to"
        return to_account_split[0] + str
    if len(to_account_split) == 3:
        if len(to_account_split[-1]) == 16:
            str = ' **' + to_account_split[-1][12:16]
        elif len(to_account_split[-1]) == 20:
            str = ' **' + to_account_split[-1][16:20]
        else:
            return "Cannot identify account to"
        return to_account_split[0] + " " + to_account_split[1] + str



def formatted_date(date):
    """
    преобразует дату в формат число.месяц.год
    :param date:
    :return: преобразованную дату
    """
    given_date = date[:10]
    formatted_date = given_date.split("-")
    formatted_date = formatted_date[2] + "." + formatted_date[1] + "." + formatted_date[0]
    return formatted_date

def sorted_operation(data: list[dict]) -> list[dict]:
    """
    сортирует список словарей по дате
    :param data:
    :return: последние 5 операций
    """
    new_list = []
    last_operations = []
    for item in data:
        if "date" in item:
            new_list.append(item["date"])
    sorted_dates = sorted(new_list, reverse=True)
    for date in sorted_dates[:5]:
        for item in data:
            if "date" in item and item["date"] == date:
                last_operations.append(item)
    return last_operations

def program_output(data):
    """
    собирает конечное сообщение по операции
    :param data:
    :return: конечное сообщение по операции
    """
    first_line = formatted_date(data["date"]) + " " + data["description"]
    if "from" in data.keys():
        second_line = mask_from(data["from"]) + " -> " + mask_to(data["to"])
    else:
        second_line = "Unknown" + " -> " + mask_to(data["to"])
    third_line = data["operationAmount"]["amount"] + " " + data["operationAmount"]["currency"]["name"]
    return '\n'.join([first_line, second_line, third_line])



