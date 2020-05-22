from flask import Flask
from flask_restful import Api

from vehicle import Vehicle

app=Flask(__name__)
app.secret_key='arjun'
api=Api(app)



api.add_resource(Vehicle,'/vehicle/<string:name>')

if __name__=='__main__':
    app.run(port=4999,debug=True)
