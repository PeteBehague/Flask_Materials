from application import app, db
from application.models import Games, Users
from application.forms import AddGameForm, UpdateGameForm, DeleteGameForm, RegistrationForm, LoginForm
from flask import Flask, request, render_template, url_for, redirect
from flask_login import login_user, current_user, logout_user, login_required
from application import bcrypt

@app.route('/add', methods=['GET', 'POST'])
def add():
    message = ""
    add_game_form = AddGameForm()
    if request.method == 'POST':
        if add_game_form.validate_on_submit():
            new_game = Games(name=add_game_form.name.data.lower())
            db.session.add(new_game)
            db.session.commit()
            message = f"{new_game.name} has been successfully added to the database"
        else:
            message = "Game name invalid. Please try again"

    return render_template('add_game.html', form=add_game_form, message=message)


@app.route('/')
@app.route('/home')
@app.route('/view_all_games_as_articles')
def view_all_games_as_articles():
    all_games = Games.query.all()
    # games_string = ""
    # for game in all_games:
    #     games_string += "<br>"+ game.name
    return render_template('view_all_games_as_articles.html', games=all_games)


@app.route('/display_games_as_table')
def display_games_as_table():
    all_games = Games.query.all()
    # games_string = ""
    # for game in all_games:
    #     games_string += "<br>"+ game.name
    return render_template('display_games_as_table.html', games=all_games)

@app.route('/count')
def count():
    number_of_games = Games.query.count()
    message = f"There are currently {number_of_games} games in the database"
    return render_template('count.html', message=message)

@app.route('/update', methods=['GET', 'POST'])
def update():
    message = ""
    update_game_form = UpdateGameForm()
    if request.method == 'POST':
        if update_game_form.validate_on_submit():
            game = Games.query.filter_by(name=update_game_form.oldname.data.lower()).first()
            if not game is None:
                game.name = update_game_form.newname.data.lower()
                db.session.commit()
                message = f"{update_game_form.oldname.data.lower()} has been altered to {game.name}"
            else:
                message = "Game could not be found. Please enter a valid game."
        else:
            message = "Game name invalid. Please try again"

    return render_template('update_game.html', form=update_game_form, message=message)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    message = ""
    delete_game_form = DeleteGameForm()
    if request.method == 'POST':
        if delete_game_form.validate_on_submit():
            game = Games.query.filter_by(name=delete_game_form.name.data.lower()).first()
            if not game is None:
                db.session.delete(game)
                db.session.commit()
                message = f"{game.name} has been successfully removed from the database"
            else:
                message = "Game could not be found. Please enter a valid game."
        else:
            message = "Game name invalid. Please try again"

    return render_template('delete_game.html', form=delete_game_form, message=message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('view_all_games_as_articles'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_pw
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('view_all_games_as_articles'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('view_all_games_as_articles'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
        # if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('view_all_games_as_articles')
    return render_template('login.html', title='Login', form=form)





