from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from forms import Answer

app =  Flask(__name__)
app.config['SECRET_KEY'] = 'asdfgasd2gfsdf3g3s1dfg313d2f1v3s20dff3gs1try3gs3fd21vsdfgvdfgws63fg63'

@app.route('/', methods=['POST','GET'])
def home():
	answers = []
	result = []
	form = Answer()
	if form.validate_on_submit():
		print('submitted')
		q1 = request.form.get('q_1')
		q2 = request.form.get('q_2')
		q3 = request.form.get('q_3')
		q4 = request.form.get('q_4')
		q5 = request.form.get('q_5')
		q6 = request.form.get('q_6')
		q7 = request.form.get('q_7')
		q8 = request.form.get('q_8')
		q9 = request.form.get('q_9')
		q10 = request.form.get('q_10')
		
		answers.append([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10])
		ans = answers[0]
		print(ans)
		if ans[0] == 'মিথ্যা':
			result.append('Correct')
		else:
			result.append('inorrect')
		if ans[1] == 'মিথ্যা':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[2] == 'সত্য':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[3] == 'মিথ্যা':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[4] == 'মিথ্যা':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[5] == 'মিথ্যা':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[6] == 'সত্য':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[7] == 'সত্য':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[8] == 'সত্য':
			result.append('Correct')
		else:
			result.append('incorrect')
		if ans[9] == 'মিথ্যা':
			result.append('Correct')
		else:
			result.append('incorrect')
		print(result)
		marks = result.count('Correct')
		# return ('Your marks is {}/10'.format(str(marks)))
		return render_template('result.html', marks=marks, ans=ans, result=result)
	else:
		print('not submitted')
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run()
	# app.run(host='0.0.0.0',debug=True)