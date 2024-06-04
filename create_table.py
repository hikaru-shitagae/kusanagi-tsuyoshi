import sqlite3

# SQLiteデータベースに接続（ファイルが存在しない場合は新規作成される）
database_file = 'sake_database.db'
conn = sqlite3.connect(database_file)
cur = conn.cursor()

# 新しいテーブルを作成するSQL文
create_table_sql = '''
CREATE TABLE IF NOT EXISTS liquor (
    name text,
    base text,
    persent text,
    taste text,
    material text,
    recommend text,
    review text
);
'''

try:
    # SQL文を実行してテーブルを作成
    cur.execute(create_table_sql)
    conn.commit()
    print("テーブルが正常に作成されました")
except Exception as e:
    print(f"エラーが発生しました: {e}")
finally:
    # 接続を閉じる
    conn.close()
