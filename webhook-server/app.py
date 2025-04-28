from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    try:
        data = request.get_json(force=True)
        print("Received Alert:", data)

        # You can add a condition if you want to trigger Ansible only on real alerts
        subprocess.run(["ansible-playbook", "/ansible/restart-nginx.yml"])
        return jsonify({"message": "Alert received and playbook triggered"}), 200

    except Exception as e:
        print("Error processing alert:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
