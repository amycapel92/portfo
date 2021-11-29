from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('webserver/database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='', encoding='utf-8') as csv_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            write_to_csv(request.form.to_dict())
            return redirect('thankyou.html')
        except:
            return 'did not save to database... try again'
    else:
        return 'something went wrong... try again'
