import os

# webhook
URL = os.environ.get('https://app-twxapi.herokuapp.com/')
PORT = int(os.environ.get('64577', '5000'))

# telegram
TOKEN = os.environ.get('524768301:AAHuaHpJQ1TunEmYDcjJlJdvw8d7qdXUuUc')
