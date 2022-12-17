from rq import Queue
from rq.job import Job
from redis import Redis

class rqclient:
    def __init__(self) -> None:        
        self.redis = Redis()
        self.filler = Queue(connection=Redis())
    
    def checktaskresult(self, jobid:str):
        return Job.fetch(jobid, connection=self.redis)