from stories import Story
from flask import Flask, request, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['DEBUG'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

# default page
@app.route('/', methods=['POST', 'GET'])
def home_page():
    return 'Welcome to Madlibs! Visit /questions to fill out the questions'

# form route
@app.route('/questions', methods=['POST', 'GET'])
def questions():
    form_data = {
        'place': '',
        'noun': '',
        'verb': '',
        'adjective': '',
        'plural_noun': ''
        }

    if request.method == 'POST':
        place = request.form['place']
        noun = request.form['noun']
        verb = request.form['verb']
        adjective = request.form['adjective']
        plural_noun = request.form['plural_noun']
        return redirect(url_for(
            'stories',
            place = place, 
            noun = noun,
            verb = verb,
            adjective = adjective,
            plural_noun = plural_noun
        ))
    return render_template(
        'questions.html',
        form_data = form_data
    )

# stories
@app.route('/stories')
def stories():
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    plural_noun = request.args.get('plural_noun')

    story = Story(
        [
            'place',
            'noun',
            'verb', 
            'adjective',
            'plural_noun'
        ],
        f"Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."
    )

    story_text = story.generate({
        'place': place,
        'noun': noun,
        'verb': verb, 
        'adjective': adjective,
        'plural_noun': plural_noun
    })

    return render_template('stories.html', story_text=story_text)



if __name__ == '__main__':
    app.run(debug=True)
    