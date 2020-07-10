# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="F", middlename="F", lastname="F", nickname="FFF", title="FFF", company="none",
                      address="none", home="adress", mobile="none",
                      work="none", fax="none", email="none", email2="none", address2="none", phone2="none",
                      notes="none contact")
    app.contact.contact(contact)
    assert (len(old_contacts) + 1) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


 #def test_add_empty_contact(app):
 #    old_contacts = app.contact.get_contact_list()
 #    contact = Contact(firstname="a", middlename="a", lastname="a", nickname="a", title="a", company="none",
 #                      address="none", home="adress", mobile="none",
 #                     work="none", fax="none", email="none", email2="none", address2="none", phone2="none",
 #                     notes="none contact")
 #    app.contact.contact(contact)
 #   new_contacts = app.contact.get_contact_list()
 #    assert (len(old_contacts) + 1) == len(new_contacts)
 #    old_contacts.append(contact)
  #   assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
