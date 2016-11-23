# _*_ coding: utf-8 _*_

from flask import Flask, render_template
from flask_bootstrap import *

dou = Flask(__name__)
bootstrap = Bootstrap(dou)


@dou.route('/')
def hello_world():
    return render_template("index.html")


@dou.route('/graph')
def graph_test():
    return render_template("graph.html")


@dou.route('/graph1')
def graph_test1():
    return render_template("graph01.html")


if __name__ == '__main__':
    dou.run(debug=True)
