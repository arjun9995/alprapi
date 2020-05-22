import sqlite3
def fun():
    connection = sqlite3.connect('vehicle_data.db')
    cursor = connection.cursor()

    create_table = "CREATE TABLE IF NOT EXISTS vehicle (id INTEGER PRIMARY KEY, location text, time text, licence_number text)"
    cursor.execute(create_table)

    connection.commit()

    connection.close()
