import os
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_history_note(conn, historynote):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO testsite_historynote(note_type, name_in_sources, titles, life_dates, biography, family_relationship, others, sources, literature,author_id,article_name, author_before)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, historynote)
    conn.commit()
    return cur.lastrowid



ar = []
i=10
path_to_db = os.path.join(os.path.dirname(__file__),'db.sqlite3')
database = path_to_db

conn = create_connection(database)
path = os.path.join(os.path.dirname(__file__),'testsite','src2')
with conn:
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            file = open(path+'/'+filename,'r',encoding='utf-8')
            for line in file:
                eq = line.index('=',0,len(line))
                value_st = line[eq+1:len(line)]
                if value_st is not None:
                    ar.append(value_st)
                else:
                    ar.append('нет')

            #  использрвать для папки src1
            # historynore = ( ar[2], ar[3], ar[4], ar[5], ar[6], ar[7], ar[8], ar[9], 1, ar[0], ar[1])
            historynore = (ar[0], ar[3], ar[4], ar[5], ar[6], ar[7], ar[8], ar[9], ar[10], 1, ar[1], ar[2])
            i+=1
            create_history_note(conn, historynore)
            ar.clear()

print('done')
