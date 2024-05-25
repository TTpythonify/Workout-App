from flask import Blueprint,render_template,request
import requests 


workout_bp= Blueprint('workout_bp', __name__,template_folder= 'templates')

@workout_bp.route('/', methods=['POST','GET'])
def main():
    results=""
    if request.method == 'POST':
        workout_target = request.form.get('workout-target')
        results = find_workout(workout_target)
        print(results)
    
    return render_template("workout.html",results=results, total_results=len(results))



def find_workout(bodypart):
    url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{bodypart}"
    result = []

    headers = {
        "X-RapidAPI-Key": "1ae4654528msh82cf9d56f299a41p175eb1jsnebd34a46be13", # Replace with new API key
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response_json = response.json() # Convert to dictionary 

        if not response_json:
            result.append({'error': "No result found"})
        else:
            # Storing each item as a dictionary 
            for item in response_json:
                workout = {
                    'name': item.get('name', 'Name unavailable'),
                    'gifUrl': item.get('gifUrl', 'Gif unavailable'),
                    'equipment': item.get('equipment', 'Equipment unavailable'),
                    'target': item.get('target', 'Target unavailable'),
                    'instructions': item.get('instructions', 'Instructions unavailable')
                }
                result.append(workout)

    except Exception as e:
        result.append({'error': str(e)})

    return result # Return the result