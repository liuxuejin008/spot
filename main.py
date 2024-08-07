import markdown
from flask import Flask, jsonify
from api.ext import db
from api.spotAPI import spots_bp
from flask import  render_template
import os
from api import app
db.init_app(app)
# 注册蓝本
app.register_blueprint(spots_bp)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.template_filter('format_datetime')
def format_datetime(value, format='%Y.%m.%d'):
    if value is None:
        return ""
    return value.strftime(format)


@app.template_filter('md_html')
def md_html(value):
    if value is None:
        return ""
    return markdown.markdown(value)



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=3300))
