from remote.auth import (
    delete_password,
    password_exists,
    setup_password,
    verify_password,
    change_password,
    get_password_info,
)

delete_password()

print(password_exists())

setup_password("123456")

print(password_exists())

print(verify_password("123456"))

print(verify_password("abcdef"))

print(change_password("123456", "654321"))

print(verify_password("654321"))

print(get_password_info())
