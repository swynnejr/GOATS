from flask_app import app
from flask_app.models.trail import Trail
from flask_app.models.athlete import Athlete
from flask import render_template, redirect, session, request, flash

@app.route('/athletes/<int:id>/Demoor')
def sethjamesdemoor(id):
    data = {
        'id':id
    }

    athlete = Athlete.get_one_athlete(data)
    return render_template ('sjdemoor.html', athlete = athlete)



