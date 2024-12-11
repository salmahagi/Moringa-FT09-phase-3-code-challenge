from .connection import get_db_connection

def create_tables():
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Create authors table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            ''')
            
            # Create magazines table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS magazines (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL
                )
            ''')
            
            # Create articles table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    author_id INTEGER NOT NULL,
                    magazine_id INTEGER NOT NULL,
                    FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE,
                    FOREIGN KEY (magazine_id) REFERENCES magazines (id) ON DELETE CASCADE
                )
            ''')

            # Commit changes
            conn.commit()
            print("Tables created successfully!")
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
