from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'youtube-manager-secret'

DATA_FILE = 'youtube_videos.txt'

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            videos = json.load(file)
            return videos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data(videos):
    with open(DATA_FILE, 'w') as file:
        json.dump(videos, file)

@app.route('/')
def index():
    videos = load_data()
    return render_template('index.html', videos=videos)

@app.route('/add', methods=['GET', 'POST'])
def add_video():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        time = request.form.get('time', '').strip()
        
        if name and time:
            videos = load_data()
            videos.append({
                'name': name,
                'time': time,
            })
            save_data(videos)
            return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_video(index):
    videos = load_data()
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        time = request.form.get('time', '').strip()
        
        if 1 <= index <= len(videos) and name and time:
            videos[index-1] = {
                'name': name,
                'time': time,
            }
            save_data(videos)
            return redirect(url_for('index'))
    
    if 1 <= index <= len(videos):
        video = videos[index-1]
        return render_template('update.html', video=video, index=index)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_video(index):
    videos = load_data()
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
