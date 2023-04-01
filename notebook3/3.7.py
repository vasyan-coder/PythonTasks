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


# Создадим словарь, в котором будем хранить количество правильных и неправильных решений для каждой задачи
# Ключами будут номера задач, а значениями будут списки количества правильных и неправильных решений для каждой задачи.
task_results = {}
for row in statuses:
    task = row[0]
    is_correct = row[4] == '2'
    if task in task_results:
        correct, wrong = task_results[task]
        if is_correct:
            correct += 1
        else:
            wrong += 1
        task_results[task] = correct, wrong
    else:
        task_results[task] = (1 if is_correct else 0, 0 if is_correct else 1)

# Создадим список списков с названием задач, средним количеством правильных и неправильных решений
table = []
for task, (correct, wrong) in task_results.items():
    total = correct + wrong
    avg_correct = correct / total
    avg_wrong = wrong / total
    table.append([task, avg_correct, avg_wrong])

# Отсортируем список по убыванию среднего количества правильных решений
table.sort(key=lambda x: x[1], reverse=True)

# Выведем результаты в виде таблицы
print(
    f"{'Название задачи':<20} {'Среднее количество правильных решений':<40} {'Среднее количество неправильных решений':<40}")
for row in table:
    task, avg_correct, avg_wrong = row
    print(f"{task:<20} {avg_correct:<40.2f} {avg_wrong:<40.2f}")

# Создаем график
plt.figure(figsize=(10, 6))  # Задаем размер графика
plt.barh(list(task_results.keys()), [x[0] / sum(x) for x in task_results.values()])  # Строим горизонтальный гистограмму
plt.title('Самые легкие и сложные задачи')
plt.xlabel('Среднее количество правильных решений')
plt.ylabel('Номер задачи')
plt.show()
