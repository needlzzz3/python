from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random
from fixture import orm


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app, db):
     groups = db.get_group_list()
     contacts = db.get_contact_list()
     if len(groups) == 0:
         app.group.create(Group(name="free_group"))
     if len(contacts) == 0:
         app.contact.contact(Contact(firstname="test"))
     # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, если таковых нет, то создаем
     contacts_without_groups = orm.contacts_without_groups()
     groups_without_contacts = orm.groups_without_contacts()
     if len(groups_without_contacts) == 0:
         app.group.create(Group(name="free_group"))
         groups_without_contacts = orm.groups_without_contacts()
     if len(contacts_without_groups) == 0:
         app.contacts.create_contact(AddNew(my_f_name="free_contact"))
         contacts_without_groups = orm.contacts_without_groups()
     # добавляем первый свободный контакт в первую свободную группу
     app.contacts.add_contact_to_group(contacts_without_groups[0], groups_without_contacts[0])
     print("Contact with id %s has been successfully added to the group with id %s" % (contacts_without_groups[0], groups_without_contacts[0]))
     # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, после добавления
     new_contacts_without_groups = orm.contacts_without_groups()
     new_groups_without_contacts = orm.groups_without_contacts()
     # проверяем, что список свободных групп и контактов изменился на 1
     assert len(contacts_without_groups) == len(new_contacts_without_groups) + 1
     assert len(groups_without_contacts) == len(new_groups_without_contacts) + 1