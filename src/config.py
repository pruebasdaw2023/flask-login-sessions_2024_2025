class Config():
    SECRET_KEY='2f4238c5ef74c28e899c3d7438059b33d96c173ef4a7f6ddc45432c5625aab29'

class DevelopmentConfig(Config):

    DEBUG=True
    MYSQL_HOST='192.168.0.177'
    MYSQL_USER='luis'
    MYSQL_PASSWORD='luis'
    MYSQL_DB='flask_login_2024_2025'

class ProductionConfig(Config):

    DEBUG=False
    MYSQL_HOST='192.168.0.177'
    MYSQL_USER='luis'
    MYSQL_PASSWORD='luis'
    MYSQL_DB='flask_login_2024_2025'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}