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

# id, message_id, time, status
checks = load_csv('staff/checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('staff/statuses.csv')

hash_table = {}

for el in statuses:
    # print(el)
    # print(el[2])
    if el[2] in hash_table:
        if el[4] == '2':
            hash_table[el[2]] += 1
    else:
        if el[4] == '2':
            hash_table[el[2]] = 1

# print(hash_table)
# print(list(hash_table.keys()))
# print(list(hash_table.values()))

plt.figure(figsize=(len(list(hash_table.keys())), max(hash_table.values()))) # Задаем размер графика
plt.barh(list(hash_table.keys()), list(hash_table.values()))  # Строим горизонтальный гистограмму
plt.title('График')
plt.xlabel('Правильно')
plt.ylabel('Группы')
plt.show()

# plt.plot(list(hash_table.values()), list(hash_table.keys()))
# plt.show()

# print(sorted(hash_table.items(), key=lambda item: item[1], reverse=True))
