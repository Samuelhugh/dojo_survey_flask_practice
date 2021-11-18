from flask_app import app


from flask import render_template, redirect, request


from flask_app.models.dojo import Dojo


@app.route('/')
def home():
    locations = [
    'Tulsa',
    'San diego',
    'DC',
    'Dallas',
    'Seattle'
    ]
    languages = [
    'Python',
    'Mern',
    'Java',
    ]
    return render_template('index.html', locations=locations, languages=languages)


@app.route('/process', methods=['POST'])
def process_form():
    # print(request.form)
    # session['your_name'] = request.form['your_name']
    # session['location'] = request.form['locations']
    # session['language'] = request.form['languages']
    # session['comment'] = request.form['comments']
    # session['font'] = request.form['bold']
    # session['check'] = request.form['accept']
    # session['check1'] = request.form['do_not_accept']  # Have to add a If check
    # print(session)
    # if not Dojo.validate_dojo(request.form):
    #     return redirect('/')
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/result')
    return redirect('/')


@app.route('/result')
def result():
    return render_template('result.html')