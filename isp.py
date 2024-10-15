class Workable:
    def work(self):
        raise NotImplementedError

class Eatable:
    def eat(self):
        raise NotImplementedError

class HumanWorker(Workable, Eatable):
    def work(self):
        return "Human is working."

    def eat(self):
        return "Human is eating."

class RobotWorker(Workable):
    def work(self):
        return "Robot is working."

# The RobotWorker only implements 'work', not 'eat', adhering to ISP.

def process_work(worker: Workable):
    print(worker.work())

def process_eat(worker: Eatable):
    print(worker.eat())

# Main program block
human = HumanWorker()
robot = RobotWorker()

process_work(human)  # Human works
process_eat(human)   # Human eats

process_work(robot)  # Robot works
# process_eat(robot)  # Uncommenting this will violate ISP as RobotWorker doesn't have eat method.
