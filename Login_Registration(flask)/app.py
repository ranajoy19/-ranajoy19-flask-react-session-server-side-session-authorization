from flask import Flask,request,jsonify,session
from config import ApplicationConfig
from flask_cors import CORS
from flask_session import Session
from flask_bcrypt import Bcrypt
from models import db,User

# initializing the app

app =Flask(__name__)
app.config.from_object(ApplicationConfig)
db.init_app(app)
cors =CORS(app,supports_credentials=True)
bcrypt = Bcrypt(app)
server_session= Session(app)

with  app.app_context():
    db.create_all()

@app.route("/info")

def Get_Current_User():
    user_id=session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Unauthorized '}), 401


    #Retrieve a user by email:
    user= User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "email": user.email
    })

# setting Routh for register with a url of localhost/register with a post method using Email and Password
# this function will return email and unique guid (default uuid4 configure inside the models.py)

@app.route("/register" , methods=["POST"])

def Register_User():

    email=request.json["email"]
    password=request.json["password"]

    #Retrieve a user by email:
    user_exist= User.query.filter_by(email=email).first()

    # this will return a boolean so that we can validate whether the user is already register or not
    if user_exist is not None:
        return jsonify({'error':'user already exist'}),409

    hashed_password=bcrypt.generate_password_hash(password)
    new_user=User(email=email,password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    session["user_id"]=new_user.id

    return jsonify({
        "id" : new_user.id,
        "email": new_user.email,
        "Message":"you are Register Successfully"
    })

@app.route("/login", methods=["POST"])

def User_Login():
    email = request.json["email"]
    password = request.json["password"]

    #Retrieve a user by email:
    user= User.query.filter_by(email=email).first()

    # if user is already register show this error message

    if user is None :
        return jsonify({'error': 'Unauthorized '}), 401

    if not bcrypt.check_password_hash(user.password,password,):
        return jsonify({'error': 'Unauthorized '}), 401

    session["user_id"]=user.id

    return jsonify({
        "id": user.id,
        "email": user.email,
        "Message": "you are Successfully Logged In"
    })
@app.route("/logout",methods=["POST"])
def User_Logout():

     session.pop("user_id")
     return "200"

if __name__=="__main__":
    app.run(debug=True)

