from flask_frozen import Freezer
from app import app, get_csv
freezer = Freezer(app)
app.config['FREEZER_RELATIVE_URLS'] = True


@freezer.register_generator
def prof():
    for row in get_csv():
        yield {'FORMATNAME': row['FORMATNAME']}

if __name__ == '__main__':
    freezer.freeze()