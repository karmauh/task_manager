tasks = {
    "2023:12:04": ["test czy dziala"]
}

def add_task(date, task):
    if date in tasks.keys():
        tasks[date].append(task)
    else:
        tasks[date] = [task]

def display_task(date=None):
    if date == None:
        print(tasks)
    elif date in tasks.keys():
        print(tasks[date])
    else:
        print('There is not task with date you entered.')


if __name__ == '__main__':
    while True:
        print('\t     HELP\t\t\n'
              'type command in format:\n'
              '[command] [date] [task]\n'
              '\t    YYYY:MM:DD\n')

        print('\tCOMMANDS:\n'
              'add_task\n'
              'display_task\n'
              '\n'
              'exit\n')

        user_input = str(input('Enter what you want to do: ')) # add_task 2023:12:04 przykladowe zadanie
        command_parts = user_input.split(' ')

        command = command_parts[0]
        arrgs = ' '.join(command_parts[1:])
        arrgs_date = arrgs[0:10]
        arrgs_task = arrgs[11:]
        # print(command_parts)
        # print(command)
        # print(arrgs_date)
        # print(arrgs_task)

        if command == 'add_task' or command == 'add task':
            add_task(arrgs_date, arrgs_task)
        elif command == 'display_task' or command == 'display task':
            display_task(arrgs_date)
        elif command == 'exit':
            break