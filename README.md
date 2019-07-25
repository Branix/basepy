# Documentação da app exemplo

## Execution Nux

Se quiser apenas executar a aplicação direta do seu repositório, faça o seguinte:

```sh
export APP_FOLDER=awesome
export GIT_URL="https://github.com/Branix/basepy"
git clone $GIT_URL $APP_FOLDER && cd $APP_FOLDER

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
#  * Serving Flask app "microblog"
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

- Acesse http://127.0.0.1:5000/

## Tutorial

```python
# app/__init__.py: Flask application instance

from flask import Flask

app = Flask(__name__)

from app import routes

```

```python
# app/routes.py: Home page route

from app import app

@app.route('/')
@app.route('/index')
def index():
    return app.__name__
```

```sh
# (venv) $
# export FLASK_APP=microblog.py
```
