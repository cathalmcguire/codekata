def extract_data(filename, min_length):
    """
    get the lines from tables that hold the relevant data
    """
    f = open(filename, 'r')
    lines = f.readlines()
    data = []
    for line in lines:
        line = line.split()
        if len(line) > min_length:
            data.append(line)
    del data[0]
    return data


def get_min_spread(data, max_index, min_index, label_index):
    """
    return the nin spread and data label
    """
    min_spread = 10000
    labels = []
    for line in data:
        spread = int(line[max_index]) - int(line[min_index])
        if spread < 0:
            spread = int(line[min_index]) - int(line[max_index])
        if spread < min_spread:
            labels = [line[label_index]]
            min_spread = spread
        elif spread == min_spread:
            labels.append(line[label_index])
    return [min_spread, labels]


data = extract_data('weather.dat', 13)
spread = get_min_spread(data, 1, 2, 0)
print 'Day(s) with min temp spread of %s degrees: %s' % (spread[0],
                                                ' '.join(spread[1]))

data = extract_data('football.dat', 7)
spread = get_min_spread(data, 6, 8, 1)
print 'Team(s) with min goal difference spread of %s: %s' % (spread[0],
                                                ' '.join(spread[1]))
