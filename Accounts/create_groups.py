from django.contrib.auth.models import Group,User
# from django.contrib.auth.models import Permission



def add_groups():
    # create groups of project
    group_names = ["admin","mentor","learner"]

    for group_name in group_names:
        new_group, created = Group.objects.get_or_create(name=group_name)
        # print("Added group", new_group)
        # if created:
        #     print(f"Group '{group_name}' was successfully created.")
        # else:
        #     print(f"Group '{group_name}' already exists.")
    
    try:
        # superuser = User.objects.get(username="admin")  
        superusers = User.objects.filter(is_superuser=True)
        admin_group = Group.objects.get(name="admin")
        # set super user to admin group
        for superuser in superusers:
            admin_group.user_set.add(superuser)
    except User.DoesNotExist:
        print("Superuser does not exist.")
      
    except Group.DoesNotExist:
        print(f"Group '{group_name}' does not exist.")
        

    