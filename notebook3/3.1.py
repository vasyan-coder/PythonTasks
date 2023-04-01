import csv
import datetime
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
messages = load_csv('staff/messages.csv')
time = [0] * 7
task = [0, 1, 2, 3, 4, 5, 6]
for i in range(len(messages)):
    tmp = (messages[i][4][0:10])
    year = int(tmp[:4])
    mon = int(tmp[5:7])
    day = int(tmp[8:10])
    if messages[i][1] != 0:
        time[(datetime.date(year, mon, day).weekday())] += 1


print(type(task))
print(type(time))
plt.plot(task, time)
plt.show()
