class EntrepreneurProfile:
  def __init__(self):
      self.name = ""
      self.age = 0
      self.phone = ""
      self.email = ""
      self.zip_code = ""
      self.address = ""
      self.additional_info = ""
      self.ogrnip = ""
      self.inn = ""
      self.bank_account = ""
      self.bank_name = ""
      self.bik = ""
      self.correspondent_account = ""

  def input_personal_info(self):
      self.name = input("Введите имя: ")
      self.age = int(input("Введите возраст: "))
      self.phone = input("Введите телефон: ")
      self.email = input("Введите электронную почту: ")
      self.zip_code = ''.join(filter(str.isdigit, input("Введите индекс: ")))
      self.address = input("Введите почтовый адрес: ")
      self.additional_info = input("Введите дополнительную информацию: ")

  def input_entrepreneur_info(self):
      self.ogrnip = input("Введите ОГРНИП (15 цифр): ")
      while len(self.ogrnip) != 15 or not self.ogrnip.isdigit():
          self.ogrnip = input("Некорректный ввод. Введите ОГРНИП (15 цифр): ")

      self.inn = input("Введите ИНН: ")
      self.bank_account = input("Введите расчётный счёт (20 цифр): ")
      while len(self.bank_account) != 20 or not self.bank_account.isdigit():
          self.bank_account = input("Некорректный ввод. Введите расчётный счёт (20 цифр): ")

      self.bank_name = input("Введите название банка: ")
      self.bik = input("Введите БИК: ")
      self.correspondent_account = input("Введите корреспондентский счёт: ")

  def display_personal_info(self):
      print(f"Имя: {self.name}")
      print(f"Возраст: {self.age}")
      print(f"Телефон: {self.phone}")
      print(f"Электронная почта: {self.email}")
      print(f"Индекс: {self.zip_code}")
      print(f"Почтовый адрес: {self.address}")
      print(f"Дополнительная информация: {self.additional_info}")

  def display_full_info(self):
      self.display_personal_info()
      print(f"ОГРНИП: {self.ogrnip}")
      print(f"ИНН: {self.inn}")
      print(f"Расчётный счёт: {self.bank_account}")
      print(f"Название банка: {self.bank_name}")
      print(f"БИК: {self.bik}")
      print(f"Корреспондентский счёт: {self.correspondent_account}")

def main_menu():
  profile = EntrepreneurProfile()
  while True:
      print("1 — Ввести или обновить информацию")
      print("2 — Вывести информацию")
      print("0 — Завершить работу")
      menu_choice = input("Введите номер пункта меню: ")

      if menu_choice == "1":
          print("1 — Личная информация")
          print("2 — Информация о предпринимателе")
          submenu_choice = input("Введите номер пункта подменю: ")

          if submenu_choice == "1":
              profile.input_personal_info()
          elif submenu_choice == "2":
              profile.input_entrepreneur_info()
          else:
              print("Некорректный пункт меню. Пожалуйста, попробуйте снова.")

      elif menu_choice == "2":
          print("1 — Личная информация")
          print("2 — Вся информация")
          submenu_choice = input("Введите номер пункта подменю: ")

          if submenu_choice == "1":
              profile.display_personal_info()
          elif submenu_choice == "2":
              profile.display_full_info()
          else:
              print("Некорректный пункт меню. Пожалуйста, попробуйте снова.")

      elif menu_choice == "0":
          print("Завершение работы.")
          break

      else:
          print("Некорректный пункт меню. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
  main_menu()