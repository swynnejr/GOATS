from flask_app import app
from flask_app.models.trail import Trail
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
            'peak_height': request.form['peak_height'],
            'vertical_gain': request.form['vertical_gain'],
            'technical': request.form['technical'],
            'difficulty': request.form['difficulty'],
            'facilities': request.form['facilities'],
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