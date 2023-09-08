#!/usr/bin/env python3
'''
Provide stats about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient


if __name__ == '__main__':
    c = MongoClient('mongodb://localhost:27017').logs.nginx
    print(f'{c.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {c.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {c.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {c.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {c.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {c.count_documents({"method": "DELETE"})}')
    print(f'{c.count_documents({"path": "/status"})} status check')
