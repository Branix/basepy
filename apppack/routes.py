from apppack import app

@app.route('/')
@app.route('/index')
def index():
    return "App name: {name} Environment: {env}. <br /> Esta forma permite reutilizar a variável, como env que é {env}".format(name=app.name, env=app.env)
