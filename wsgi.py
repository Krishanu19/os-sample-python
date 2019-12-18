from flask import Flask, render_template

application = Flask(__name__, template_folder='template')

@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run()