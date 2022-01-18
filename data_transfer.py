import sqlite3
DB_PATH = "animal.db"


def connection_to_db():
    connection = sqlite3.connect(DB_PATH)

    return connection


def get_animal_types():
    connection = connection_to_db()

    sqlite_query = f"""
                       SELECT DISTINCT animal_type
                       FROM animals
                       """

    cursor = connection.cursor()
    cursor.execute(sqlite_query)
    data_raw = cursor.fetchall()

    result_list = []
    for item in data_raw:
        if item[0] != None:
            result_list.append(item[0])
    result_list.sort()
    return result_list

def get_breeds():
    connection = connection_to_db()

    sqlite_query = f"""
                       SELECT DISTINCT breed
                       FROM animals
                       """

    cursor = connection.cursor()
    cursor.execute(sqlite_query)
    data_raw = cursor.fetchall()

    breeds_list = []
    for item in data_raw:
        for breed in item:
            temp_result = breed.split("/")
            breeds_list += temp_result

    breeds_list = list(set(breeds_list))
    breeds_list.sort()
    return breeds_list


def get_colors():
    connection = connection_to_db()

    sqlite_query = f"""
                           SELECT DISTINCT color1, color2
                           FROM animals
                           """

    cursor = connection.cursor()
    cursor.execute(sqlite_query)
    data_raw = cursor.fetchall()

    colors_list = []
    for item in data_raw:
        for color in item:
            if color != None:
                if color[-1] == ' ':
                    colors_list.append(color[:-1])
                else:
                    colors_list.append(color)

    colors_list = list(set(colors_list))
    colors_list.sort()
    return colors_list


def get_outcome_subtype():
    connection = connection_to_db()

    sqlite_query = f"""
                           SELECT DISTINCT outcome_subtype
                           FROM animals
                           """

    cursor = connection.cursor()
    cursor.execute(sqlite_query)
    data_raw = cursor.fetchall()

    result_list = []
    for item in data_raw:
        if item[0] != None:
            result_list.append(item[0])
    result_list.sort()
    return result_list


def get_outcome_type():
    connection = connection_to_db()

    sqlite_query = f"""
                           SELECT DISTINCT outcome_type
                           FROM animals
                           """

    cursor = connection.cursor()
    cursor.execute(sqlite_query)
    data_raw = cursor.fetchall()

    result_list = []
    for item in data_raw:
        if item[0] != None:
            result_list.append(item[0])
    result_list.sort()
    return result_list


""" Часть закомментирована, потому что исполнена для переноса данных animals_types """
# data_to_insert = get_animal_types()
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#         cursor = connection.cursor()
#         query = (f"INSERT INTO animals_types VALUES (1, 'Cat')")
#         cursor.execute(query)


""" Часть закомментирована, потому что исполнена для переноса данных в breeds """
# data_to_insert = get_breeds()
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""INSERT INTO breeds (breed) VALUES ('{item}')""")
#          cursor.execute(query)

""" Пришлось добавить это, потому что первый элемент дважды добавился """
# with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""DELETE FROM breeds WHERE id = 1""")
#          cursor.execute(query)


""" Часть закомментирована, потому что исполнена для переноса данных в colors """
# data_to_insert = get_colors()
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""INSERT INTO colors (color) VALUES ('{item}')""")
#          cursor.execute(query)


""" Часть закомментирована, потому что исполнена для переноса данных в outcome_subtype """
# data_to_insert = get_outcome_subtype()
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""INSERT INTO outcome_subtypes (outcome_subtype) VALUES ('{item}')""")
#          cursor.execute(query)

""" Часть закомментирована, потому что исполнена для переноса данных в outcome_type """
# data_to_insert = get_outcome_type()
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""INSERT INTO outcome_types (outcome_subtype) VALUES ('{item}')""")
#          cursor.execute(query)


""" Пришлось добавить, потому что неправильно назвала столбец"""
# with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""ALTER TABLE outcome_types RENAME outcome_subtype TO outcome_type""")
#          cursor.execute(query)

""" Добавила еще один столбец, которого не хватало new_animals"""
# with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""ALTER TABLE new_animals ADD outcome_month INTEGER""")
#          cursor.execute(query)

""" Перенесла данные из старой таблицы в новую"""
# with sqlite3.connect('animal.db') as connection:
#     cursor = connection.cursor()
#     query = (f"""SELECT *
#                  FROM animals""")
#     cursor.execute(query)
#     data_raw = cursor.fetchall()
#
# print(data_raw[0])
# for item in data_raw:
#     with sqlite3.connect('animal.db') as connection:
#         cursor = connection.cursor()
#         query = (f"""INSERT INTO new_animals
#         ("index", age_upon_outcome, animal_id,
#         animal_type, name, breed, color1, color2,
#         date_of_birth, outcome_subtype, outcome_type,
#         outcome_month, outcome_year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
#         cursor.execute(query, item)
#         connection.commit()

""" Далее идут изменения даннsх, чтобы внести значения foreign key"""
# with sqlite3.connect('animal.db') as connection:
#     cursor = connection.cursor()
#     query = (f"""SELECT *
#                  FROM animals_types""")
#     cursor.execute(query)
#     data_to_insert = cursor.fetchall()
#
# print(data_to_insert)
#
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#         cursor = connection.cursor()
#         query = (f"""UPDATE new_animals
#         SET animal_type = {item[0]}
#         WHERE animal_type = '{item[1]}'""")
#         cursor.execute(query)

# with sqlite3.connect('animal.db') as connection:
#     cursor = connection.cursor()
#     query = (f"""SELECT *
#                  FROM breeds""")
#     cursor.execute(query)
#     data_to_insert = cursor.fetchall()
#
# print(data_to_insert)
#
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#         cursor = connection.cursor()
#         query = (f"""UPDATE new_animals
#         SET breed = {item[0]}
#         WHERE breed = '{item[1]}'""")
#         cursor.execute(query)

# with sqlite3.connect('animal.db') as connection:
#     cursor = connection.cursor()
#     query = (f"""SELECT *
#                  FROM outcome_subtypes""")
#     cursor.execute(query)
#     data_to_insert = cursor.fetchall()
#
# print(data_to_insert)
#
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#         cursor = connection.cursor()
#         query = (f"""UPDATE new_animals
#         SET outcome_subtype = {item[0]}
#         WHERE outcome_subtype = '{item[1]}'""")
#         cursor.execute(query)

# with sqlite3.connect('animal.db') as connection:
#     cursor = connection.cursor()
#     query = (f"""SELECT *
#                  FROM colors""")
#     cursor.execute(query)
#     data_to_insert = cursor.fetchall()
#
# print(data_to_insert)
#
# for item in data_to_insert:
#     with sqlite3.connect('animal.db') as connection:
#         cursor = connection.cursor()
#         query = (f"""UPDATE new_animals
#         SET color1 = {item[0]}
#         WHERE color1 LIKE '{item[1]}%'""")
#         cursor.execute(query)

# with sqlite3.connect('animal.db') as connection:
#          cursor = connection.cursor()
#          query = (f"""DELETE FROM new_animals WHERE "index" NOT NULL """)
#          cursor.execute(query)


# print(get_animal_types())
# print(get_breeds())
# print(get_colors())
# print(get_outcome_subtype())
# print(get_outcome_type())
# print("\n")

