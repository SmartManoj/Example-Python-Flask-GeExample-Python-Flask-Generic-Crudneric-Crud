from flask import render_template, request, redirect
from app import app, db
from app.models import Entry,cols

pkey='customer_id'
def row_to_dict(row,skip=[]):
    d = {}
    for column in row.__table__.columns:
        name = column.name
        if name in skip:continue
        d[name] = str(getattr(row, name))
    return d
def query_as_dict(entries):
    table=[]
    for row in entries:
        table.append(row_to_dict(row))
    return table


@app.route('/')
@app.route('/index')
def index():
    entries = query_as_dict(Entry.query.all())
    return render_template('index.html', entries=entries,cols=cols)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = dict(request.form)
        del form[pkey]
        entry = Entry(**form)
        db.session.add(entry)
        db.session.commit()
        return redirect('/')

@app.route('/update/<int:cid>')
def updateRoute(cid):
    entry = Entry.query.get(cid)
    if entry:
        return render_template('update.html', entry=row_to_dict(entry),cols=cols)
    return ""

@app.route('/update', methods=['POST'])
def update():
    form = request.form
    entry = Entry.query.get(int(form.get(pkey)))
    if entry:
        for column in entry.__table__.columns:
            name = column.name
            setattr(entry, name, form[name] )
        db.session.commit()
    return redirect('/')




@app.route('/delete/<int:cid>')
def delete(cid):
    entry = Entry.query.get(cid)
    if entry:
        db.session.delete(entry)
        db.session.commit()
    return 'done'



