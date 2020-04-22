from flask import Flask, render_template, request, redirect, g
from hashlib import sha256
import wombat 
from wombat import pt,ct

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('wombat.html')

@app.route('/submitted', methods=['POST'])
def encrypt():
	data = request.form.get('vote')
	print(data)
	res = wombat.encryptVote(data)

	g.pt = res[0]
	g.ct = res[1]
	ct = res[1]

	h = sha256()
	h.update(ct.encode('ASCII'))
	hashed = h.hexdigest()

	return render_template('audit.html', vote=res[0], encrypted=hashed)

@app.route('/audit', methods=['POST'])
def audit():
	result = wombat.auditVote()
	print(result)
	if result != True:
		return redirect("http://localhost:5000/error")
	
	return render_template('passedAudit.html')

@app.route('/success', methods=['POST'])
def success():
	return render_template('success.html')

@app.route('/error', methods=['POST'])
def error():
	return render_template('failedAudit.html')
	
if __name__ == '__main__':
	app.run()