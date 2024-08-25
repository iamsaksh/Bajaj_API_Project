from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# User information
USER_ID = "saksham_gupta_01012000"  # Format: fullname_ddmmyyyy


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get("data", [])

    # Process input data
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets, default="")

    # Prepare the response
    response = {
        "is_success": True,
        "user_id": USER_ID,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

    return jsonify(response)


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    # Return HTTP Status Code 200
    return jsonify({"operation_code": 1}), 200


if __name__ == '__main__':
    app.run(debug=True)
