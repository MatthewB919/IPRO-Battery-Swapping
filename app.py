from flask import Flask

start app= flask.flask(__index__) indicate html file
/home



        def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Release':
            pass # do something
        elif request.form['submit_button'] == 'Emergency Button':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)