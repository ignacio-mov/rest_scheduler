import requests as requests
from apscheduler.job import Job
from flask import request, jsonify

import scheduler
from scheduler import app


def callback(url, param):
    requests.get(url, params=param)


def job_to_callback(job: Job):
    if job is None:
        return dict()

    callback_data = job.args

    return {'name': job.name,
            'function': callback_data,
            'trigger': {'type': str(job.trigger)},
            'next': job.next_run_time
            }


@app.route('/job', methods=['POST'])
def schedule():
    data = request.json
    name = data['name']
    trigger = data['trigger']
    func = data['function']
    job = scheduler.scheduler.add_job(name, func=callback, args=[func['url'], func['args']],
                                      trigger=trigger['type'], **trigger['args'])
    return job_to_callback(job)


@app.route('/job/<job_id>', methods=['DELETE'])
def delete(job_id):
    scheduler.scheduler.remove_job(job_id)
    return {'id': job_id}


@app.route('/job', methods=['DELETE'])
def delete_all():
    scheduler.scheduler.remove_all_job()
    return {}


@app.route('/job', methods=['GET'])
def get_all():
    datos = [job_to_callback(j) for j in scheduler.scheduler.get_jobs()]
    return jsonify(datos)


@app.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    return job_to_callback(scheduler.scheduler.get_job(job_id))
