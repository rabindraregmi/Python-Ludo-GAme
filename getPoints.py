'''
Code for movement of gatti along a snake or ladder
get_points fxn returns a list of all points which lies on the given line
Two points of the line i.e. origin and target must be passed
'''

def slope(origin, target):
    if target['x'] == origin['x']:
        return 0
    else:
        m = (float(target['y'] - origin['y'])) / (target['x'] - origin['x'])
        return m

def line_eqn(origin, target):
    x = origin['x']
    y = origin['y']
    c = y - (slope(origin, target)*x)
    m = slope(origin, target)
    return {'m':m, 'c':c}

#get y for a value of x
def get_y(x, slope, c):
    # y = mx + c
    y = (slope*x) + c
    return y


def get_points(origin, target):
    coord_list = []
    if origin['x']>target['x']:
        step=-1
    else:
        step=1
    for i in range(origin['x'], target['x']+step,step):
        eqn = line_eqn(origin, target)
        y = get_y(i, eqn['m'], eqn['c'])
        coord_list.append([i, int(y)])
    return coord_list

