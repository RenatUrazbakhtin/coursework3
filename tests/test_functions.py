"Импорт функций из functions"
import pytest

from src.functions import read_json
from src.functions import check_executed, mask_from, mask_to, formatted_date, program_output



def test_read_json(data):
  """
  тест для функции чтения файла из json
  :return:
  """
  assert read_json("test_operations.json") == data

def test_check_executed(data, executed_expected):
  """
  тест для проверки статуса операции
  :param data:
  :return:
  """
  assert check_executed(data) == executed_expected

def test_mask_from():
  """
  тест для проверки функции mask_from
  :return:
  """
  assert mask_from("Счет 12189246980267075758") == "Счет 1218 92** **** **** 5758"
  assert mask_from("МИР 4878656375033856") == "МИР 4878 65** **** 3856"
  assert mask_from("Visa Platinum 8990850370884895") == "Visa Platinum 8990 85** **** 4895"
  assert mask_from("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"

def test_mask_to():
  """
  тест для проверки функции mask_to
  :return:
  """
  assert mask_to("Счет 59986621134048778289") == "Счет **8289"
  assert mask_to("Счет 49304996510329747621") == "Счет **7621"
  assert mask_to("MasterCard 6783917276771847") == "MasterCard **1847"
  assert mask_to("Visa Gold 9447344650495960") == "Visa Gold **5960"

def test_formatted_date():
  """
  тест для проверки функции formatted_date
  :return:
  """
  assert formatted_date("2018-07-31T12:25:32.579413") == "31.07.2018"
  assert formatted_date("2019-11-05T12:04:13.781725") == "05.11.2019"
  assert formatted_date("2019-02-14T03:09:23.006652") == "14.02.2019"
  assert formatted_date("2018-01-23T01:48:30.477053") == "23.01.2018"

def test_program_output():
  """
  тест для проверки функции program_output
  :return:
  """
  assert program_output({'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}) == "08.12.2019 Открытие вклада\nUnknown -> Счет **5907\n41096.24 USD"
  assert program_output({'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}) == "07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD"

def test_main():
  with pytest.raises(FileNotFoundError):
    read_json("../fake_operations.json")

