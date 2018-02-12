from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           the_title='This is the index page')


@app.route('/listing')
def display_listing():
    names = ['Paul', 'George', 'Ringo', 'John']
    return render_template('listing.html',
                           the_title='This is the LISTING page.',
                           the_names=names, )


@app.route('/hello/<name>')
def hello(name="unknown"):
    return render_template('hello.html',
                           the_title='The hello page',
                           the_name=name,)


@app.route('/processform', methods=['GET', 'POST'])
def form_process():
    if request.method == 'GET':
        return render_template('form.html',
                               the_title='This is the form page')
    elif request.method == 'POST':
        first = request.form['firstname']
        session['first'] = first
        last = request.form['lastname']
        session['last'] = last
        return f'Hi there, your name is {first} {last}'
    return 'Please use GET or POST.'


@app.route('/showname')
def show_the_name():
    return f"Hello  {session.get('first', 'unknown')} {session.get('last', 'unknown')}"


@app.route('/bye')
def bye():
    return render_template('bye.html',
                           the_title='This is the bye page')

if __name__ == '__main__':
    app.secret_key = 'youwillneverguess'
    app.run(debug=True)

