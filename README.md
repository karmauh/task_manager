# Task Manager

This simple Python script serves as a basic task manager. Users can add tasks for specific dates, display tasks for a given date, and exit the program.

## How to Use

1. Run the script in a Python environment.
2. Follow the on-screen instructions to interact with the task manager.

### Commands

- `add_task [date] [task]`: Adds a task for a specified date. The date should be in the format YYYY:MM:DD. For example, `add_task 2023:12:04 test czy dziala` will add the task "test czy dziala" for the date December 4, 2023.

- `display_task [date]`: Displays tasks for the specified date. If no date is provided, it displays all tasks.

- `exit`: Exits the task manager.

## Example

```bash
add_task 2023:12:04 test czy dziala
```
### Notes
- Tasks are stored in a dictionary (tasks) where keys are dates, and values are lists of tasks for each date.
The script runs in an infinite loop until the user chooses to exit.
- Feel free to use and modify the script according to your needs. If you encounter any issues or have suggestions for improvements, please let me know!
