# -*- coding:utf-8 -*-
class UserSession(object):
    def __init__(self, userID, userName):
        self.userid = userID
        self.username = userName

    def toDict(self):
        return {"userID": self.userid, "userName": self.username}
