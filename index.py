import sqlite3 as db
from bottle import route, run, template, request

# Index page - displays login page
@route('/', method='GET')
def index():
    return template('login')

# Validates login info from index page
@route('/login',method=['GET', 'POST'])
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    
    conn = db.connect('travel_expenses.db')   
    cur = conn.cursor()

    sql = "SELECT * FROM members WHERE username = ? and password = ?" 
    cur.execute(sql, (username, password))
    result = cur.fetchone()

    if result:
        return template('menu')
    else:
        return template('error')

# Displays add trip form and posts data to db    
@route('/addTrip', method=['GET', 'POST'])
def addTrip():
    if request.method == 'GET':
        return template ('addTrip')
    else:
        user = request.forms.get('user')
        date = request.forms.get('date')
        dest = request.forms.get('dest')
        miles = request.forms.get('miles')
        gallons = request.forms.get('gallons')
        
        try:
            conn = db.connect('travel_expenses.db')   
            cur = conn.cursor()
            
            data = (None, user, date, dest, miles, gallons)
            sql = "INSERT INTO trips VALUES (?, ?, ?, ?, ?, ?)"
            cur.execute(sql, data)
            conn.commit()
            cur.close()
            
            msg = {'msg' : 'Trip successfully added'}
            return template('status', msg)
        except: 
            msg = {'msg' : 'Error adding Trip'}
            return template('status', msg)
        finally: 
            conn.close()

# Displays prompt for username, then displays that users trips
@route('/viewTrips', method=['GET', 'POST'])
def viewTrips():
    if request.method == 'GET':
        return template ('enterUsername')
    else:
        username = request.forms.get('username')
        
        conn = db.connect('travel_expenses.db')   
        cur = conn.cursor()
        
        sql = "SELECT * FROM trips WHERE username = ?"
        cur.execute(sql,(username, ))
        trips = cur.fetchall()
        
        data = {'username': username, 'rows':trips}
        return template('trips', data)

@route('/menu')
def menu():
    return template('menu')
    
run(host='localhost', port=8081)