from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('mainPage.html', author = "Bob", sunny = False)




if __name__ =='__main__':
    app.run()