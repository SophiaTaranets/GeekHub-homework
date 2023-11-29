import sqlite3


class Category:
    def __init__(self, title=None):
        self.id = id
        self.title = title

    def __get_id(self):
        return self.id

    @staticmethod
    def create_category(title):
        db = sqlite3.connect('library.db')
        cursor = db.cursor()

        cursor.execute('SELECT category_id FROM category WHERE title = ?', (title,))
        existing_category = cursor.fetchone()

        if existing_category:
            return "Category already exists."
        else:
            cursor.execute('INSERT INTO category (title) VALUES (?)', (title,))
            db.commit()
            db.close()
            return True

    @staticmethod
    def get_all_categories():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute(f'SELECT title FROM category')
            categories = cursor.fetchall()
        except sqlite3.IntegrityError:
            conn.close()
            return False
        except sqlite3.Error as e:
            conn.close()
            return str(e)
        finally:
            conn.close()
        return categories
