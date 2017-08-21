from flask import Flask, render_template, abort, redirect
from geometry.triangle import Triangle
from geometry.circle import Circle
from geometry.square import Square

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Aplikasi Penghitung Geometry</h1>' \
           '<a href="/geometry">Geometry</a>'


@app.route('/geometry', methods=['GET', 'POST'])
def route_geometry():
    return '<h2>Daftar geometry</h2>' \
           '<ol>' \
           '<li><a href="/circle">Circle</a></li>' \
           '<li><a href="/triangle">Triangle</a></li>' \
           '<li><a href="/square">Square</a></li>' \
           '</ol>'


@app.route('/triangle', methods=['GET', 'POST'])
def route_triangle():
    t1 = Triangle(40, 4)
    return '<h1>Triangle</h1>' + str(t1.triangle_area())


app.run(debug=True, host='0.0.0.0', port=8000)
