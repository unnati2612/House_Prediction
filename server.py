from flask import Flask, request, jsonify, render_template
import util

print("➡️ File started executing...")  # DEBUG line

app = Flask(__name__, template_folder='../client')  # 👈 Pointing to client folder
print("✅ Flask app created")  # DEBUG line


@app.route('/')
def home():  # 👈 NEW: Serve the HTML page
    print("🏠 / route called — serving index.html")
    return render_template('index.html')


@app.route('/get_location_names')
def get_location_names():
    print("📍 /get_location_names called")
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    print("📍 /predict_home_price called")
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    try:
        util.load_saved_artifacts()
        print("🎉 Artifacts loaded successfully!")
    except Exception as e:
        print("❌ Error loading artifacts:", e)

    print("🔥 Running Flask app now...")
    app.run(debug=True)
