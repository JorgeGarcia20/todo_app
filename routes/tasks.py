from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.task import Task
from utils.db import db

tasks = Blueprint('tasks', __name__)


@tasks.route('/')
def index():
    active_tasks = Task.query.filter_by(status=1)
    deactive_tasks = Task.query.filter_by(status=0)
    return render_template('index.html', active_tasks=active_tasks, dtask=deactive_tasks)


@tasks.route('/new', methods=['POST'])
def new():
    title = request.form['title']
    description = request.form['description']

    new_task = Task(title, description)

    db.session.add(new_task)
    db.session.commit()

    flash('Tarea agregada satisfactoriamente')
    return redirect(url_for('tasks.index'))


@tasks.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):

    task = Task.query.get(id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']

        db.session.commit()

        flash('Tarea editada satisfactoriamente')

        return redirect(url_for('tasks.index'))

    return render_template('update.html', task=task)


@tasks.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    flash('Tarea eliminada satisfactoriamente')

    return redirect(url_for('tasks.index'))


@tasks.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get(id)
    task.status = 0
    db.session.commit()

    return redirect(url_for('tasks.index'))


@tasks.route('/active/<int:id>')
def active(id):
    task = Task.query.get(id)
    task.status = 1
    db.session.commit()

    return redirect(url_for('tasks.index'))
