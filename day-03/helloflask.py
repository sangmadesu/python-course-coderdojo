from flask import Flask, request
from geometry.triangle import Triangle
from geometry.square import Square
from geometry.circle import Circle


application = Flask(__name__)


@application.route('/')
def index():
	return 'Hello World!'


@application.route('/segitiga', methods=['GET', 'POST'])
def triangleArea():
	bottom = int(request.args.get('bottom'))
	height = int(request.args.get('height'))

	# print bottom, height 
	triArea = Triangle(bottom, height)
	result = triArea.triangle_area()
	return 'Luas segitiga jika alas = ' + str(bottom) + ' dan tinggi = ' + str(height) + ' adalah ' + str(result)
	# print result



@application.route('/bujursangkar', methods=['GET', 'POST'])
def squareArea():
	sqrArea = Square(10)
	result = sqrArea.square_area()
	return 'Luas bujursangkar jika sisi = 10 adalah ' + str(result)


@application.route('/lingkaran', methods=['GET', 'POST'])
def circleArea():
	circArea = Circle(5)
	result = circArea.circle_area()
	return 'Luas lingkaran jika jari-jari = 5 adalah ' + str(result)
	

if __name__ == '__main__':
	application.run(debug=True, host='0.0.0.0', port=8888)
