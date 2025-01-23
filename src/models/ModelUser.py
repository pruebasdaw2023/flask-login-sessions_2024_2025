class ModelUser():

    def login(self, db, user):

        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM user WHERE username = %s'

            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()

        except Exception as e:

            raise Exception(e)