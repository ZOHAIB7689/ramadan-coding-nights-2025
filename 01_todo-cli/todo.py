import click 
import json
import os

TODO_FILE ="todo.json"


def todo_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = json.load(file)
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file , indent=4)

@click.group()
def cli ():
    """Simple Todo List Manager"""


@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = todo_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task '{task}' added to the list")

cli.add_command(add)


@click.command()
def list():
    """List all the tasks"""
    tasks = todo_tasks()
    if not tasks:
        click.echo("No tasks found")
    for index, task in enumerate(tasks , 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} {status}")


@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = todo_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed")
    else:
        click.echo("Invalid task number")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = todo_tasks()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task {task_number} removed from the list")
    else:
        click.echo("Invalid task number")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()