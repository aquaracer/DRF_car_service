from django.contrib.auth.models import Group, Permission

editors_permission_list = ['Can view Категория',
                           'Can view Сотрудник',
                           'Can view Услуга',
                           'Can add Услуга',
                           'Can change Услуга']
moderators_permission_list = ['Can delete Услуга',
                              'Can change Сотрудник',
                              'Can add Сотрудник'] + editors_permission_list
editors_permission_id = Permission.objects.filter(name__in=editors_permission_list).values('id')
moderators_permission_id = Permission.objects.filter(name__in=moderators_permission_list).values('id')
group_editors = Group.objects.get_or_create(name='editors')
group_moderators = Group.objects.get_or_create(name='moderators')
if type(group_moderators) == tuple:
    group_moderators = group_moderators[0]
if type(group_editors) == tuple:
    group_editors = group_editors[0]
for permission in editors_permission_id:
    group_editors.permissions.add(permission['id'])
for permission in moderators_permission_id:
    group_moderators.permissions.add(permission['id'])
