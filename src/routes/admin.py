from flask import Blueprint, render_template
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def index():
    dfSummary = None
    return render_template('admin/index.html', dfSummary = dfSummary)

