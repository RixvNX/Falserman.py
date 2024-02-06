def isInt(number:int) -> bool:
    if type(eval(str(number))) == int:
        return True
    else:
        return False

def isStr(string:str) -> bool:
    if type(eval(str(string))) == str:
        return True
    else:
        return False

def isBool(boolean:bool) -> bool:
    if type(eval(str(boolean))) == bool:
        return True
    else:
        return False

