import click


@click.group()
def cli_task():
    pass


@click.command()
@click.option('--add', help='Create a new task')
@click.argument('description', required=True, type=str)
def add_task(add, description):
    click.echo(f'Task Added: {description}')


@click.command()
@click.option('--update', help='Update a task')
@click.argument('id', required=True, type=int)
@click.argument('description', required=True, type=str)
def update_task(update, id, description):
    click.echo(f'Task Updated: {id} - {description}')


@click.command()
@click.option('--delete', help='Delete a task')
@click.argument('id', required=True, type=int)
def delete_task(delete, id, ):
    click.echo(f'Task Deleted: {id}')


cli_task.add_command(add_task, name='add')
cli_task.add_command(update_task, name='update')
cli_task.add_command(delete_task, name='delete')

if __name__ == '__main__':
    # cli_task()

    from utils import FileHandler
    from task import Task

    task = Task('task 2', 'todo', '2020-01-01', '2020-01-01')
    file_handler = FileHandler()
    file_handler.add_task(task)
