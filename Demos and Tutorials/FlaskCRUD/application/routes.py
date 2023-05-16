from application import app, db
from application.models import Games
from application.forms import AddGameForm, UpdateGameForm, DeleteGameForm
from flask import Flask, request, render_template

@app.route('/add', methods=['GET', 'POST'])
def add():
    message = ""
    add_game_form = AddGameForm()
    if request.method == 'POST':
        if add_game_form.validate_on_submit():
            new_game = Games(name=add_game_form.name.data.lower())
            db.session.add(new_game)
            db.session.commit()
            message = f"{add_game_form.name.data} has been successfully added to the database"
        else:
            message = "request was not a POST. Please try again"

    return render_template('add_game.html', form=add_game_form, message=message)

@app.route('/')
@app.route('/read')
def read():
    all_games = Games.query.all()
    # games_string = ""
    # for game in all_games:
    #     games_string += "<br>"+ game.name
    return render_template('read_games.html', games=all_games)

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
                message = f"{update_game_form.oldname.data} has been altered to {update_game_form.newname.data}"
            else:
                message = "Game could not be found. Please enter a valid game."
        else:
            message = "request was not a POST. Please try again"

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
                message = f"{delete_game_form.name.data} has been successfully removed from the database"
            else:
                message = "Game could not be found. Please enter a valid game."
        else:
            message = "request was not a POST. Please try again"

    return render_template('delete_game.html', form=delete_game_form, message=message)


    # first_game = Games.query.filter_by(name=name).first()

