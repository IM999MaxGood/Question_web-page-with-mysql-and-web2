import web

db= web.database(dbn="mysql", db="web_page_mysql2", user="im999maxgood_U", pw="123456")

def getItems():
    items = db.select("item", order="id")
    return items

def addItem(title):
    db.insert("item", title=title)

def delItem(id):
    #im999 because of error: tokenize.TokenError: ('unterminated string literal (detected at line 1)', (1, 4))
    #db.delete("item", where="id=$id")
    str = "id="+id
    db.delete("item", where=str)

def getItem(id):
    try:
        #im999 because of error: tokenize.TokenError: ('unterminated string literal (detected at line 1)', (1, 4))
        #item = db.delete("item", where="id=$id")[0]
        str = "id="+id
        item = db.select("item", where=str)[0]
        return item
    except IndexError:
        return None
    
def updateItem(id, title):
    #im999 because of error: tokenize.TokenError: ('unterminated string literal (detected at line 1)', (1, 4))
    #db.update("item", where="id=$id", title=title)
    str = "id="+id
    db.update("item", where=str, title=title)
