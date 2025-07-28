from flask import Flask

app = Flask(__name__) #Init Flask

# Server
app.run(debug=True)