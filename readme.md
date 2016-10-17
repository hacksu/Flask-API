# Flask

Flask is a micro-framework for Python which allows you to progromatically control what gets returned from an http server.
It's meant to be easy to use and in my opinion it is.

## Installation

Install python from https://www.python.org/ (the first thing that comes up when you Google for Python). The version shouldn't matter.
Check that you have it installed by running `python -V`
Install `flask` by typing `pip install flask`

Then make a new directory and open it in your editor of choice.

## Steps

### Hello Internet

Make a app.py file and put the following basically copied from Flask's main page in it

        from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def hello():
            return "Hello Internet!"

        if __name__ == "__main__":
            app.run(debug=True)

Lets go over this line by line and see what's happening

`from flask import Flask` import the `Flask` thing from the `flask` package
`app = Flask(__name__)` make a new instance of Flask and pass it the name of the current scope (not quite clear on what that is either)
`@app.route("/")` registers a route listening for anyone going to `/` on the webserver

        def hello():
            return "Hello Internet!"

is the function that will handle the request, here it just returns "Hello Internet!" 

Finally 

        if __name__ == "__main__":
            app.run(debug=True)

starts the webserver. Note this configuration is not something you want to use in production. Not only is it slow, but because we've set the debug flag
it's insecure.

To run it type `python app.py`

You should see

        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        * Restarting with stat
        * Debugger is active!
        * Debugger pin code: 270-413-265

or similar.


Go to http://127.0.0.1:5000/ to see our site.

### Change the message

Change 

        def hello():
            return "Hello Internet!"

to return something else. Save the file and reload in the browser. The message in your browser should say whatever you put there.

### Add another route.

How do you think you'd add another route?

It turns out to be about what you'd guess

        @app.route("/bye/")
        def bye():
            return "Bye folks"

Go to `http://localhost:5000/bye/` to see the message

Note that there is a difference between

@app.route("/bye/") and @app.route("/bye") the former will redirect people to the version with the trailing slash if they go to just /bye where as
the later will just match for /bye. It doesn't matter which you use, but you should know there is a difference.

### JSON

Up to now we've just returned a HTML, To be honest you may not have realized it was HTML it certainly wasn't properly formatted HTML,
but to your browser and critically anything else making http requests it was HTML. 

JSON is a bit different, it stands for JavaScript Object Notation and is a text based way of representing a JavaScript class or really any class. It servers a similar purpose to
XML, but to me is much easier to read and write. 


Anyway, enough explenation, that all sounds good, how do we actually send it.

Again flask makes it easy. We just need to make two changes. First add a `from flask import Jsonify` to the top of the file then inside a route replace the return with
`jsonify({"message": "Hello Internet!"})`

### Practical Problem

Everytime I talked about doing a survey, sami would say I really should make a world cloud of topic suggestions. My Googling skills weren't up to snuff though
and I couldn't find a site to do it. We can make one though. Or at least the backend of one. We'll need a couple of routes.

In partical we need a way of voting for a particlar topic and then a way of listing the topics people have voted on. Listing the topics is pretty easy
Lets just add a route like

        @app.route("/topics/")
        def topics():
            return jsonify({
                "words": {
                    "json": 4,
                    "jokes": 1,
                    "Mobile": 10
                }
            })
