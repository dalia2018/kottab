from django.contrib.auth.models import Group,User
from django.contrib.auth.models import Permission

# create groups og project
group_names = ["admin","mentor","learner"]

for group_name in group_names:
    new_group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"Group '{group_name}' was successfully created.")
    else:
        print(f"Group '{group_name}' already exists.")

try:
    superuser = User.objects.get(username="admin")  
    admin_group = Group.objects.get(name="admin")
except User.DoesNotExist:
    print("Superuser does not exist.")
except Group.DoesNotExist:
    print(f"Group '{group_name}' does not exist.")

# set super user to admin group
admin_group.user_set.add(superuser)