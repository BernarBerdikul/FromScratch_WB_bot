from scratch_bot.core.models import Guest
from typing import Optional


def create_guest(message):
    try:
        user_instance = message.chat
        username: Optional[str] = user_instance.username
        if not Guest.objects.filter(username=username).exists():
            first_name: Optional[str] = user_instance.first_name
            last_name: Optional[str] = user_instance.last_name
            Guest.objects.create(first_name=first_name,
                                 last_name=last_name,
                                 username=username)
    except Exception:
        pass
