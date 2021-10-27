from flask import Blueprint, request, redirect, url_for, flash, render_template
from ...ext.database import db

bp = Blueprint('autenticacao', __name__, url_prefix='/autenticacao', template_folder='templates')


# @bp.route('/')
# def root():
#     return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
#         sobre = ""


#         jatem = User.query.filter_by(email=email).first()

#         if jatem is not None:
#             flash('Já existe uma conta com esse e-mail. Insira outro e-mail')
#             return redirect(url_for('register'))

#         else:
#             user = User(name, email, pwd, sobre)
#             db.session.add(user) #inserir
#             db.session.commit()  #atualiza
#             flash('Conta criada com sucesso!')
#             return redirect(url_for('login'))

    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        # user = User.query.filter_by(email=email).first()

        # if not user or not user.verify_password(pwd):
        #     flash("Email ou senha inválidos!")
        #     return redirect(url_for('login'))

        # login_user(user)
        flash('Você foi logado com sucesso :)\n')
        return redirect(url_for('root'))

    return render_template('login.html')


def init_app(app):
    app.register_blueprint(bp)