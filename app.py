from flask import Flask, render_template, redirect
import random
import os
import glob

app = Flask(__name__)

@app.route('/')
def index():
    moc_image_paths = [f"/static/data/MOC{str(i).zfill(4)}.png" for i in range(133)]
    mod_image_paths = [f"/static/data/MOD{str(i).zfill(4)}-{str(j)}.png" for i in range(0, 133) for j in range(8)]

    random.shuffle(moc_image_paths)
    random.shuffle(mod_image_paths)

    selected_paths = []
    selected_paths.append(moc_image_paths.pop())

    # answer_image = (f"/static/data/MOC{str(i).zfill(4)}.png" for i in range(133))

    for _ in range(8):
        selected_paths.append(mod_image_paths.pop())

    context = {"answer_image": selected_paths[0]}
    random.shuffle(selected_paths)

    for i, path in enumerate(selected_paths):
        vae_name = f"path{i+1}"
        context[vae_name] = path

    return render_template('index.html', **context)


@app.route('/correct')
def correct():
    return render_template('correct.html')


@app.route('/wrong')
def wrong():
    return render_template('wrong.html')


@app.route('/logout')
def logout():
    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)