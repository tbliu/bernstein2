import numpy as np


class Source:
    def __init__(self, coords, weight, name=None):
        self.coords = np.asarray(coords)
        self.weight = weight
        self.name = name

    def __str__(self):
        return 'Source ' + self.name + ', ' + str(self.coords) + ', ' + str(self.weight)


class System:
    def __init__(self, ground_truth):
        self.ground_truth = np.asarray(ground_truth)
        self.sources = []
        self.barycenter = None

    def add_source(self, src):
        self.sources.append(src)
        self.barycenter = self.calc_barycenter()

    def calc_barycenter(self):
        accumulator = self.sources[0].coords*self.sources[0].weight
        weight_sum = 0.0
        for src in self.sources:
            accumulator += src.coords*src.weight
            weight_sum += src.weight
        return (accumulator + -1*self.sources[0].coords*self.sources[0].weight)/weight_sum

    def calc_projected(self):
        weight_sum = 0.0
        for src in self.sources:
            weight_sum += src.weight
        p = ((weight_sum+1)*self.ground_truth) - (self.barycenter*weight_sum)
        m = np.amax(p)
        return Source(p/m, m, '<dark source>')