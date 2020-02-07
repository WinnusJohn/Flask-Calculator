from flask import Flask, render_template, request
app = Flask(__name__)

p1 = ''
p2 = ''
op = ''
sub_param = "" 
ans = None
@app.route("/")
def index():

	print('\n\n', request.args.get("num"), '\n\n')
	# print('\n\n', request.args.get("operator"), '\n\n')


	number = request.args.get("num")
	operator = request.args.get('operator')



           
	return render_template("index.html", ans=ans, sub_param=number, operator=operator)


	# operator = request.form['operator']

	# if operator == 'plus':
	# 	plus = float(num0) + float(num1) + float(num2) + float(num3) + float(num4) + float(num5) + float(num6) + float(num7) + float(num8) + float(num9)
	# 	return render_template('index.html', sum=sum)

	# elif operator == 'subtract':
	# 	subtract = float(num0) - float(num1) - float(num2) - float(num3) - float(num4) - float(num5) - float(num6) - float(num7) - float(num8) - float(num9)
	# 	return render_template('index.html', sum=sum)

	# elif operator == 'multiply':
	# 	subtract = float(num0) * float(num1) * float(num2) * float(num3) * float(num4) * float(num5) * float(num6) * float(num7) * float(num8) * float(num9)
	# 	return render_template('index.html', sum=sum)

	# elif operator == 'division':
	# 	subtract = float(num0) / float(num1) / float(num2) / float(num3) / float(num4) / float(num5) / float(num6) / float(num7) / float(num8) / float(num9)
	# 	return render_template('index.html', sum=sum)

	# else:
	# 	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)


	# @app.route('/operate')
# def operate(sum=sum):


# 	number = request.args.get("num")
# 	param1 = request.args.get("field1")
# 	param2 = request.args.get("field2")
# 	operator = request.args.get('operator')

	# equalto

	# if request.method == 'POST':
		#Start pulling data from form input
		# num0 = request.form['num0']
		# num1 = request.form['num1']
		# num2 = request.form['num2']
		# num3 = request.form['num3']
		# num4 = request.form['num4']
		# num5 = request.form['num5']
		# num6 = request.form['num6']
		# num7 = request.form['num7']
		# num7 = request.form['num8']
		# num9 = request.form['num9']