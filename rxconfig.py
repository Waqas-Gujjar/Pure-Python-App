import reflex as rx
from decouple import config

DATABASE_URL = config("NEON_DATABASE_URL")


config = rx.Config(
    app_name="Python_App",
    db_url = DATABASE_URL,
)