# python3
from collections import namedtuple
import heapq


class JobScheduling:

    def __init__(self):
        self.AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
        self.n_workers = 0
        self.n_jobs = 0
        self.threads = []
        self.finish_time = []
        self.timer = []
        self.jobs = []
        self.result = []

    def read_data(self):
        self.n_workers, self.n_jobs = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert len(self.jobs) == self.n_jobs

        self.threads = [0] * self.n_workers
        self.finish_time = [0] * self.n_workers
        self.timer = [0] * self.n_workers

    def print_data(self):
        for job in self.result:
            print(job[0], job[1])

    def assign_job(self):
        '''heapq.heapify(self.jobs)
        print(self.jobs)
        rem = heapq.heappop(self.jobs)
        print(rem)
        print(self.jobs)'''

        '''for i in range(len(self.jobs)):
            queue.put(self.jobs[i])
        for j in range(len(self.jobs)):
            print(queue.get())'''

        # heapq.heapify(self.jobs)
        '''print(self.jobs)
        self.jobs.pop(0)
        print(self.jobs)
        self.jobs.pop(0)
        print(self.jobs)'''
        timer1 = 0
        timer2 = 0
        while len(self.jobs) != 0:
            for i in range(len(self.threads)):
                if self.threads[i] == 0:
                    if len(self.jobs) != 0:

                        # print(self.jobs)
                        # print(self.jobs.pop(0))
                        task = self.jobs.pop(0)
                        # print(task)

                        # task = heapq.heappop(self.jobs)
                        self.threads[i] = task
                        self.timer[i] = task
                        self.result.append((i, self.finish_time[i]))
                        self.finish_time[i] += task

            minimum = min(self.timer)
            for i in range(len(self.threads)):
                if self.threads[i] >= minimum:
                    self.threads[i] -= minimum
                else:
                    self.threads[i] -= 1

    def assign_job1(self):
        next_free_time = [0] * self.n_workers

        for job in self.jobs:
            next_worker = min(range(self.n_workers), key=lambda w: next_free_time[w])
            self.result.append(self.AssignedJob((next_worker), next_free_time[next_worker]))
            next_free_time[next_worker] += job

            '''for i in range(len(self.threads)):
                self.threads[i] -= 1'''

    def solve(self):
        self.read_data()
        self.assign_job()
        self.print_data()


if __name__ == '__main__':
    js = JobScheduling()
    js.solve()
