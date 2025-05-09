class Protected:
    def __init__(self):
        self._protectedVar = 0

#A private 
class Private:
    def __init__(self):
        self.__privateVar = 125

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj._protectedVar = 47
print(obj._protectedVar)

obj = Private()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
