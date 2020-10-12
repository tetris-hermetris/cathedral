from cathedral.engine.core import *

if __name__ == "__main__":

    scenario = (
             (((0, 0), (0, 30)),     knob,    ('k1', 0)),
             (((0, 30), (0, 50)),    knob,    ('k1', 0, 100)),
             (((0, 50), (0, 80)),    knob,    ('k1', 100, 0)),
             (((0, 0), (0, 100)),    add,     ('sheep1', sheep, (300, (500,500), 'k1'))),
             )

    engine( scenario, 1, ('PIL', (1000, 1000), 1.5), ('cathedral/', 'test.gif'))