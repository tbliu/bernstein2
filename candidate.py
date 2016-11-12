from gravitation import Source, System

coords_data = {'LINDSEY GRAHAM': [-1, -1, 0, 0, -1, 0, 0, -1, -1, -1]}
source_data = {'LINDSEY GRAHAM': [Source([1,-1,-1,-1,-1,-1,0,-1,-1,1], 5000, 'Country First PAC'),
                                  Source([0,-1,-1,-1,0,-1,0,-1,-1,-1], 5000, 'Fund for America\'s Future')]}


class Candidate:
    def __init__(self, name):
        self.name = name
        self.sources = source_data[self.name]
        self.coords = coords_data[self.name]

        sys = System(self.coords)
        for src in self.sources:
            sys.add_source(src)

        self.predicted = sys.barycenter
        self.dark_src = sys.calc_projected()

    def __str__(self):
        strcs = ''
        for src in self.sources:
            strcs += '\n\t' + str(src)

        return 'Name: ' + str(self.name) + \
               '\nSources: ' + strcs + \
               '\nGround truth: ' + str(self.coords) + \
               '\nPredicted: ' + str(self.predicted) + \
               '\nDark source: ' + str(self.dark_src)



