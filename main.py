# Standard Library
import logging
import os
from logging import getLogger
from pathlib import Path

# Third Party Library
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(
    format="[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d] - %(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)

load_dotenv(dotenv_path=Path(__file__).parents[0] / ".env")

CONST_SLACK_BOT_USER_OAUTH_TOKEN: str = os.environ.get("SLACK_BOT_USER_OAUTH_TOKEN", "")
if not CONST_SLACK_BOT_USER_OAUTH_TOKEN:
    raise RuntimeError("SLACK_BOT_USER_OAUTH_TOKEN is not set")
CONST_SLACK_BOT_APP_LEVEL_TOKEN: str = os.environ.get("SLACK_BOT_APP_LEVEL_TOKEN", "")
if not CONST_SLACK_BOT_APP_LEVEL_TOKEN:
    raise RuntimeError("SLACK_BOT_APP_LEVEL_TOKEN is not set")

app = App(token=CONST_SLACK_BOT_USER_OAUTH_TOKEN)


@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")


if __name__ == "__main__":
    SocketModeHandler(app, CONST_SLACK_BOT_APP_LEVEL_TOKEN).start()
