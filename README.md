# Task scheduler

#### This task scheduler is designed to check Celery behaviour for async functions. Here, we will be executing both synchronous and asynchronous functions using Celery.  

1. Install Celery, asgiref packages
2. Start Celery worker:
```
celery -A celery_stuff.tasks worker -l debug
```
3. Provide queue names to execute jobs from epecific queues:
```
celery -A celery_stuff.tasks worker -l debug -Q wine,bear,coffee
```
4. Start application to push jobs to the queue:
```
python first_app.py
```
5. You should see a beer, coffee and wine in Celery logs where beer and coffee are defined as synchronous functions while wine is defined as asynchronous!
 
Here asynchronous function will be called as synchronous in Celery.
Celery or other similar task management systems are better to use for cpu intensive tasks.  
