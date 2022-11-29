from celery_stuff.tasks import serve_a_beer, serve_a_coffee, sync_task # Importing the task

def start_serve_a_beer():
    """ Adds serve_a_beer task to the queue with apply_async method.
    the method doesn't wait the task execution be finished.
    """
    serve_a_beer.apply_async(('weiss', '500ml')) # Just add's to a queue, to be executed when celery reads the queue
    print('This will be executed before the serve_a_beer task be finished')

def start_serve_a_coffee():
    """ Starts the execution of a celery task with the delay method.
    the delay method doesn't wait the task execution be finished.
    """
    serve_a_coffee.apply_async(('express', 'small'))
    print('This will be executed before the serve_a_beer task be finished')

def start_serve_a_wine():
    sync_task.apply_async()
    print('This will be executed before the sync_task task be finished')

start_serve_a_beer()
start_serve_a_coffee()
start_serve_a_wine()
