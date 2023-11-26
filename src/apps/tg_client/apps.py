from config.logger import logger
from config.telegram import CLIENT_SESSION_BOT
from config.telegram import CLIENT_SESSION_SEARCH
from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_default_sessions(sender, **kwargs):
    from apps.tg_client.models import ClientSession, Login

    search, created_search = ClientSession.objects.get_or_create(name=CLIENT_SESSION_SEARCH)
    if created_search:
        logger.info("search session created")

    bot, created_bot = ClientSession.objects.get_or_create(name=CLIENT_SESSION_BOT)
    if created_bot:
        logger.info("bot session created")

    login_search, created_login_search = Login.objects.get_or_create(client_session=search)
    if created_login_search:
        logger.info("search login created")

    login_bot, created_login_bot = Login.objects.get_or_create(client_session=bot)
    if created_login_bot:
        logger.info("bot login created")


class TgClientConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.tg_client"

    def ready(self):
        post_migrate.connect(init_default_sessions, sender=self)
