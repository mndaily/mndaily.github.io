import csv
from flask import Flask
from flask import abort
from flask import render_template

app = Flask(__name__)

def get_csv():
    csv_path = './static/newSalaries.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

def dept_csv():
    csv_path = './static/departments.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route("/departments")
def depts():
    template = 'departments.html'
    object_list = dept_csv()
    return render_template(template, object_list=object_list)    

# @app.route('/<DEPT>/')
# def detail(DEPT):
#     template = 'dept.html'
#     object_list = get_csv()
#     for row in object_list:
#         if row['DEPT'] == DEPT:
#             return render_template(template, object=row)
#     # return render_template(template)

@app.route('/<FORMATNAME>/')
def prof(FORMATNAME):
    template = 'prof.html'
    object_list = get_csv()
    for row in object_list:
        if row['FORMATNAME'] == FORMATNAME:
            return render_template(template, object=row)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, threaded=True)
