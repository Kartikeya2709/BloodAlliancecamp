from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

donors = []  # In-memory donor list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        if not (name and age and blood_group and contact):
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_donor'))
        donors.append({'Name': name, 'Age': age, 'Blood Group': blood_group, 'Contact': contact})
        flash('Donor added successfully!', 'success')
        return redirect(url_for('view_donors'))
    return render_template('add.html')

@app.route('/donors')
def view_donors():
    return render_template('donors.html', donors=donors)

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        blood_group = request.form['blood_group']
        results = [d for d in donors if d['Blood Group'].lower() == blood_group.lower()]
    return render_template('search.html', results=results)

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_donor(index):
    if index < 0 or index >= len(donors):
        flash('Invalid donor index!', 'danger')
        return redirect(url_for('view_donors'))
    donor = donors[index]
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        if not (name and age and blood_group and contact):
            flash('All fields are required!', 'danger')
            return redirect(url_for('update_donor', index=index))
        donors[index] = {'Name': name, 'Age': age, 'Blood Group': blood_group, 'Contact': contact}
        flash('Donor updated!', 'success')
        return redirect(url_for('view_donors'))
    return render_template('update.html', donor=donor, index=index)

@app.route('/delete/<int:index>')
def delete_donor(index):
    if index < 0 or index >= len(donors):
        flash('Invalid donor index!', 'danger')
    else:
        donors.pop(index)
        flash('Donor deleted!', 'success')
    return redirect(url_for('view_donors'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/awareness')
def awareness():
    return render_template('awareness.html')

@app.route('/events')
def events():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
