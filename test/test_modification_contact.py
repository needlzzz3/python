from model.contact import Contact
from random import randrange


def test_modification_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact (firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact (firstname="new")
    contact.id = old_contacts[index].id
    app.contact.modificate_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def test_modificate_group_name(app):
        if app.group.count() == 0:
            app.group.create(Group(name="test"))
        old_groups = app.group.get_group_list()
        index = randrange(len(old_groups))
        group = Group(name="new")
        group.id = old_groups[index].id
        app.group.modificate_group_by_index(index, group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

