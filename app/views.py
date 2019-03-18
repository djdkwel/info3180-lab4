"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
'''import datetime
from app import app
from flask import render_template, request, redirect, url_for,flash'''
import os
from app import app,db
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app.forms import UploadForm
from app.models import UserProfile
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")
    
@app.route('/profile',methods=['GET','POST'])
def profile():
    form = UploadForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        location = request.form['location']
        gender = request.form['gender']
        biography = request.form['biography']
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user =  UserProfile(firstname,lastname,email,location,gender,biography,filename)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully filled out the form', 'success')  
        redirect(url_for('profiles'))
    flash_errors(form)
    return render_template('profile.html', form=form)

@app.route('/profiles')
def profiles():
    users = db.session.query(UserProfile).all()
    return render_template('profiles.html', users=users)

@app.route('/profiles/<userid>')
def profile_userid(userid):
    user=UserProfile.query.get(userid)
    return render_template('userprofile.html',user=user)
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
'''
@app.route('/profile')
def profile():
    datejoined=format_date_joined()
    return render_template('profile.html', date = datejoined)
    #return render_template('profile.html')'''
    
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
