from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Toronto',
  'salary': 350000
}, {
  'id': 2,
  'title': 'Information Scientist',
  'location': 'Manitoba',
  'salary': 150000
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'Los Angeles',
  'salary': 450000
}, {
  'id': 4,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': 270000
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
