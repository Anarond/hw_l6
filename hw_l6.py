# 1. Создайте словарь email
email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "  lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam",
}

def normalize_addresses(addresses):
    """
    Возвращает значение, в котором адрес приведен к нижнему регистру и очищен от пробелов по краям.
    """
    return addresses.strip().lower()

print(normalize_addresses(email5["from"]))
print(normalize_addresses(email5["to"]))

