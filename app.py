from flask import Flask, render_template, redirect, url_for
from algo_code.simple_stack import StackSpitter
from algo_code.simple_queue import QueueSpitter
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



@app.route('/simple_stack/create')
def simple_stack_url():

    stack = StackSpitter.make_stack(elems=5)

    return redirect(url_for('simple_stack'))


@app.route('/simple_stack/pop')
def simple_stack_pop():

    item = StackSpitter.active_stack.pop()

    return render_template('front.html', item=item)


@app.route('/simple_stack/length')
def simple_stack_length():

    length = str(len(StackSpitter.active_stack))

    return render_template('front.html', length=length)


@app.route('/simple_queue')
def simple_queue():

    front = QueueSpitter.active_queue.front

    rear = QueueSpitter.active_queue.rear

    queue = []
    for i in QueueSpitter.active_queue.array:
        queue.append(i)

    return 'Current queue is ' + str(queue) + \
           ', Current front number is ' + str(QueueSpitter.active_queue.array[front])\
           + ', Current rear index is ' + str(QueueSpitter.active_queue.rear-1)\
           + ', Current rear element is ' + str(QueueSpitter.active_queue.array[rear-1])


@app.route('/simple_queue/create')
def simple_queue_create():

    queue = QueueSpitter.make_queue()

    return redirect(url_for('simple_queue'))


@app.route('/simple_queue/serve')
def simple_queue_serve():

    item = QueueSpitter.active_queue.serve()

    return str(item)


@app.route('/simple_queue/append/<item>')
def simple_queue_append(item):

    QueueSpitter.active_queue.append(int(item))

    return redirect(url_for('simple_queue'))


@app.route('/simple_queue/rear')
def simple_queue_rear():

    rear = str(QueueSpitter.active_queue.rear)

    return render_template('front.html', rear=rear)

if __name__ == '__main__':
    app.run()
