from flask import Flask, render_template, request, redirect
from hashlib import sha256
import wombat 
from wombat import pt,ct

#Flask api to interact with html pages
app = Flask(__name__)

#home page route where voter can designate who they are voting for
@app.route('/', methods=['GET','POST'])
def index():
	return render_template('wombat.html')

#once the voter submits their vote, the vote will get encrypted via El Gamal encryption
@app.route('/submitted', methods=['POST'])
def encrypt():
	data = request.form.get('vote')
	print(data)
	res = wombat.encryptVote(data)

	ct = res[1]

	#compute sha-256 hash of encrypted plaintext to serve as receipt for voter
	h = sha256()
	h.update(ct.encode('ASCII'))
	hashed = h.hexdigest()

	return render_template('audit.html', vote=res[0], encrypted=hashed)

#If the voter chooses to audit their ballot, the machine will check that the 
#decrypted ciphertext matches the plaintext
@app.route('/audit', methods=['POST'])
def audit():
	result = wombat.auditVote()
	print(result)

	#if audit fails -> error page
	if result != True:
		return redirect("http://localhost:5000/error")
	
	return render_template('passedAudit.html')

#If the voter does not audit their ballot, their vote will successfully be cast
@app.route('/success', methods=['POST'])
def success():
	return render_template('success.html')

#If the audit fails, the voter will be notified of the error
@app.route('/error', methods=['POST'])
def error():
	return render_template('failedAudit.html')

if __name__ == '__main__':
	app.run()