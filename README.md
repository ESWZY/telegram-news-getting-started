# telegram-news-getting-started

A news pushing demo using [Telegram-news](https://github.com/ESWZY/telegram-news).

## Running Locally

Make sure you have [Python3](https://www.python.org/) and the [Heroku CLI](https://cli.heroku.com/) installed.

```sh
$ git clone https://github.com/ESWZY/telegram-news-getting-started # or clone your own fork
$ cd telegram-news-deploy
$ pip install -r requirements.txt
$ python main.py
```

Your app should now be running in the background.

## Deploying to Heroku

```
$ heroku create
$ git push heroku main
$ heroku open
```
or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
