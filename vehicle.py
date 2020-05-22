import sqlite3
from flask_restful import Resource,reqparse

class Vehicle(Resource):
    def get(self,name):
        connection = sqlite3.connect('vehicle_data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM vehicle WHERE location=?"
        result = cursor.execute(query,(name,))

        items = []

        for row in result:
            x = {'id':row[0], 'location':row[1], 'time':row[2], 'licence_number':row[3]}
            items.append(x)

        connection.close()
        return {'details':items}

    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument('location')
        parser.add_argument('time')
        parser.add_argument('licence_number')
        row = parser.parse_args()
        connection = sqlite3.connect('vehicle_data.db')
        cursor = connection.cursor()
        query = "INSERT INTO vehicle values (NULL,?,?,?)"
        cursor.execute(query,(row['location'],row['time'],row['licence_number']))
        connection.commit()
        connection.close()
