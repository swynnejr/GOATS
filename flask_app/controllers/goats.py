from flask_app import app
from flask_app.models.trail import Trail
from flask_app.models.athlete import Athlete
from flask import render_template, redirect, session, request, flash

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/trails')
def trails():
    return render_template("trails.html")

@app.route('/trails/searched')
def trailsSearched():
    return render_template("trailsSearched.html")

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
            'user_id': session['user_id']
        }
        Athlete.create_athlete(data)
        flash('Athlete accepted')
        return redirect('/admin')
    flash('Athlete declined')
    return redirect('/admin')