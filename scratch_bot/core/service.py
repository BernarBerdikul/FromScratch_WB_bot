from typing import Optional

from scratch_bot.core.models import Guest


def create_guest(message):
    try:
        user_instance = message.chat
        first_name: Optional[str] = user_instance.first_name
        last_name: Optional[str] = user_instance.last_name
        username: Optional[str] = user_instance.username
        Guest.objects.create(
            first_name=first_name, last_name=last_name, username=username
        )
    except Exception:
        pass
