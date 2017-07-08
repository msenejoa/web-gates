# Test Message
#second
from flask import Flask, Response, json, jsonify, request
from flask_bootstrap import Bootstrap
from flask import render_template
from flask import send_file
import values as v


app = Flask(__name__)
Bootstrap(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/submit_gates", methods = ['GET', 'POST'])
def submit():
    #grabs the values from the html page and assigns them to a variable
    tray_name = request.form['tray_name']
    mac_num = int(request.form['mac_num'])
    build_temp = float(request.form['build_temp'])
    beam_offset = float(request.form['beam_offset'])
    x_scale = float(request.form['xscale'])
    y_scale = float(request.form['yscaling'])
    humidity = float(request.form['humidity'])
    outside_temp = float(request.form['outside_temp'])
    r_thick_one = float(request.form['r_thick_one'])
    r_thick_six = float(request.form['right_thick_six'])
    r_val_1 = float(request.form['r_val_1'])
    r_val_2 = float(request.form['r_val_2'])
    r_val_3 = float(request.form['r_val_3'])
    r_val_4 = float(request.form['r_val_4'])
    r_val_5 = float(request.form['r_val_5'])
    r_val_6 = float(request.form['r_val_6'])
    l_thick_one = float(request.form['l_thick_one'])
    l_thick_six = float(request.form['l_thick_six'])
    l_val_1 = float(request.form['l_val_1'])
    l_val_2 = float(request.form['l_val_2'])
    l_val_3 = float(request.form['l_val_3'])
    l_val_4 = float(request.form['l_val_4'])
    l_val_5 = float(request.form['l_val_5'])
    l_val_6 = float(request.form['l_val_6'])

    #average values and add to database
    v.Gates(tray_name, mac_num, build_temp, beam_offset, x_scale, y_scale, humidity, outside_temp, r_thick_one, r_thick_six, r_val_1, r_val_2, r_val_3, r_val_4, r_val_5, r_val_6, l_thick_one, l_thick_six, l_val_1, l_val_2, l_val_3, l_val_4, l_val_5, l_val_6)


    return render_template("index.html")

@app.route("/graph", methods = ['GET', 'POST'])
def graphs():
    #reads the values to pass to the html document
    avg = v.read_values(10)
    average_10 = avg[0]
    quality_10 = avg[1]
    qa_date_10 = avg[2]
    thick_10 = avg[3]

    avg = v.read_values(15)
    average_15 = avg[0]
    quality_15 = avg[1]
    qa_date_15 = avg[2]
    thick_15 = avg[3]
    return render_template("graphs.html", average_10 = average_10, quality_10 = quality_10, date_10 = qa_date_10, thick_10 = thick_10, average_15 = average_15, quality_15 = quality_15, date_15 = qa_date_15, thick_15 = thick_15)


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=12345)