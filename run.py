from flask import Flask,render_template,jsonify
app=Flask(__name__)
LISTVAL=[
{
  'id':678901,
  'title':'Nurse',
  'Location':'Kolkata,India',
  'Salary':'Rs.25000'
},
{
  'id':678100,
  'title':'Ambulance Driver',
  'Location':'Chennai,India',
  'Salary':'Rs.20000'
},
{
  'id':678902,
  'title':'Physican',
  'Location':'Toronto,Canada',
  'Salary':'CAD 100000'
},
{
  'id':678945,
  'title':'Dermotologist',
  'Location':'Newjersey,USA',
  'Salary':'USD 120000'
}
]
@app.route('/')
def hello_world():
  return render_template('home.html',jobs=LISTVAL,company='Practitioner')

@app.route('/LISTVAL')
def list_jobs():
  return jsonify(LISTVAL)

if( __name__ == '__main__'):
  app.run(host='0.0.0.0',debug=True)