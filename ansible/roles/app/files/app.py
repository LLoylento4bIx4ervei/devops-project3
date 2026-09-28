from flask import Flask, jsonify
import os
import psycopg2


app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'counter_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'secret')

def db_connect():
	conn = psycopg2.connect(
	host = DB_HOST,
	database = DB_NAME,
	user = DB_USER,
	password = DB_PASS
)
	return conn

def db_init():
	conn = db_connect()
	cur = conn.cursor()
	cur.execute(
	""" CREATE TABLE IF NOT EXISTS counter(
	id SERIAL PRIMARY KEY,
	value INTEGER DEFAULT 0 
);
""")
	cur.execute("INSERT INTO counter (value) SELECT 0 WHERE NOT EXISTS (SELECT 1 FROM counter);")
	conn.commit()
	cur.close()
	conn.close()

@app.route("/")
def index():
	return '<h1>DevOps Project 2</h1><p><a href="/api/counter">/api/counter</a></p>'

@app.route("/api/counter", methods=["GET"])
def get_counter():
	conn = db_connect()
	cur = conn.cursor()
	cur.execute("UPDATE counter SET value = value + 1 RETURNING value;")
	new_value = cur.fetchone()[0]
	conn.commit()
	cur.close()
	conn.close()
	return jsonify({'counter': new_value})

if __name__ == '__main__':
	db_init()
	app.run(host='0.0.0.0', port=5000) 	
