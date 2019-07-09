from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/<num_of_box>/<color>')
def index(num_of_box, color):
    boxes = int(num_of_box)
    selected_color = color
    return render_template("index.html", boxes = int(num_of_box), selected_color = color)
if __name__=="__main__":
    app.run(debug=True)