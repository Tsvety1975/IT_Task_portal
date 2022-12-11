from IT_TaskPortal.tasks.models import TaskForNewWorker

# this is for images ir i need it later
# def megabytes_to_bytes(mb):
#     return mb * 1024 * 1024


def is_owner(request, obj):
    return request.user == obj.user

def get_task_new_user_by_username_task_pk(task_new_user_pk):
    return TaskForNewWorker.objects.get(pk= task_new_user_pk)