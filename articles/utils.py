from mongoengine import connect

def connect_to_mongodb():
    connect(db='articles_db', host='mongodb://saplings:_Saplings2025@192.168.1.142:27017/')
