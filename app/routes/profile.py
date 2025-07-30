from flask import Blueprint, session, redirect, url_for, render_template
from app.models import User

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.filter_by(username=session['user']).first()
    return render_template('profile.html', user=user)
