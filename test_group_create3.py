from models.group import Group


def test_group_create(app, init_login):
    group = Group("TEST170710_1","comment170710_1",  "test170710")
    app.open_group_page()
    app.create_new_group(group)
    # Verify group page
    assert "A new group has been entered into the address book." in app.message()
    app.return_to_group_page()
    app.Logout()


