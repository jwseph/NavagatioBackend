from flask import Flask, render_template
from base.json_processing import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Welcome To Wanderlag!</h1>'


@app.route('/activities/')
def activities_home():
    return "<h1>ACTIVITIES HOME</h1>"


@app.route('/activities/<city>')
def render_activities(city):
    # return render_template('rec_activities.html.jinja2', city_name=city, attraction_list=[])
    response_body = {
        "name": city,
        "data" :"Currently No Data Available"
    }

    return response_body

@app.route('/activities/Seoul')
def demo_render():
    seoul_attractions = parse_data('Seoul')
    # return render_template('rec_activities.html.jinja2', city_name="Seoul", attraction_list=seoul_attractions)
    return seoul_attractions

if __name__ == '__main__':
    app.run()
