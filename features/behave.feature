Feature: Тестовая фича
  Scenario: Тестовый сценарий
    Given Открыли сайт Гугл "http://google.ru"
    Then Ввели "что такое хорошо и что такое плохо" в поле "ввод"
    Then Проверил что ссылок "> 25"