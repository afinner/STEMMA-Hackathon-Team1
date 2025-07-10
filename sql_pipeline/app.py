from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    return psycopg2.connect(
        dbname="stemma_db_copy", 
        user="postgres", 
        password="andrewroot", 
        host="localhost"
    )

# Route to serve the main HTML dashboard
@app.route('/')
def index():
    return render_template('index.html')

# API for search functionality
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple search query (modify to match your database schema)
    cursor.execute("SELECT * FROM your_table WHERE name LIKE %s", (f'%{query}%',))
    results = cursor.fetchall()
    
    # Convert results to a dictionary for easier handling on the front-end
    columns = [desc[0] for desc in cursor.description]
    result_dict = [dict(zip(columns, row)) for row in results]
    
    # Close the connection
    cursor.close()
    conn.close()
    
    # Return the filtered data as JSON
    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(debug=True)