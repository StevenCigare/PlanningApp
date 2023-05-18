from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        new_note = Note(data=note, user_id=current_user.id, date=current_user.chosen_date)
        #current_user.date_chosen_notes.append(new_note)
        print(current_user.chosen_date)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/date', methods=['POST'])
def change_date():
    date = json.loads(request.data)  
    date = date['selectedDate']
    print(date)
    date = datetime.strptime(date, '%m/%d/%Y').date()
    current_user.chosen_date = date
    #current_user.chosen_date_notes = current_user.notes.filer_by(date=date).all()
    print(current_user.chosen_date)
    db.session.commit()

    return jsonify({})

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})

@views.route('/mark-done', methods=['POST'])
def mark_as_done():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            note.completed = True
            db.session.commit()
    
    return jsonify({})