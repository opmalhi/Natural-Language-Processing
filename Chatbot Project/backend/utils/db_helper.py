from mysql.connector import pooling
from .config import get_db_config

class Database:
    def __init__(self):
        self.config = get_db_config()
        self.pool = pooling.MySQLConnectionPool(
            pool_name="my_pool",
            pool_size=5,
            **self.config
        )

    def get_connection(self):
        return self.pool.get_connection()

# Initialize database connection pool
db = Database()