from flask import Flask, jsonify, render_template, send_from_directory
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__, static_folder='static')

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="asritha@2002",
        database="education_site"
    )

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/subjects')
def get_subjects():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM subjects")
        subjects = cursor.fetchall()
        return jsonify(subjects)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/lessons/<int:subject_id>')
def get_lessons(subject_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM lessons 
            WHERE subject_id = %s 
            ORDER BY lesson_number
        """, (subject_id,))
        lessons = cursor.fetchall()
        return jsonify(lessons)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/topics/<int:subject_id>/<int:lesson_number>')
def get_topics(subject_id, lesson_number):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM Topics_info 
            WHERE subject_id = %s AND lesson_number = %s
            ORDER BY Topic_id
        """, (subject_id, lesson_number))
        topics = cursor.fetchall()
        return jsonify(topics)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/content/<int:subject_id>/<int:lesson_number>/<int:topic_id>')
def get_content(subject_id, lesson_number, topic_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM Info 
            WHERE subject_id = %s AND lesson_number = %s AND Topic_id = %s
        """, (subject_id, lesson_number, topic_id))
        content = cursor.fetchone()
        return jsonify(content)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)