from flask import Blueprint,  render_template

views = Blueprint('views', __name__)

@views.route('/home')
@views.route('/')
def home():
    #logo_image = os.path.join(app.config['UPLOAD_FOLDER'], 'spy.jpg')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)