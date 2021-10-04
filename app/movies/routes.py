from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import submitMovie
from flask_login import login_required

from app.models import db, Movie


movies = Blueprint('movies', __name__, template_folder='movies_templates')

@movies.route('/hayaomiyazaki')
def miyazaki():
    prod_comp='Studio Ghilbli'
    return render_template('hayaomiyazaki.html', universe=prod_comp)



@movies.route('/submitmovie', methods=['GET','POST'])
@login_required
def submit_movie():
    form = submitMovie()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('form validated')
            newMovie = Movie(movie=form.movie.data, protagonist=form.protagonist.data, antagonist=form.antagonist.data, movie_released=form.movie_released.data, actor=form.actor.data)
            try:
                db.session.add(newMovie)
                db.session.commit()
            except:
                flash('Movie stated is already in the Database, please try again.', category='alert-danger')
                return redirect(url_for('movies.submit_movie'))


            flash('New Movie added!', category='alert-info')
            flash(f'{newMovie.to_dict()}', category='alert-info')
            return redirect(url_for('movies.submit_movie'))
        else:
            flash('You entered incomplete or incorrect data, please try again', category='alert-danger')
            validated = False
        return redirect(url_for('movies.submit_movie'))
    return render_template('submitHero.html', form=form)
