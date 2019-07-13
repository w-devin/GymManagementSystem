from flask import render_template, redirect, url_for
from . import person
from .forms import ModifyForm
from .. import db
from ..models import User, load_users, load_user_by_phone
from ..auth.forms import RegistrationForm

import sys


@person.route('list')
def person_list():
    persons = load_users()
    return render_template('person/list.html', persons=persons)


@person.route('<phone>', methods=['GET', 'POST'])
def get_person(phone):
    form = ModifyForm()
    person = load_user_by_phone(phone)

    if person is None:
        return render_template('404.html'), 404

    if form.validate_on_submit():
        person.name = form.name.data
        person.age = form.age.data
        person.gender = form.gender.data
        person.identify = form.identify.data
        person.reserved = form.reserved.data
        person.password = form.password.data
        db.session.commit()
        return redirect('list')
    else:
        form.phone.data = person.phone
        form.name.data = person.name
        form.age.data = person.age
        form.gender.data = person.gender
        form.identify.data = person.identify
    return render_template('person/person.html', form=form)

@person.route('del/<phone>', methods=['GET', 'POST'])
def del_person(phone):
    person = load_user_by_phone(phone)

    if person is None:
        return render_template('404.html'), 404

    db.session.delete(person)
    db.session.commit()

    return redirect('../list')

@person.route('add', methods=['GET', 'POST'])
def add_person():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(phone=form.phone.data,
                    name=form.name.data,
                    password=form.password.data,
                    age=form.age.data,
                    gender=form.gender.data,
                    identify=form.identify.data,
                    reserved=form.identify.data
                    )
        db.session.add(user)
        db.session.commit()
        return redirect('list')
    return render_template('auth/register.html', form=form)


