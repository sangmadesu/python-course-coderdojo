from flask import Flask, render_template
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)

# Semua konfigurasi flask disimpan di tipe data dictionary, config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/daftarbuku'
app.config['SECRET-KEY'] = 'belajar'
db = SQLAlchemy(app)

# Model buku
class Buku(db.Model, object):
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))

admin = Admin(app, name='daftarbuku', template_mode='bootstrap3')
admin.add_view(ModelView(Buku, db.session))

@app.route('/')
def show_index():
    return render_template('homepage/index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
