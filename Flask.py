from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# In-memory database (for simplicity)
# books = [
#     {"id": 1, "title": "The Psychology of Money", "author": "Morgan Housel"},
#     {"id": 2, "title": "Ikigai", "author": "Francesc Miralles"},
#     {"id": 3, "title": "The Power of your subconscious mind", "author": "Joseph Murphy"}
# ]

data = json.load(open("data.json", "r"))["cars"]

#Route to get all car
@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(data)

# Route to get a single book by id
@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    car = next((car for car in data if car['id'] == id), None)
    if car:
        return jsonify(car)
    else:
        return jsonify({"error": "Car not found"}), 404
    
# Route to add a new car
@app.route('/cars', methods=['POST'])
def add_car():
    new_car = request.json
    new_car['id'] = len(data) + 1
    data.append(new_car)
    return jsonify(new_car), 201

# Route to update an existing car
@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    car = next((car for car in data if car['id'] == id), None)
    if data:
        req_data = request.json
        car.update(req_data)
        return jsonify(car)
    return jsonify({"error": "Car not found"}), 404

# Route to delete a car by id
@app.route('/cars/<int:id>', methods=["DELETE"])
def delete_car(id):
    global data
    data = [car for car in data if car['id'] != id]
    return jsonify({"message": "Car deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

    