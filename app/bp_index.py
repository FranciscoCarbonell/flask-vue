from flask import Blueprint
from flask import render_template
from flask_login import login_required

import os

app_node = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'web')
print(app_node)

bp_index = Blueprint('index', __name__, template_folder='../web')

@bp_index.route('/')
def index():
    return render_template('index.html')