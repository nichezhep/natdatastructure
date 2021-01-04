from flask import Flask, render_template, redirect, url_for
from algo_code.simple_stack import StackSpitter
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('front.html')


@app.route('/simple_stack')
def simple_stack():

    if StackSpitter.has_stack:

        return str(StackSpitter.active_stack.reveal())

    else:

        return "There is currently no stack"



@app.route('/start_simple_stack')
def simple_stack_url():

    stack = StackSpitter.make_stack(elems=5)

    return redirect(url_for('simple_stack'))


if __name__ == '__main__':
    app.run()
