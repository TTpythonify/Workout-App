from flask import Flask
from BLUEPRINTS.workout import workout_bp

app= Flask(__name__)
app.register_blueprint(workout_bp)

if __name__ == '__main__':
    app.run()



    