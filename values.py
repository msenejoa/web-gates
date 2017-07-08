from numpy import mean
import sqlite3
import csv


"""
c.execute('''CREATE TABLE results
             (tray_name text, date text, mac_num real, build_temp real, beam_offset real, x_scaling real, y_scaling real, humidity real, outside_temp real, right_thick_1 real, right_thick_6 real, left_thick_1 real, left_thick_6 real, right_average real, left_average real, machine_average real)''')
"""

class Gates:
    def __init__(self, tray_name, mac_num, build_temp, beam_offset, x_scaling, y_scaling, humidity, outside_temp, right_thick_1, right_thick_6, one_r, two_r, three_r, four_r, five_r, six_r, left_thick_1, left_thick_6, one_l, two_l, three_l, four_l, five_l, six_l):
        self.tray_name = tray_name
        self.mac_num = mac_num
        self.build_temp = build_temp
        self.beam_offset = beam_offset
        self.x_scaling = x_scaling
        self.y_scaling = y_scaling
        self.humidity = humidity
        self.outside_temp = outside_temp
        self.right_thick_1 = right_thick_1
        self.right_thick_6 = right_thick_6
        self.one_r = one_r
        self.two_r = two_r
        self.three_r = three_r
        self.four_r = four_r
        self.five_r = five_r
        self.six_r = six_r
        self.left_thick_1 = left_thick_1
        self.left_thick_6 = left_thick_6
        self.one_l = one_l
        self.two_l = two_l
        self.three_l = three_l
        self.four_l = four_l
        self.five_l = five_l
        self.six_l = six_l

        #grab tray date from name
        d = self.tray_name
        self.date = d[:4] + '-' + d[4:6] + '-' + d[6:8]


        #takes machine averages

        self.right_avg = self.average(self.one_r, self.two_r, self.three_r, self.four_r, self.five_r, self.six_r)
        self.left_avg = self.average(self.one_l, self.two_l, self.three_l, self.four_l, self.five_l, self.six_l)
        self.machine_average = self.total_avg(self.right_avg, self.left_avg)

        #writes to database

        self.write_values(self.tray_name, self.date, self.mac_num, self.build_temp, self.beam_offset, self.x_scaling, self.y_scaling, self.humidity, self.outside_temp, self.right_thick_1, self.right_thick_6, self.left_thick_1, self.left_thick_6, self.right_avg, self.left_avg, self.machine_average)


    def average(self, a, b, c, d, e, f):
        list = [a, b, c, d, e, f]
        return(mean(list))

    def total_avg(self, a, b):
        list = [a, b]
        return(mean(list))


    def write_values(self, tray_name, date, mac_num, build_temp, beam_offset, x_scaling, y_scaling, humidity, outside_temp, right_thick_1, right_thick_6, left_thick_1, left_thick_6, right_avg, left_avg, machine_average):
        path = 'Gates.db'
        conn = sqlite3.connect(path)
        c = conn.cursor()

        values = (tray_name, date, mac_num, build_temp, beam_offset, x_scaling, y_scaling, humidity, outside_temp, right_thick_1, right_thick_6, left_thick_1, left_thick_6, right_avg, left_avg, machine_average)
        c.execute("INSERT INTO results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

        conn.commit()
        conn.close()



def read_values(mac_num):
    path = 'Gates.db'
    fp = open('static/mac_%s.csv' %mac_num, 'w')
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("select date, right_average, left_average, machine_average from results where mac_num = {machine} and tray_name not like '%QA%' order by date desc".format(machine = mac_num))
    rows = c.fetchall()
    myFile = csv.writer(fp, lineterminator='\n')
    myFile.writerow(['Date','Right','Left','Average'])
    for row in rows:
        myFile.writerow(row)
    fp.close()

    fp = open('static/mac_%s_quality.csv' %mac_num, 'w')
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("select date, right_average, left_average, machine_average from results where mac_num = {machine} and tray_name like '%QA%' order by date desc".format(machine = mac_num))
    rows = c.fetchall()
    myFile = csv.writer(fp, lineterminator='\n')
    myFile.writerow(['Date','Right','Left','Average'])
    for row in rows:
        myFile.writerow(row)
    fp.close()

    c.execute("select AVG(p.machine_average) from(select date, machine_average from results where mac_num = {machine} and tray_name not like '%QA%' order by date desc limit 5) as p".format(machine = mac_num))
    average_value = c.fetchall()
    average_value = round(average_value[0][0], 2)


    c.execute("select AVG(p.machine_average) from(select date, machine_average from results where mac_num = {machine} and tray_name like '%QA%' order by date desc limit 5) as p".format(machine = mac_num))
    quality_value = c.fetchall()
    print(quality_value)
    quality_value = round(quality_value[0][0], 2)

    c.execute("select date from results where mac_num = {machine} and tray_name  like '%QA%' order by date desc limit 1".format(machine = mac_num))
    last_qa = c.fetchall()
    last_qa = last_qa[0][0]
    print last_qa
    last_qa = last_qa[5:7] + "/" + last_qa[8:10]
    print last_qa


    c.execute("select avg(p.avg) from(select (right_thick_1 + right_thick_6 + left_thick_1 + left_thick_6)/4 as avg from results where mac_num = 10 and tray_name not like '%QA%' order by date desc limit 5) as p".format(machine=mac_num))
    thickness = c.fetchall()
    thickness = round(thickness[0][0], 2)

    return average_value, quality_value, last_qa, thickness
"""
    def write_values(self, tray_name, date, mac_num, build_temp, beam_offset, x_scale, y_scale, humidity, outside_temp, r_thick_one, r_thick_six, l_thick_one, l_thick_six, right_avg, left_avg, machine_average):
        values = (self.tray_name, self.date, self.mac_num, self.build_temp, self.beam_offset, self.x_scale, self.y_scale, self.humidity, self.outside_temp, self.r_thick_one, self.r_thick_six, self.l_thick_one, self.l_thick_six, self.right_avg, self.left_avg, self.machine_average)
        c.execute("INSERT INTO results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", results)
"""