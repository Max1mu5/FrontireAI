### Реализованная функциональность
* Парсинг архива статей для создания датасета, содержащего 4 поля:
  - Дата
  - Ключевые слова статьи
  - Количество статей с этими ключевыми словами
  - Актуальность статьи(Считается самим сайтом Scopus из просмотров, цитирований)
* Парсинг сайта "Google trends"

### Особенность проекта в следующем:
* Рекурсивная кластеризация для получения наборов с максимально близкими темами
* Определение актульности темы с учетом статистики, которая характеризуется количеством поисковых запросов

### Основной стек технологий:
* Python
* HTML, CSS, JavaScript
* Google Colab
* Django, REST API
* Apache, wsgi

## СРЕДА ЗАПУСКА
1. Развертывание сервиса производится 
2. Требуется установленный web-сервер с поддержкой Python, и Apache, wsgi
3. Требуется установленный пакет pandas, sklearn, csv, pybliometrics.scopus, pytrends

## УСТАНОВКА
Выполните 
```bash
pip install pandas sklearn csv pybliometrics pytrends
```
