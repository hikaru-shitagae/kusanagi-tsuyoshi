from flask import Flask, request, render_template
import sqlite3
import random
import json

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route('/index.html')
def index():
    con = sqlite3.connect('sake_database.db')
    cur = con.cursor()

    alco_array = []

    for row in cur.execute("select * from liquor;"):
        alco_array.append([row[0],row[1]])

    con.close()

    return render_template('index.html', data=alco_array)

@app.route('/alcohol.html')
def alcohol():
    return render_template('alcohol.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/answershop', methods=['POST'])
def answershop():
    con = sqlite3.connect('sake_database.db')
    cur = con.cursor()

    address = request.form['address']
    price = request.form['price']
    capacity = request.form['capacity']
    mood = request.form['mood']
    s = '<!DOCTYPE html>\n'
    s += '<html><head><meta charset=UTF-8">\n'
    s += '<link rel="stylesheet" href="static/style_alcohol.css">\n'
    s += '<script scr="static/osake.js"></script></head>\n'
    s += '<body><h2>以下のような居酒屋がおすすめです。</h2>\n'
    i = 0
    for row in cur.execute("select * from shop where address like '%{}%' and price like '%{}%' and capacity like '%{}%' and mood like '%{}&';".format(address, price, capacity, mood)):
        s += '<section class="sake">'
        s += '<div class="btn-container">\n'
        s += '<p>{}</p>\n'.format(row[0])
        s += '<button class="button">詳細を見る</button></div>\n'
        s += '<div class="mask hidden"></div>'
        s += '<section class="modal hidden">\n'
        s += '<ul>\n'
        s += '<li>ベース：{}</li>\n'.format(row[1])
        s += '<li>度数：{}%</li>\n'.format(row[2])
        s += '<li>味：{}</li>\n'.format(row[3])
        s += '<li>割り材：{}</li>\n'.format(row[4])
        s += '<li>こんな人におすすめ：{}</li>\n'.format(row[5])
        s += '<li>レビュー：{}</li>\n'.format(row[6])
        s += '</ul></section>\n'
        s += '<a href="https://www.google.co.jp/maps/place/{}">お店の場所はこちら</a><br>'.format(address)
        s += '</section>\n'
    s += '<p>検索結果：{}件</p>\n'.format(i)
    s += '<a href="index.html">トップに戻る</a>\n'
    s += '</body></html>'
    con.close()
    return s

@app.route('/answeralco', methods=['POST'])
def answeralco():
    con = sqlite3.connect('sake_database.db')
    cur = con.cursor()

    category = request.form['category']
    persent = request.form['persent']
    taste = request.form['taste']

    s = '<!DOCTYPE html>\n'
    s += '<html><head><meta charset="utf-8">\n'
    s += '<link rel="stylesheet" href="static/style_alcohol.css">\n'
    s += '<script src="static/osake.js"></script></head>\n'
    s += '<body><h2>以下のようなお酒がおすすめです。</h2>\n'
    i = 0
    for row in cur.execute("select * from liquor where base like '%{}%' and persent like '%{}%' and taste like '%{}%';".format(category, persent, taste)):
        s += '<section class="sake">'
        s += '<div class="btn-container">\n'
        s += '<p>{}</p>\n'.format(row[0])
        s += '<button class="button">詳細を見る</button></div>\n'
        s += '<div class="mask hidden"></div>'
        s += '<section class="modal hidden">\n'
        s += '<ul>\n'
        s += '<li>ベース：{}</li>\n'.format(row[1])
        s += '<li>度数：{}%</li>\n'.format(row[2])
        s += '<li>味：{}</li>\n'.format(row[3])
        s += '<li>割り材：{}</li>\n'.format(row[4])
        s += '<li>こんな人におすすめ：{}</li>\n'.format(row[5])
        s += '<li>レビュー：{}</li>\n'.format(row[6])
        s += '</ul></section><br>\n'
        s += '<center><a href="https://www.amazon.co.jp/s?k={}">購入はこちらから</a></center><br>'.format(row[0])
        s += '</section>\n'
    s += '<p>検索結果：{}件</p>\n'.format(i)
    s += '<a href="index.html">トップに戻る</a>\n'
    s +=  '</body></html>'
    con.close()
    return s


if __name__ == '__main__':
    app.run(port=5000, debug=True)