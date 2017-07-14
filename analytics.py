import json
import plotly.plotly as py
import plotly.graph_objs as go
from collections import defaultdict


def read_data(path):
    with open(path) as f:
        data = json.loads(f.read())
    return data


def draw_all(data, output):
    result = defaultdict(int)
    for distro in data:
        for d in distro['data']:
            if d['Python_version'] not in ['', '--', '\xa0']:
                result[d['Python_version']] += 1


    labels = []
    values = []
    for k, v in sorted(result.items()):
        if v > 2:
            labels.append(k)
            values.append(v)

    trace = go.Pie(labels=labels, values=values)
    py.iplot([trace], filename=output)


def draw(data, output):
    result = defaultdict(int)
    for distro in data:
        if not distro['data']:
            continue
        if distro['data'][0]['Python_version'] not in ['', '--', '\xa0']:
            result[distro['data'][0]['Python_version']] += 1


    labels = []
    values = []
    for k, v in sorted(result.items()):
        labels.append(k)
        values.append(v)

    trace = go.Pie(labels=labels, values=values)
    py.iplot([trace], filename=output)


def draw6(data, output):
    result = defaultdict(int)
    for distro in data:
        if not distro['data']:
            continue
        if distro['data'][0]['Python_version'] not in ['', '--', '\xa0']:
            if distro['data'][0]['Python_version'].startswith('3'):
                result['Python 3'] += 1
            else:
                result['Python 2'] += 1


    labels = []
    values = []
    for k, v in sorted(result.items()):
        labels.append(k)
        values.append(v)

    trace = go.Pie(labels=labels, values=values)
    py.iplot([trace], filename=output)


if __name__ == '__main__':
    import sys

    data = read_data(sys.argv[1])
    draw(data, sys.argv[2])


