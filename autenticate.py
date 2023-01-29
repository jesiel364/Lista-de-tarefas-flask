import pyrebase

config = {
	  'apiKey': "AIzaSyDDQXepg6eW_fygTg6_LM9t1eVPhTvULDc",
	  'authDomain': "lista-de-tarefas-c7323.firebaseapp.com",
	  'databaseURL': "https://lista-de-tarefas-c7323-default-rtdb.firebaseio.com",
	  'projectId': "lista-de-tarefas-c7323",
	  'storageBucket': "lista-de-tarefas-c7323.appspot.com",
	  'messagingSenderId': "302470237725",
	  'appId': "1:302470237725:web:f0e82f04371de15a4e40f4",
	  'measurementId': "G-RR9LLY7NB2"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@email.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)

# info = auth.get_account_info(user['idToken'])
# print(info)

# auth.send_email_verification(user['idToken'])

# auth.send_password_reset_email(email)