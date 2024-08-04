import psycopg2

class Database:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname = self.dbname,
                user = self.user,
                password = self.password,
                host = self.host
            )
        except Exception as e:
            print(f'Error connecting to database: {e}')

    def close(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            if query.strip().upper().startswith('SELECT'):
                return cursor.fetchall()
            elif query.strip().upper().startswith('INSERT') or query.strip().upper().startswith('UPDATE') or query.strip().upper().startswith('DELETE'):
                self.conn.commit()
                return cursor.fetchone()
            else:
                self.conn.commit()
                return None






















'''
CREATE TABLE marketplace (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100)
);

CREATE TABLE good (
    id SERIAL PRIMARY KEY,
    marketplace_id INT,
    name VARCHAR(100),
    price NUMERIC(5,2),
    brand VARCHAR(100),
    rating NUMERIC(3,2),
    quantity INT,
    FOREIGN KEY (marketplace_id) REFERENCES marketplace(id)
)
'''

