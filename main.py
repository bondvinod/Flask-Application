from flask import Flask, render_template

app = Flask('Vinod')


@app.route('/lord_of_rings')
def lord_of_rings():
    return 'Lord of the rings'


@app.route('/game_of_thrones')
def game_of_thrones():
    return 'Game_of_thrones'


@app.route('/king_of_Parsia')
def king_of_parsia():
    return 'King_of_Parsia'


@app.route('/clash_of_Titans')
def clash_of_titans():
    return 'Clash_of_Titans'


@app.route('/the_Great_Britan_Very_good_Wife')
def the_great_britan_very_good_wife():
    return 'The_Great_Britan_Very_good_Wife'


@app.route('/bumble_Bee')
def bumble_bee():
    return 'Bumble_Bee'


@app.route('/')
def main_page():
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
