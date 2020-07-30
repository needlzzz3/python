import re
from fixture import contact
from model.contact import Contact

def test_full_contact_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_bd = sorted(db.get_contact_list(),  key=Contact.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_bd)
    for z in range(len(contact_from_home_page)):
        assert contact_from_home_page[z].firstname == contact_from_bd[z].firstname
        assert contact_from_home_page[z].lastname == contact_from_bd[z].lastname
        assert contact_from_home_page[z].address == contact_from_bd[z].address
        assert contact_from_home_page[z].email == contact_from_bd[z].merge_emails_like_on_home_page
        assert contact_from_home_page[z].all_phones_from_home_page == contact_from_bd[z].merge_phones_like_on_home_page


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.home == contact_from_edit_page.home
#    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#    assert contact_from_view_page.work == contact_from_edit_page.work
#    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2