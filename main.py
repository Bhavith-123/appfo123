from flask import *

app = Flask(__name__)  
 
app.secret_key = 'sha256hueolzbsvkeflaskhbsjsaooipp'

@app.route('/')  
def index():  
    return redirect('default/user/login/index')
 
@app.route('/default/user/login/index')  
def login():  
    return render_template('login.html')

@app.route('/home')  
def home():  
    return render_template('index.html')

@app.route('/validate/user/index', methods = ['GET', 'POST'])
def validate():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin@123':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('home'))

   return render_template('login.html', error = error)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
