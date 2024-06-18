from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/components')
def components():
    return render_template('components.html')

@app.route('/components/cpu')
def components_cpu():
    return render_template('components_cpu.html')

@app.route('/components/gpu')
def components_gpu():
    return render_template('components_gpu.html')

@app.route('/components/ram')
def components_ram():
    return render_template('components_ram.html')

@app.route('/components/storage')
def components_storage():
    return render_template('components_storage.html')

@app.route('/components/motherboard')
def components_motherboard():
    return render_template('components_motherboard.html')

@app.route('/components/power')
def components_power():
    return render_template('components_power.html')

@app.route('/components/case')
def components_case():
    return render_template('components_case.html')


@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/videos/reviews')
def videos_reviews():
    return render_template('videos_reviews.html')

@app.route('/videos/tutorials')
def videos_tutorials():
    return render_template('videos_tutorials.html')

@app.route('/videos/new')
def videos_new_releases():
    return render_template('videos_new_releases.html')


if __name__ == '__main__':
    app.run(debug=True)
