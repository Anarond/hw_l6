from datetime import date

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

def build_sent_text(email: dict) -> str:
    """
    Формирует текст письма в формате:

    Кому: {to}, от {from}
    Тема: {subject}, дата {date}
    {clean_body}
    """
    a = f"Кому: {normalize_addresses(email5['to'])}, от {normalize_addresses(email5['from'])}"
    b = f"Тема: {(email['subject'])}, дата {date.today()}"
    c = clean_body_text(email5)
    return f"{a}\n{b}\n{c}"
print(("4 ") + build_sent_text(email5))

def check_empty_fields(subject: str, body:str) -> tuple[bool, bool]:
    """
    Возвращает кортеж (is_subject_empty, is_body_empty).
    True, если поле пустое.
    """
    is_subject_empty = not subject.strip()
    is_body_empty = not body.strip()
    return is_subject_empty, is_body_empty
print(("5 ") + str(check_empty_fields(email5["subject"], email5["body"])))

def mask_sender_email(login: str, domain: str) -> str:
    """
    Возвращает маску email: первые 2 символа логина + "***@" + домен.
    """
    return f"{login}[:2] + '***@' + {domain}"
