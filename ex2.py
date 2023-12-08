ex_2 = """-------------------------------------------------------------------
Дано список країн і міст кожної країни. Потім подані назви міст. 
Для кожного міста вкажіть, в якій країні воно знаходиться. 
Програма отримує на вхід кількість країн n. 
Далі йде n рядків, кожен рядок починається з назви країни, 
потім йдуть назви міст цієї країни. У наступному рядку записано число num_queries, 
далі йдуть num_queries запитів - назви якихось num_queries міст, перерахованих вище. 
Для кожного із запиту виведіть назву країни, в якій знаходиться дане місто

                                                     ||| курс, Бритвич Олександр Володимирович (ПІБ)
-------------------------------------------------------------------"""
print(ex_2)


# Функція для знаходження країни за назвою міста в списку країн та міст
def find_country(city, countries_from_input):
    # Перевіряємо кожну країну та список міст у цій країні
    for country_from_data, cities_from_data in countries_from_input.items():
        # Перевіряємо, чи знаходиться місто у списку міст конкретної країни
        if city in cities_from_data:
            # Якщо знайдено, повертаємо назву країни
            return country_from_data
    # Якщо місто не знайдено у жодній країні, повертаємо відповідне повідомлення
    return "Такого міста в списку не було"


# Вхідні дані для тестування програми
input_data = """2
Ukraine Kyiv Kharkiv Lviv
England London Liverpool Manchester Bristol
3
Kyiv
London
Lviv"""
data_lines = input_data.split("\n")

# Отримання кількості країн та списків їх міст
n = int(data_lines[0])
countries = {}
current_line = 1

for _ in range(n):
    # Розділення рядка на назву країни та список міст цієї країни
    country_data = data_lines[current_line].split()

    country = country_data[0]
    cities = country_data[1:]

    countries[country] = cities
    current_line += 1

# Отримання кількості запитів та виведення країн, в яких знаходяться вказані міста
num_queries = int(data_lines[current_line])
current_line += 1

for _ in range(num_queries):
    # Отримання запиту щодо міста
    query_city = data_lines[current_line]
    # Пошук країни для заданого міста та виведення результату
    country_found = find_country(query_city, countries)

    print(country_found)
    current_line += 1
