from rq import Queue
from redis import Redis

# connection to Redis
redis_conn = Redis()

# Create a queue
q = Queue(connection=redis_conn)