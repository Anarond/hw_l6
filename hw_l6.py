from datetime import date

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


def add_short_body(email):
    """
    Возвращает email с новым ключом email["short_body"] —
    первые 10 символов тела письма + "...".
    """
    email_body = email["body"]
    email_body = email_body[:10] + "..."
    return email_body


def clean_body_text(body):
    """
    Заменяет табы и переводы строк на пробелы.
    """
    clean_body = email5["body"]
    clean_body = clean_body.replace("\n", " ").replace("\t", " ")
    return clean_body


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


def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    """
    Возвращает кортеж (is_subject_empty, is_body_empty).
    True, если поле пустое.
    """
    is_subject_empty = not subject.strip()
    is_body_empty = not body.strip()
    return is_subject_empty, is_body_empty


def mask_sender_email(login: str, domain: str) -> str:
    """
    Возвращает маску email: первые 2 символа логина + "***@" + домен.
    """
    return f"{login}[:2] + '***@' + {domain}"


def get_correct_email(email_list: list[str]) -> list[str]:
    """
    Возвращает список корректных email.
    """
    correct_email = []
    for email in email_list:
        clean_email = email.strip().lower()
        if "@" in clean_email and clean_email.endswith((".com", ".ru", ".net")):
            correct_email.append(clean_email)
    return correct_email


test_emails = [
    # Корректные адреса
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]


def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    """
    Создает словарь email с базовыми полями:
    'sender', 'recipient', 'subject', 'body'
    """
    return {"sender": sender, "recipient": recipient, "subject": subject, "body": body}


def add_send_date(email: dict) -> dict:
    """
    Возвращает email с добавленным ключом email["date"] — текущая дата в формате YYYY-MM-DD.
    """
    email["date"] = date.today().isoformat()
    return email


def extract_login_domain(address: str) -> tuple[str, str]:
    """
    Возвращает логин и домен отправителя.
    Пример: "user@mail.ru" -> ("user", "mail.ru")
    """
    address = address.strip()
    login, domain = address.split("@")
    return login, domain
