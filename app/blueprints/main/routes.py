from flask import render_template, url_for, jsonify, request, flash, redirect
from .import bp as app
from flask_login import current_user
from app import db
from app.blueprints.authentication.models import User
from app.blueprints.blog.models import Post



@app.route('/')
def home():
    context = {
        'posts': current_user.followed_posts() if current_user.is_authenticated else []
    }
    return render_template('home.html', **context)

@app.route('/users')
def get_users():

    return jsonify({
        'message': 'This works!!!!!!!!'
    })


# profile
@app.route('/profile', methods= ['GET', 'POST'])
def profile():
    if request.method == 'POST':
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first_name')
        u.last_name = request.form.get('last_name')
        u.email = request.form.get('email')
        db.session.commit()
        flash('Profile Updated Successfully', 'info')
        return redirect(url_for('main.profile'))
    return render_template('profile.html')


# contact
@app.route('/contact')
def contact():

    return """
    <h1>contact us yo</h1>
    """
