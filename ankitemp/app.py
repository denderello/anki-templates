import os

from flask import Flask, abort, render_template
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'ankitemp': ('static/sass', 'static/css', '/static/css')
})

@app.route('/<string:card_type>')
def display_card_type(card_type : str):
    template_file = f'{card_type}.html.j2'

    if not os.path.isfile(f'ankitemp/templates/{template_file}'):
        abort(404)

    return render_template(template_file, card_type=card_type)