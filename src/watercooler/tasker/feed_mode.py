from watercooler.config.models import Model
from watercooler.tasker.helpers import get_task_by_model


def feed_mode(prompt: str, models: list[Model]):
    tasks = []
    for model in models:
        task = get_task_by_model(prompt, model)
        tasks.append(task)
    return tasks
