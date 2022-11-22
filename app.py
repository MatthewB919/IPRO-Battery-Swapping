from flask import Flask, redirect, url_for, request

app= Flask(__name__) 


@app.route('/', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Release':
            pass # do something
        elif request.form['submit_button'] == 'Emergency Button':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return ("error occured")


if __name__ == "__main__":
    app.run