# flask-env-example

Example repo demonstrating local public, local private, and remote environment variables.

## Local public vs local private

Flask recommends using 2 separate env files (`.flaskenv`, which should be [checked in](https://github.com/drewwyatt/flask-env-example/blob/master/.flaskenv), and `.env`, which should be [`.gitignored`](https://github.com/drewwyatt/flask-env-example/blob/master/.gitignore#L2))

**From the docs:**

> Variables set on the command line are used over those set in .env, which are used over those set in .flaskenv. .flaskenv should be used for public variables, such as FLASK_APP, while .env should not be committed to your repository so that it can set private variables.
>
> \- [Environment Variables, Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/cli/#environment-variables-from-dotenv)

In this example, I set the following (flask specific, and harmless) variables in `.flaskenv` to avoid having to set them in the command line every time. These are considered _public_ because they are checked in.

```dotenv
FLASK_APP=endpoints.py
FLASK_ENV=development
```

Locally, I also have a `.env` file, that is not seen in this repo, because it is [`.gitignored`](https://github.com/drewwyatt/flask-env-example/blob/master/.gitignore#L2). It looks like this:

```dotenv
MY_SECRET_VARIABLE="This is a secret variable set on my local machine"
SMTP_PASSWORD="p@ssw0rd!"
```

**NOTE: The first time you run `flask run` after creating these files, flask will prompt you to `pip install python-dotenv`. This is a necessary step before you can access them.**

## Accessing environment variables

Inside this flask app ([`endpoints.py`](https://github.com/drewwyatt/flask-env-example/blob/master/endpoints.py#L9-L15)) I have defined a single route (`/`). There are 2 areas to look at here (un-annotated code can be seen without omissions [here](https://github.com/drewwyatt/flask-env-example/blob/master/endpoints.py)):

```python
import os # import the os module

# ...

@app.route("/", methods={"GET"})
def index():
    return json_response({"message": "these are examples of some environment variables. (normally you would not print these!)",
                          "variables": {"FLASK_ENV": os.getenv("FLASK_ENV"), # use os.getenv() to access the values
                                        "MY_SECRET_VARIABLE": os.getenv("MY_SECRET_VARIABLE"), # use os.getenv() to access the values
                                        "SMTP_PASSWORD": os.getenv("SMTP_PASSWORD") # use os.getenv() to access the values
                                        }})
```

Here, we are importing and using [`os.getenv`](https://docs.python.org/3/library/os.html#os.getenv) to access the environment variables set in `.flaskenv` and `.env`.

If I run this locally, this is what I see when visiting [`http://localhost:5000/`](http://localhost:5000/):

![Local Output](https://i.imgur.com/KrVjveC.png)

The especially interesting thing to notice here is that the values defined in `.env` (`MY_SECRET_VARIABLE` and `SMTP_PASSWORD`) are present without having to expose those values to *everyone* that has access to the source code. (note that, in most circumstances, we would probably not expose these values via an unauthentiated `GET` response)

## Remote environments

Okay, so how do we access these when we deploy? This example uses [Heroku](), but there are many SaaS alternatives that offer something similar. 

If you visit the settings pane of your project, you will find [Config Vars](https://devcenter.heroku.com/articles/config-vars). Here you can re-define all of your local variables in Heroku, using the same key/value format. Here's what my configuration for this example looks like:

![Heroku config vars](https://i.imgur.com/QgJEjTb.png)

These will be set by Heroku the same way you would set these variables on your machine via CLI:

```bash
$ export MY_SECRET_VARIABLE="something like this"
```

Another cool thing, is that because of the priority flask applies to environments (CLI > .env > .flaskenv), you can use the Heroku config to override `.flaskenv` variables (the ones that are checked in). In this example, I took advantage of this by setting `FLASK_ENV` to `"production"` (disabling DEBUG mode).

You can see this working in the screenshot below, and see for youself [by visiting the deployed site](https://flask-env-example.herokuapp.com/).

![Heroku output](https://i.imgur.com/0SzCds8.png)
`

## References

1. [Environment Variables, Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/cli/#environment-variables-from-dotenv)
2. [OS Library, Python Documentation](https://docs.python.org/3/library/os.html)
3. [Config Vars, Heroku Documentation](https://devcenter.heroku.com/articles/config-vars)
