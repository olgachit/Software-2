#1 Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not. Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.
from flask import Flask
app = Flask(__name__)

def is_prime(n):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/prime_number/<int:number>')
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return result

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=5000)

#2 Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
from flask import Flask
import mysql.connector

app = Flask(__name__)

connection=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='Relational_database',
    user='olgachit',
    password='OLga123!',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )

@app.route('/airport/<ICAO>')
def fetch_airport_info(ICAO):
    cursor=connection.cursor()
    query = "SELECT name, municipality FROM airport WHERE ident=%s"
    cursor.execute(query, (ICAO,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    result = {
        "ICAO": ICAO,
        "Name": result[0],
        "Location": result[1]
    }
    return result

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=5000)
