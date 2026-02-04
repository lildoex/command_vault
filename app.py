from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

    # Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cmd = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            "id": self.id, 
            "cmd": self.cmd, 
            "description": self.description
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/commands', methods=['GET'])
def get_commands():
    all_commands = Command.query.all()
    return jsonify([c.to_dict() for c in all_commands])

@app.route('/api/commands', methods=['POST'])
def add_command():
    data = request.get_json()
    new_command = Command(
        cmd=data['cmd'], 
        description=data['description']
    )
    db.session.add(new_command)
    db.session.commit()
    return jsonify(new_command.to_dict()), 201

@app.route('/api/commands/<int:command_id>', methods=['DELETE'])
def delete_command(command_id):
    command = Command.query.get(command_id)
    if command:
        db.session.delete(command)
        db.session.commit()
        return jsonify({"message": "Command deleted"}), 200
    return jsonify({"error": "Command not found"}), 404

@app.route('/api/commands/<int:command_id>', methods=['PUT'])
def update_command(command_id):
    command = Command.query.get(command_id)
    if not command:
        return jsonify({"error": "Not found"}), 404

    data = request.get_json()
    
    # Ladicí výpis do terminálu - uvidíš, co Python přijal
    print(f"Updating ID {command_id} with data: {data}")

    command.cmd = data['cmd']
    command.description = data['description'] # Musí odpovídat tvému modelu!

    db.session.commit() # Bez tohoto se nic v souboru .db nezmění
    return jsonify(command.to_dict())



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
