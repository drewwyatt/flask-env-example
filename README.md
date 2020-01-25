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

Locally, I also haave a `.env` file, that is not seen in this repo, because it is [`.gitignored`](https://github.com/drewwyatt/flask-env-example/blob/master/.gitignore#L2). It looks like this:

```dotenv
MY_SECRET_VARIABLE="This is a secret variable set on my local machine"
SMTP_PASSWORD="p@ssw0rd!"
```

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

## References

1. [Environment Variables, Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/cli/#environment-variables-from-dotenv)
2. [OS Library, Python Documentation](https://docs.python.org/3/library/os.html)
