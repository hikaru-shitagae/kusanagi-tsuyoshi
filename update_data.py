import sqlite3

# データベースファイルに接続
database_file = 'sake_database.db'
conn = sqlite3.connect(database_file)
cur = conn.cursor()

# データを挿入するSQL文
update_data_sql = '''
INSERT INTO liquor (name, base, persent, taste, material, recommend, review)
VALUES (?, ?, ?, ?, ?, ?, ?)
'''

# 挿入するデータの例
update_data=[

]



try:
    # データを挿入
    cur.executemany(update_data_sql, update_data)
    conn.commit()
    print("データが正常に挿入されました")
except Exception as e:
    print(f"エラーが発生しました: {e}")
finally:
    # 接続を閉じる
    conn.close()
