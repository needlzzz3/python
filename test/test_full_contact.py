import re

def clear(s):
    return re.sub("[() -]", "", s)

def merge_info_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.firstname, contact.lastname, contact.address,
                                         contact.home, contact.mobile, contact.work,
                                         contact.email, contact.email2, contact.email3,
                                         contact.phone2]))))

def test_check_all_contact_info(app):
    full_contact_from_home_page = app.contact.get_contact_list()[0]
    full_contact_from_edit_page = app.contact.get_all_contact_info_from_edit_page(0)
    assert full_contact_from_home_page.contact_cache == merge_info_like_on_home_page(full_contact_from_edit_page)