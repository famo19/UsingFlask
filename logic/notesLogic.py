from core.pyba_logic import PybaLogic


class VideoLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertVideo(self, title, content):
        database = self.databaseObj
        sql = (
            "INSERT INTO `prueba`.`notes` "
            + f"(`id`,`title`,`content`) "
            + f"VALUES(0, '{title}', {content});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllNotes(self):
        database = self.databaseObj
        sql = f"SELECT * FROM prueba.notes;"
        result = database.executeQuery(sql)
        return result

    def getVideoById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM prueba.notes where id={id};"
        result = database.executeQuery(sql)
        return result

    def updateVideo(self, id, video):#TODO CAMBIAR PARAMETROS DE LAS CONSULTAS SQL POR LOS CORRECTOS EN ESTE PROYECTO
        database = self.databaseObj
        sql = (
            "UPDATE `videoappdb`.`video` "
            + f"SET `name` = '{video['name']}', `views` = {video['views']}, `likes` = {video['likes']} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteVideo(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `videoappdb`.`video` WHERE id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows
