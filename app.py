from flask import Flask, render_template, request
from pushdb_comment import send_comment
from get_comment import getComment

app = Flask(__name__)

@app.route('/comment', methods= ['POST', 'GET'])
def commentFunc():
	if request.method == 'POST':

		username = request.form.get('name')
		email = request.form.get('email')
		comment = request.form.get('comment')
		send_comment(username, email, comment)

		return 'comment successfully created'

	else:
		return render_template('comment.html')

@app.route('/getcomment')
def getcomment():
	comments = getComment()
	return render_template('show_comments.html', comments=comments)


if __name__ == '__main__':
	app.run(debug=True)