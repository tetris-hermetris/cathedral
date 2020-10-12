Small graphic library for specific purpose: to generate stage projections in stained glass style. 

Deeply work in progress.

## TODO

- ~~make **engine**~~
- output via drawbot
- **render:** make outline width relative to q
- **render:** separate given img and generated one
- **utils:** implement normalize sequence function


## CURRENT STATE

It's take a simple scenario, like this:
```python
scenario = (
             (((0, 0), (0, 30)),     knob,    ('k1', 0)),
             (((0, 30), (0, 50)),    knob,    ('k1', 0, 100)),
             (((0, 50), (0, 80)),    knob,    ('k1', 100, 0)),
             (((0, 0), (0, 100)),    add,     ('sheep1', sheep, (300, (500,500), 'k1'))),
             )
```
Here we have a knob, which is set in 0 for first 30 frames, then knob's value grows to 100 from frame 30 to frame 50, then fall backward to zero from 50 to 80. And we place in frame a sheep primitive with scale 300, pivot point (500, 500) and our knob as a phase.

Now we can render scenario:
```python
    engine( scenario, 1, ('PIL', (1000, 1000), 1.5), ('cathedral/', 'test.gif'))
```

And the result:

![result](test.gif)

