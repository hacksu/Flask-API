# Flask

Flask is a micro-framework for Python which allows you to progromatically control what gets returned from an http server.
It's meant to be easy to use and in my opinion it is.

## Installation

Install python from https://www.python.org/ (the first thing that comes up when you Google for Python). The version shouldn't matter.
Check that you have it installed by running `python -V`
Install `flask` by typing `pip install flask`

Then make a new directory and open it in your editor of choice.

## Steps

## Hello Internet

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

## Change the message

Change 

        def hello():
            return "Hello Internet!"

to return something else. Save the file and reload in the browser. The message in your browser should say whatever you put there.

