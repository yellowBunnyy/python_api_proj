from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from . import generate_plots


main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Render index html template

    Returns:
        str: This will return the rendered template as a string.
    """
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    """Render proflile html template

    Returns:
        str: This will return the rendered template as a string.
    """
    return render_template('profile.html', 
                            name=current_user.name.title(), 
                            covid=generate_plots.cov_plot(),
                            influenza=generate_plots.flu_plot())
