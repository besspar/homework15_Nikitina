import sqlite3
DB_PATH = "animal.db"

def get_pet_information(index):
    with sqlite3.connect('animal.db') as connection:
        cursor = connection.cursor()
        query = (f"""SELECT "index", age_upon_outcome, animal_id, new_animals.name, animals_types.animal_type,
                     date_of_birth, outcome_month, outcome_year
                     FROM new_animals
                     INNER JOIN  animals_types ON new_animals.animal_type = animals_types.id
                     WHERE "index" = {index}
                     """)
        cursor.execute(query)
    name_type = cursor.fetchall()[0]
    main_info = {'index': name_type[0], 'age_upon_outcome': name_type[1],
                 'animal_id': name_type[2], 'name': name_type[3], 'animal_type': name_type[4],
                 'date_of_birth': name_type[5], 'outcome_month': name_type[6], 'outcome_year': name_type[7]}

    with sqlite3.connect('animal.db') as connection:
        cursor = connection.cursor()
        query = (f"""SELECT b.breed
                     FROM new_animals
                     INNER JOIN  breeds b on new_animals.breed = b.id
                     WHERE "index" = {index}
                     """)
        cursor.execute(query)
    _breed = cursor.fetchall()[0]
    breed = {'breed': _breed[0]}

    with sqlite3.connect('animal.db') as connection:
        cursor = connection.cursor()
        query = (f"""SELECT c.color
                     FROM new_animals
                     INNER JOIN  colors c on new_animals.color1 = c.id
                     WHERE "index" = {index}
                     """)
        cursor.execute(query)
    color1 = {'color1': cursor.fetchall()}

    with sqlite3.connect('animal.db') as connection:
        cursor = connection.cursor()
        query = (f"""SELECT c.color
                     FROM new_animals
                     INNER JOIN  colors c on new_animals.color2 = c.id
                     WHERE "index" = {index}
                     """)
        cursor.execute(query)
    color2 = {'color2': cursor.fetchall()}

    with sqlite3.connect('animal.db') as connection:
        cursor = connection.cursor()
        query = (f"""SELECT os.outcome_subtype
                     FROM new_animals
                     INNER JOIN  outcome_subtypes os on new_animals.outcome_subtype = os.id
                     WHERE "index" = {index}
                     """)
        cursor.execute(query)
    _outcome_subtype = cursor.fetchall()[0]
    outcome_subtype = {'outcome_subtype': _outcome_subtype[0]}

    final = {**main_info, **breed, **color1, **color2, **outcome_subtype}
    return final

print(get_pet_information(1))
