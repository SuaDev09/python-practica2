from app import create_app
from app.models import *
from flask import render_template, redirect, url_for, request, session

app = create_app()


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/inicio')
def inicio():
    return render_template("inicio.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/hacer_login', methods=['POST'])
def hacer_login():
    name = request.form['name']
    password = request.form['password']
    listUsers = Users.query.all()
    for user in listUsers:
        if (user.name == name and user.password == password):
            session['usuario'] = name
            return redirect('/inicio')
    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/login')


@app.before_request
def antes_de_peticion():
    ruta = request.path
    if not 'usuario' in session and ruta != '/login' and ruta != '/hacer_login' and ruta != '/logout' and not ruta.startswith('static'):
        return redirect('/login')


@app.route("/series/list", methods=["GET"])
def get_series():
    series = Series.query.all()
    return render_template("viewSeries.html", series=series)


@app.route("/serie/create", methods=["POST", 'GET'])
def create_serie():
    if request.method == 'POST':
        serie = Series(
            id=0,
            name=request.form['name'],
            state=request.form['state'],
            temporadas=request.form['temporadas'],
            capPorTem=request.form['capPorTem']
        )
        db.session.add(serie)
        db.session.commit()
        return redirect('/series/list')
    elif request.method == 'GET':
        return render_template("createSerie.html")
    else:
        return redirect('/series/list')


# @app.route('/series/edit/<int:id>', methods=['GET'])
# def edit_view(id):
#     if request.method == 'GET':
#         serie = Series.query.get(id)
#         return render_template("editSerie.html", serie=serie)
#     else:
#         return redirect('/series/list')


# @app.route('/series/edit/update', methods=['POST'])
# def update_serie():
#     if request.method == 'POST':
#         serie = Series.query.get(request.form['id'])
#         serie.id = request.form['id']
#         serie.name = request.form['name']
#         serie.state = request.form['state']
#         serie.temporada = request.form['temporada']
#         serie.capPorTem = request.form['capPorTem']
#         db.session.commit()
#         return redirect('/series/list')
#     else:
#         return redirect('/series/list')


@app.route('/series/delete/<int:id>')
def delete_book(id):
    serie = Series.query.get(id)
    db.session.delete(serie)
    db.session.commit()
    return redirect('/series/list')

# https://parzibyte.me/blog/2021/03/29/login-sesiones-flask/
