import datetime

from django.db import models as models_base
from django.contrib.auth import models as models_auth
from django.utils import timezone


class UserExtended(models_auth.User):
    join_date = models_base.DateTimeField("date joined")

    def __str__(self):
        return f"{self.username}: {self.last_name} {self.first_name}"

    def is_birthday(self) -> bool:
        now = timezone.now()
        return now.year != self.join_date.year and now.month == self.join_date.month and now.day == self.join_date.day
