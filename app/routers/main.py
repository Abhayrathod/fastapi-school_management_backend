from fastapi import FastAPI, Response,status,HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from random import randrange
from sqlalchemy.orm import Session
import time


def auth():
    while True:
        try:
            conn= psycopg2.connect(host='localhost', database='my_local_postgres', port='5433',user='postgres', 
                    password='Abhay66231456',cursor_factory=RealDictCursor)
            cursor = conn.cursor()
            print("Database connection is successful")
            break
        except Exception as error:
                print("Connection to database failed")
                print("Error:",error)
                time.sleep(2)
    return cursor,conn