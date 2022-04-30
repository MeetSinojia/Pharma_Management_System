from flask import render_template, redirect, url_for, request, flash, abort
from pharmaton.forms import RegistrationForm, LoginForm, AdminForm, SalesForm, DepartureForm, DiseaseForm
from pharmaton import app, db, bcrypt
from pharmaton.models import Medicine, User, Sales, Departure, Add_disease
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    medn = Medicine.query.all()
    return render_template('Home.html', title='Home Page', medn=medn)


# Admin Login, Registration and Logout

@app.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = AdminForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Admin Register successfully', category='success')
        return redirect(url_for('home'))
    return render_template('admin_register.html', title='Admin Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login successfully', category='success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful please check your email and password', 'danger')
    return render_template('login.html', title='Admin Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('home')


@app.route('/register', methods=['POST', 'GET'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        med = Medicine(medname=form.medname.data, efficiency=form.efficiency.data, sideeffect=form.sideeffect.data,
                       typemed=form.typemed.data, cmpname=form.cmpname.data, disease=form.disease.data,
                       expdate=form.expdate.data, mfgdate=form.mfgdate.data, author=current_user)
        db.session.add(med)
        db.session.commit()
        flash('Medicine Register Successfully', category='success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Medicine Registration', form=form)


# Medicine update and delete

@app.route("/medicine/<int:med_id>")
def medicine(med_id):
    medicine = Medicine.query.get_or_404(med_id)
    return render_template('medicine.html', medicine=medicine, title='Medicine')


@app.route("/medicine/<int:med_id>/update", methods=['GET', 'POST'])
def update_medicine(med_id):
    medicine = Medicine.query.get_or_404(med_id)

    if medicine.author != current_user:
        abort(403)

    form = RegistrationForm()
    if form.validate_on_submit():
        medicine.medname = form.medname.data
        medicine.efficiency = form.efficiency.data
        medicine.sideeffect = form.sideeffect.data
        medicine.typemed = form.typemed.data
        medicine.cmpname = form.cmpname.data
        medicine.disease = form.disease.data
        medicine.expdate = form.expdate.data
        medicine.mfgdate = form.mfgdate.data
        db.session.commit()
        flash('Your medicine has been updated!!', 'success')
        return redirect(url_for('medicine', med_id=medicine.ref_no))
    elif request.method == 'GET':
        form.medname.data = medicine.medname
        form.efficiency.data = medicine.efficiency
        form.sideeffect.data = medicine.sideeffect
        form.typemed.data = medicine.typemed
        form.cmpname.data = medicine.cmpname
        form.disease.data = medicine.disease
        form.expdate.data = medicine.expdate
        form.mfgdate.data = medicine.mfgdate

    return render_template('register.html', form=form, title='Update medicine', legend='Update Medicine')


@app.route("/medicine/<int:med_id>/delete", methods=["POST"])
@login_required
def delete_medicine(med_id):
    medicine = Medicine.query.get_or_404(med_id)

    if medicine.author != current_user:
        abort(403)
    db.session.delete(medicine)
    db.session.commit()
    flash('Your medicine has been deleted!', 'success')
    return redirect(url_for('home'))


# <----------------Sales table------------------>

@app.route('/salse_register', methods=['GET', 'POST'])
def salse_register():
    form = SalesForm()
    if form.validate_on_submit():
        sale = Sales(price=form.price.data, does_available=form.does_available.data, dose_sale=form.dose_sale.data,
                     medname=form.medname.data, profit=form.profit.data)
        db.session.add(sale)
        db.session.commit()
        flash('Registration successfully', category='success')
        return redirect(url_for('salse_register'))

    med = Sales.query.all()

    return render_template('salse_register.html', title='Salse Registration', form=form, legend='Sales Registration',
                           med=med)


# <--------------------Departure table---------------->


@app.route('/departure', methods=['GET', 'POST'])
def departure():
    form = DepartureForm()
    if form.validate_on_submit():
        dep = Departure(ref_no=form.ref_no.data, city=form.city.data, medname=form.medname.data, depid=form.depid.data,
                        vehicleno=form.vehicleno.data)
        db.session.add(dep)
        db.session.commit()
        flash('Departure Data added successfully !!', category='success')
        return redirect(url_for('departure'))

    dep = Departure.query.all()

    return render_template('departure.html', form=form, title='Departure Table', legend='Departure Data Register',
                           dep=dep)


# <-----------------Disease-------------------->

@app.route('/disease')
def disease():
    disease = Add_disease.query.all()

    return render_template('disease.html', title='Disease', disease=disease)


@app.route('/add_disease', methods=['GET', 'POST'])
def add_disease():
    form = DiseaseForm()
    if form.validate_on_submit():
        dis = Add_disease(disease=form.disease.data)
        db.session.add(dis)
        db.session.commit()
        flash('Disease added successfully !!!', category='success')
        return redirect(url_for('disease'))
    return render_template('add_disease.html', title='Add Disease', form=form)


@app.route('/fever')
def Fever():
    emp = Medicine.query.filter_by(disease='Fever')

    return render_template('fever.html', title='Fever', emp=emp)


@app.route('/cuf')
def Cuf():
    emp = Medicine.query.filter_by(disease='Cuf')

    return render_template('fever.html', title='Cuf', emp=emp)

@app.route('/flue')
def Flue():
    emp = Medicine.query.filter_by(disease='Flue')

    return render_template('fever.html', title='Flue', emp=emp)

@app.route('/vomite')
def Vomite():
    emp = Medicine.query.filter_by(disease='Vomite')

    return render_template('fever.html', title='Vomite', emp=emp)

@app.route('/xyz')
def Xyz():
    emp = Medicine.query.filter_by(disease='Xyz')

    return render_template('fever.html', title='Xyz', emp=emp)