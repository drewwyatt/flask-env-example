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

## References

1. [Environment Variables, Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/cli/#environment-variables-from-dotenv)
