class Participant:
    def __init__(self,name,distance,runs):
        self.name = ''
        self.distance = 0
        self.runs = 0

    def add_distance(d):
        distance = d
    # add single distance to the distance accumulator and increments runs by 1. Argument d is a single float.
    def add_distances(ds):
        distance = sum(ds)
    # add an array of distances to distance accumulator. Argument ld is a list of floats. getDistance()
    def get_name(self):
        return self.name
    # get the name of the participant of the current instance
    def get_distance(self):
        return self.distance
    # get the current value of the distance accumulator.
    def get_runs(self):
        return self.runs
    # get the current value of the runs accumulator
    def __str__(self):
        return 'Name:' + self.name + '\n' + 'Distance:' + str(self.distance) + '\n' + 'Runs' + str(self.runs)
    # stringify method. Returns a string with name, total distance run and how many distances the object added, according to the following format:
    # Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
    # where xxxxxxxxxxxxxxxxxxx is a right align string of 20 characters for the name, yyyy.yyyy is the total distance run with 9 digits, decimal point and
    # 4 decimals, and zzzz is the number of runs with 4 digits, no decimals.


