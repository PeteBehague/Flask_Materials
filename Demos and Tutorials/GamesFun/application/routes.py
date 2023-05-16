from application import app, db
from application.models import Games
from flask import render_template, request
from application.forms import AddGameForm, UpdateGameForm, DeleteGameForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('layout_master.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    message = ''
    add_game_form = AddGameForm()
    if request.method == 'POST':
        if add_game_form.validate_on_submit():
            new_game = Games(name=add_game_form.name.data.lower())
            db.session.add(new_game)
            db.session.commit()
            message = f"{new_game.name} has been added successfully to the database"
            add_game_form.name.data = ''
        else:
            message = "Invalid data. Addition rejected"
    return render_template('add_game.html', form=add_game_form, message=message)


@app.route('/display_games')
def display_games():
    all_games = Games.query.all()
    return render_template('display_games.html', games=all_games)


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
                message = f"{delete_game_form.name.data.lower()} has been deleted"
            else:
                message = "Game could not be found. Please enter a valid game."

    return render_template('delete_game.html', form=delete_game_form, message=message)