from flask_app import app
from flask_app.models.trail import Trail
from flask_app.models.athlete import Athlete
from flask import render_template, redirect, session, request, flash

from flask_bcrypt import Bcrypt

@app.route('/')
def index():
    return render_template("index.html")


# ATHLETES PAGES

@app.route('/athletes')
def display_athletes():
    athletes = Athlete.get_all_athletes()
    return render_template("athletes.html", athletes = athletes)

@app.route('/athletes/<int:id>')
def athleteBio(id):
    data = {
        'id':id
    }

    athlete = Athlete.get_one_athlete(data)
    return render_template ('athleteBio.html', athlete = athlete)




# TRAILS PAGES

@app.route('/trails')
def display_trails():
    trails = Trail.get_all_trails()
    return render_template("trails.html", trails = trails)

@app.route('/trails/<int:id>')
def trailBio(id):
    data = {
        'id':id
    }

    trail = Trail.get_one_trail(data)
    return render_template ('trailBio.html', trail = trail)

# RACES SECTION

@app.route('/races')
def races():
    return render_template("races.html")


# ADMIN SECTION BELOW

@app.route('/admin')
def admin():
    if 'user_id' not in session:
        flash("Please log in to view this page.")
        return redirect('/')
    return render_template("addTrail.html")

@app.route('/admin/create/trail', methods=['POST'])
def create_trail():

    if Trail.validate_trail(request.form):
        data = {
            'name': request.form['name'],
            'start': request.form['start'],
            'variation': request.form['variation'],
            'distance': request.form['distance'],
            'peak_height': request.form['peak_height'],
            'vertical_gain': request.form['vertical_gain'],
            'country': request.form['country'],
            'state': request.form['state'],
            'category1': request.form['category1'],
            'category2': request.form['category2'],
            'category3': request.form['category3'],
            'user_id': session['user_id']
        }
        Trail.create_trail(data)
        flash('Trail accepted')
        return redirect('/admin')
    flash('Trail declined')
    return redirect('/admin')

@app.route('/admin/create/athlete', methods=['POST'])
def create_athlete():

    if Athlete.validate_athlete(request.form):
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'birthday': request.form['birthday'],
            'nationality': request.form['nationality'],
            'home_state': request.form['home_state'],
            'weight': request.form['weight'],
            'sex': request.form['sex'],
            'youtube': request.form['youtube'],
            'bio': request.form['bio'],
            'user_id': session['user_id']
        }
        Athlete.create_athlete(data)
        flash('Athlete accepted')
        return redirect('/admin')
    flash('Athlete declined')
    return redirect('/admin')