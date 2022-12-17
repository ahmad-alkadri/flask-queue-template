#!.locenv/bin/python
from rq import Connection, Worker

with Connection():
    w = Worker(['default'])
    w.work(with_scheduler=True)