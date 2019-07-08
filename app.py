import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename
from services.count_areas import colour_counter
from services.img_bin_converter import png_to_ints

UPLOAD_FOLDER = './uploads'
if not os.path.isdir('./uploads'):
    os.mkdir('./uploads')

ALLOWED_EXTENSIONS = {'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
socketio = SocketIO(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser will
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('show_result',
                                    filename=filename))
    return render_template('index.html')

@app.route('/result/<filename>', methods=['GET', 'POST'])
def show_result(filename):
    matrix = png_to_ints(UPLOAD_FOLDER + '/' + filename)
    result = colour_counter(matrix, matrix.shape)
    return '''<!doctype html>
                <title>Colour Counter</title>
                <head>
                </head>
                <h1>The number of colours is: </h1>
                <pre>''' + str(result) + '</pre>' + '''
                <img src="/uploads/''' + filename + '">'


if __name__ == '__main__':
    print('* Running Colour Counter Service on http://127.0.0.1:5000/')
    socketio.run(app)
