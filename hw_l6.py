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
    text = addresses.strip().lower()
    return text
print(("1 ") + normalize_addresses(email5["from"]))
print(("1 ") + normalize_addresses(email5["to"]))

def add_short_body(email):
    """
    Возвращает email с новым ключом email["short_body"] —
    первые 10 символов тела письма + "...".
    """
    email_body = email["body"]
    email_body = email_body[:10] + "..."
    return email_body
print(("2 ") + add_short_body(email5))

def clean_body_text(body):
    """
    Заменяет табы и переводы строк на пробелы.
    """
    clean_body = email5["body"]
    clean_body = clean_body.replace("\n", " ").replace("\t", " ")
    return clean_body
print(("3 ") + clean_body_text(email5))