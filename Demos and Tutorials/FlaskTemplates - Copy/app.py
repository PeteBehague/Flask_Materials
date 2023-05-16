from flask import Flask, render_template, request, redirect, url_for
from dog import DogForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '08523ac73d20d781d9dd6ea1d38f883d'


@app.route('/add_dog', methods = ['GET','POST'])
def add_dog():
    # instantiate the DogForm object
    form = DogForm()

    # checks is the http request is a post request
    if request.method == 'POST':
        # checks if the form passes validation
        if form.validate_on_submit():
            # adds the dog to the database
            dog = DogForm(
                name = form.name.data,
                age = form.age.data,
                breed = form.breed.data
            )
            #db.session.add(dog)
            #db.session.commit()
            # redirects the user to the home page
            return redirect(url_for('home') + '')

    # pass object to Jinja2 template
    return render_template('add_dog.html', form=form)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html', name="XXX")


@app.route('/number_comparer/<int:x>,<int:y>,<user_names>')
def number_comparer(x, y, user_names):
    list_of_users = user_names.split(',')
    search_char = list_of_users[0].upper()
    list_of_users = list_of_users[1:]
    return render_template('AnotherPage.html', x=x, y=y, search_char=search_char, employees=list_of_users)


@app.route('/greeting/<persons_name>')
def greeting(persons_name):
    return render_template('Greeting.html', name=persons_name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
