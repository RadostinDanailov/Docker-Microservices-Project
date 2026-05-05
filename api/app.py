from flask import Flask, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.get("/hello")
def hello():
    r.set("name", "Radostin")
    name = r.get("name").decode()
    return jsonify(message=f"Hello {name}, your microservice works!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
