import login, commandlined, shelve
import os

print(os.getcwd())

# reset thread database
threaddb = shelve.open("../data/system/thread")
threaddb["list"] = {}
threaddb["total"] = 0
threaddb.sync()
threaddb.close()

print("Welcome to use FakeOS alpha 0.0.1")
print("When you want to exit, please type 'exit' to exit, not click 'X' on the window.\n")

# yêu cầu login
username = None
while username is None:
    username = login.app([])

# sau khi login thành công
commandlined.commandline(username)

# reset thread khi thoát
threaddb = shelve.open("../data/system/thread")
threaddb["list"] = {}
threaddb["total"] = 0
threaddb.sync()
threaddb.close()


class info:
    osVersion = "0.0.1"
    osBuild = "1"
    osAuthor = "Error063"
    osCompany = "Example Company"
    createTime = 1627625284