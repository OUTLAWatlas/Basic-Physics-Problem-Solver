from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle problem selection
@app.route('/solve', methods=['POST'])
def calculate_problem():
    problem_type = request.form['problem_type']
    
    if problem_type == 'projectile':
        return redirect(url_for('projectile'))
    elif problem_type == 'forces':
        return redirect(url_for('forces'))
    elif problem_type == 'electromagnetism':
        return redirect(url_for('electromagnetism'))
    elif problem_type == 'optics':
        return redirect(url_for('optics'))
    elif problem_type == 'electric_field':
        return redirect(url_for('electric_field'))
    else:
        return redirect(url_for('home'))  # If no problem type is selected, go back to home

# Route for the projectile problem page
@app.route('/projectile', methods=['GET', 'POST'])
def projectile():
    result = None
    if request.method == 'POST':
        # Placeholder for actual calculation logic
        result = "Projectile calculation result"
    return render_template('projectile.html', result=result)

# Route for the forces problem page
@app.route('/forces', methods=['GET', 'POST'])
def forces():
    result = None
    if request.method == 'POST':
        # Placeholder for actual calculation logic
        result = "Forces calculation result"
    return render_template('forces.html', result=result)

# Route for the electromagnetism problem page
@app.route('/electromagnetism', methods=['GET', 'POST'])
def electromagnetism():
    result = None
    if request.method == 'POST':
        # Placeholder for actual calculation logic
        result = "Electromagnetism calculation result"
    return render_template('electromagnetism.html', result=result)

# Route for the optics problem page
@app.route('/optics', methods=['GET', 'POST'])
def optics():
    result = None
    if request.method == 'POST':
        # Placeholder for actual calculation logic
        result = "Optics calculation result"
    return render_template('optics.html', result=result)

# Route for the electric field problem page
@app.route('/electric_field', methods=['GET', 'POST'])
def electric_field():
    result = None
    if request.method == 'POST':
        # Placeholder for actual calculation logic
        result = "Electric field calculation result"
    return render_template('electric_field.html', result=result)

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
