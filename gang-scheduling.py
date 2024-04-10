class TaskNode:
    def __init__(self, id, bursts):
        self.id = id
        self.bursts = bursts
        self.next = None

class JobNode:
    def __init__(self, job_id, arrival_time, job_type, processing_unit, priority, num_tasks):
        self.id = job_id
        self.arrival_time = arrival_time
        self.type = job_type
        self.processing_unit = processing_unit
        self.priority = priority
        self.num_tasks = num_tasks
        self.tasks_head = None
        self.next_job = None
    
    def add_task(self, id, bursts):
        if not self.tasks_head:
            self.tasks_head = TaskNode(id, bursts)
        else:
            current = self.tasks_head
            while current.next:
                current = current.next
            current.next = TaskNode(id, bursts)

# working with json
data = {
  "max-cpu-per-job": 1000,
  "jobs": [
    {
      "job": {
        "id": 10,
        "arrival-time": 0,
        "type": "interactive",
        "processing-unit": "CPU",
        "priority": 1,
        "num-tasks": 13,
        "tasks": [
          {
            "task": {
              "id": 1,
              "bursts": [
                5, 33, 
              ]
            }
          },
          {
            "task": {
              "id": 2,
              "bursts": [
                9, 9, 
              ]
            }
          },
          {
            "task": {
              "id": 3,
              "bursts": [
                4, 25, 
              ]
            }
          },
          {
            "task": {
              "id": 4,
              "bursts": [
                1, 65, 
              ]
            }
          },
         
        ]
      }
    },
   
  ]
}


jobs_head = None

# creatingthe linked list with jobs and their tasks
for job_data in data["jobs"]:
    job_info = job_data["job"]
    new_job = JobNode(job_info["id"], job_info["arrival-time"], job_info["type"], job_info["processing-unit"], job_info["priority"], job_info["num-tasks"])
    
    # Adding tasks to the job
    for task_data in job_info["tasks"]:
        task_info = task_data["task"]
        new_job.add_task(task_info["id"], task_info["bursts"])
    
    # job to jobs
    if not jobs_head:
        jobs_head = new_job
    else:
        current_job = jobs_head
        while current_job.next_job:
            current_job = current_job.next_job
        current_job.next_job = new_job

\
first_job_id = jobs_head.id if jobs_head else None
first_task_id = jobs_head.tasks_head.id if jobs_head and jobs_head.tasks_head else None
print(first_job_id, first_task_id)
