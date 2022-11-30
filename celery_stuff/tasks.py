import asyncio
from asgiref.sync import async_to_sync
from time import sleep
from celery import Celery

# Creating a celery instance with redis as message broker.
app = Celery('first_app', broker='redis://localhost:6379')

app.conf.task_routes = {
    'celery_stuff.tasks.serve_a_beer': {'queue': 'beer'},
    'celery_stuff.tasks.serve_a_coffee': {'queue': 'coffee'},
    'celery_stuff.tasks.sync_task': {'queue': 'wine'}
}

@app.task
def serve_a_beer(_type, size):
    """
     This is a celery task. Just a normal function with task decorator.
     Note that we use the decorator from a celery insance.
    """
    print('Serving {} of {} beer!'.format(size, _type))
    sleep(3)

@app.task
def serve_a_coffee(_type, size):
    """
     This is a celery task. Just a normal function with task decorator.
     Note that we use the decorator from a celery insance.
    """
    print('Serving a {} {} coffee!'.format(size, _type))
    sleep(1)

# @app.task
async def serve_wine_asynchrously():
    await asyncio.sleep(3)
    print("Serving a wine asynchrously....")
    return 'wine'

# @app.task(name="sync_task")
@app.task
def sync_task():
    async_to_sync(serve_wine_asynchrously)()