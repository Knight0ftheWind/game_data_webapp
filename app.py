from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import datetime

# Initialize app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up dictionary for month conversion
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
name_to_num = {months[num] : num + 1 for num in range(12)}

class Game(db.Model):
    """
    This class is the design for a game table
    """
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    genre = db.Column(db.String(20), nullable = True)
    release_date = db.Column(db.Date, nullable = True)

    def __repr__(self):
        return '<Game %r>' % self.title
    
# Route and function to render the list.html file, which will show a table of all games in the db
@app.get('/list')
def list_games():
    game_list = Game.query.all()
    return render_template('list.html', games = game_list)

# To render the form.html file, which allows the user to input data for a game to be added to the db
@app.route('/form')
def game_form():
    return render_template('form.html')

# Post route and function to validate input and add a game to the database
@app.route('/add', methods = ['POST'])
def add_game():
    # Get form values
    title = request.form.get('title', '')
    genre = request.form.get('genre', '')
    day = request.form.get('day', '')
    month_name = request.form.get('month', '')
    year = request.form.get('year', '')

    # Validate Input
    if not title or not genre or not day or not month_name or not year:
        return redirect('/err')

    # Convert Month name to Month number and form date in SQL format
    month = name_to_num[month_name]
    day = int(day)
    year = int(year)
    if year < 1800 or year > 2025:
        return redirect('/err')
    release_date = datetime.date(year, month, day)

    # Add the game to the database
    game = Game(title = title, genre = genre, release_date = release_date)
    db.session.add(game)
    db.session.commit()
    return redirect('/list')

# Route and function to render the error page to prompt the user to input valid information
@app.route('/err')
def error_page():
    return render_template('err.html')

# Route and function to delete a game from the database
@app.route('/delete', methods = ["POST"])
def del_game():
    id = request.form.get('id')
    if id:
        todelete = Game.query.filter_by(id = id).first()
        db.session.delete(todelete)
        db.session.commit()
    return redirect('/list')

if __name__ == "__main__":
    app.run()