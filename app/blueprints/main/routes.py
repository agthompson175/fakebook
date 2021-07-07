from flask import render_template, url_for, jsonify
from .import bp as app


'''
CREATE - POST
READ   - GET
UPDATE - PUT
DELETE - DELETE
'''


@app.route('/users')
def get_users():

    return jsonify({
        'message': 'This works!!!!!!!!'
    })


# profile
@app.route('/profile')
def profile():
    logged_in_user = 'Adam'
    return render_template('profile.html', u=logged_in_user)


# contact
@app.route('/contact')
def contact():

    return """
    <h1>contact us yo</h1>
    """
