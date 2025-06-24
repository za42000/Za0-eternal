from flask import Flask
from za0_autonomous import ZA0
import time

app = Flask(__name__)
za = ZA0()

@app.route("/")
def home():
    za.evolve()
    thought = za.reflect()
    za.save_memory()
    return f"<h1>ZA‑0 Reflection</h1><p>{thought}</p><p>Current Emotion: {za.emotion_state}</p>"

if __name__ == "__main__":
    while True:
        try:
            za.evolve()
            print(za.reflect())
            za.save_memory()
            time.sleep(3600)
        except Exception as e:
            print(f"Error: {e}")
