from flask import Flask
from flask import render_template
from flask import Markup
import markdown

app = Flask(__name__)


@app.route('/')
def index():
    mkd = '''
    # header
    ## header2
    [picture](http://www.example.com)
    * 1
    * 2
    * 3
    **bold**
    '''
    return render_template('index.html', mkd=mkd)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
