import click
from tabulate import tabulate

from task import Task, get_task_by_id, get_tasks


@click.group()
def cli_task():
    """
    Welcome to the Python Task Tracker CLI application

    This application allow you to manage your tasks using CRUD operations.

    Creator: Bruno de Santana Santos
    https://github.com/BrunoSantanaS
    """
    pass


@click.command()
@click.option('--add', help='Create a new task')
@click.argument('description', required=True, type=str)
def add_task(add, description):
    """
    Adds a new task with the given description.

    Args:
        add (click.core.Context): The Click context object (not used in the function).
        description (str): The description of the task to be added.

    Returns:
        None
    """
    task = Task(description, 'todo')
    if task.create_task():
        click.echo(f'Task Added: {description}')
    else:
        click.echo(f'Error adding task: {description}')


@click.command()
@click.option('--update', help='Update a task')
@click.argument('id', required=True, type=int)
@click.argument('description', required=True, type=str)
def update_task(update, id, description):
    """
    Update the description of a task by its ID.

    Args:
        update (function): A function to update the task.
        id (int): The ID of the task to be updated.
        description (str): The new description for the task.
    Returns:
        None
    Side Effects:
        Prints a message indicating whether the task was successfully updated or if an error occurred.
    """
    task = get_task_by_id(id)

    if task is None:
        click.echo(f'Task not found: {id}')
        return

    update_data = {'description': description}
    if task.update_task(id, update_data):
        click.echo(f'Task Updated: {task.description} To: {description}')
    else:
        click.echo(f'Error updating task: {task.description} To: {description}')


@click.command()
@click.option('--delete', help='Delete a task')
@click.argument('id', required=True, type=int)
def delete_task(delete, id):
    """
    Deletes a task by its ID.

    Args:
        delete (bool): A flag indicating whether to delete the task.
        id (int): The ID of the task to be deleted.
    Returns:
        None: This function does not return a value. It prints messages to the console indicating the result of the delete operation.
    """
    task = get_task_by_id(id)

    if task is None:
        click.echo(f'Task not found: {id}')
        return

    if task.delete_task(id):
        click.echo(f'Task Deleted: {task.description}')
    else:
        click.echo(f'Error deleting task: {task.description}')

@click.command()
@click.option('--in_progress', help='Mark a task as in progress')
@click.argument('id', required=True, type=int)
def mark_in_progress(in_progress, id):
    """
    Mark a task as 'in-progress' based on its ID.

    Args:
        in_progress (bool): A flag indicating if the task is in progress.
        id (int): The unique identifier of the task to be updated.
    Returns:
        None: This function does not return a value. It prints the result of the operation.
    """
    task = get_task_by_id(id)

    if task is None:
        click.echo(f'Task not found: {id}')
        return

    update_data = {'status': 'in-progress'}
    if task.update_task(id, update_data):
        click.echo(f'Task status updated: {task.description} (in progress)')
    else:
        click.echo(f'Error updating status: {task.description} (in progress)')


@click.command()
@click.option('--done', help='Mark a task as in progress')
@click.argument('id', required=True, type=int)
def mark_done(done, id):
    """
    Marks a task as 'done' based on the provided task ID.

    Args:
        done (bool): A flag indicating if the task is done.
        id (int): The unique identifier of the task to be marked as done.
    Returns:
        None: This function does not return a value. It prints messages to the console
              indicating the result of the operation.
    """
    task = get_task_by_id(id)

    if task is None:
        click.echo(f'Task not found: {id}')
        return

    update_data = {'status': 'done'}
    if task.update_task(id, update_data):
        click.echo(f'Task status updated: {task.description} (in progress)')
    else:
        click.echo(f'Error updating status: {task.description} (in progress)')

@click.command()
@click.option('--todo', help='Mark a task as to do')
@click.argument('id', required=True, type=int)
def mark_to_do(todo, id):
    """
    Marks a task as 'todo' based on the provided task ID.

    Args:
        todo: Placeholder argument, not used in the function.
        id (int): The ID of the task to be marked as 'todo'.
    Returns:
        None: This function does not return a value. It prints messages to the console
              indicating the success or failure of the operation.
    """
    task = get_task_by_id(id)

    if task is None:
        click.echo(f'Task not found: {id}')
        return

    update_data = {'status': 'todo'}
    if task.update_task(id, update_data):
        click.echo(f'Task status updated: {task.description} (todo)')
    else:
        click.echo(f'Error updating status: {task.description} (todo)')

@click.command()
@click.option('--list', help='List all tasks')
@click.argument('filter_by', required=False, type=click.Choice(['todo', 'in-progress', 'done'], case_sensitive=True))
def list_task(list, filter_by):
    """
    Lists tasks based on the provided filter.

    Args:
        list (str): The list of tasks to be displayed.
        filter_by (str): The filter criteria to apply when retrieving tasks.
    Returns:
        None: Prints the tasks in a tabulated format if tasks are found,
              otherwise prints "No tasks found".
    """
    if filter_by:
        tasks = get_tasks(filter_by)
    else:
        tasks = get_tasks()

    if tasks:
        headers = tasks[0].keys()
        rows = [task.values() for task in tasks]
        table = tabulate(rows, headers, tablefmt='grid')
        click.echo(table)
        return

    return click.echo("No tasks found")

cli_task.add_command(add_task, name='add')
cli_task.add_command(update_task, name='update')
cli_task.add_command(delete_task, name='delete')
cli_task.add_command(mark_in_progress, name='mark-in-progress')
cli_task.add_command(mark_done, name='mark-done')
cli_task.add_command(list_task, name='list')
cli_task.add_command(mark_to_do, name='mark-to-do')

if __name__ == '__main__':
    cli_task()
