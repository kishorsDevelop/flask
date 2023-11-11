from flask import Flask, Blueprint, render_template

admin_bp = Blueprint('admin_bp', __name__, template_folder='templates')

@admin_bp.route('/admin')
def admin():
    return render_template('admin.html', msg = 'admin')