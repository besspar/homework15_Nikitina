import sqlite3
from flask import Flask, render_template

def get_information(id):
    with sqlite3.connect('animal.db') as connection:
        cursor = connection.cursor()
        query = (f"""SELECT animals_final.id, animals_final.animal_id, animals_final.name, date_of_birth, age_upon_outcome, outcome_subtype, outcome_type, outcome_month, outcome_year, breed.name, color_id
                     FROM animals_final
                     LEFT JOIN outcomes o on animals_final.animal_id = o.animal_id
                     LEFT JOIN breed  on animals_final.breed_id = animals_final.breed_id = breed.id
                     LEFT JOIN animal_colors ac on animals_final.animal_id = ac.animal_id
                     WHERE animals_final.id={id}
                     """)
        cursor.execute(query)
        data_raw = cursor.fetchall()
        result = {}
        result["note"] = data_raw[0][0]
        result["idx"] = data_raw[0][1]
        result["name"] = data_raw[0][2]
        result["birthday"] = data_raw[0][3]
        result["age"] = data_raw[0][4]
        result["subtype"] = data_raw[0][5]
        result["type"] = data_raw[0][6]
        result["month"] = data_raw[0][7]
        result["year"] = data_raw[0][8]
        result["breed"] = data_raw[0][9]
        result["color"] = data_raw[0][10]

        if len(data_raw) > 1:
            result["color"] = result["color"] + " and " + data_raw[1][10]


        return result


print(get_information(9))

app = Flask(__name__)


@app.route("/<int:itemid>")
def search(itemid):
    info = get_information(itemid)
    return render_template("card.html", info=info)


if __name__ == '__main__':
    app.run()