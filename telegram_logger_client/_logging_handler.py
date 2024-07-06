import logging
import os
from typing import Optional
from ._telegram_logger_client import TelegramLoggerClient
from ._constants import (
    ENV_VAR_TELEGRAM_LOGGER_BASE_URL,
    ENV_VAR_TELEGRAM_LOGGER_X_ID,
)


class TelegramLoggerHandler(logging.Handler):
    def __init__(
        self,
        base_url: str,
        x_id: str,
        show_originating_file: bool = False,
        *args,
        **kwargs,
    ):
        super(TelegramLoggerHandler, self).__init__(*args, **kwargs)
        self.client = TelegramLoggerClient(base_url, x_id)
        self.show_originating_file = show_originating_file

    def emit(self, record):
        try:
            message = record.getMessage()

            data = {}
            if self.show_originating_file:
                data["file"] = f"{record.pathname}:{record.lineno}"

            if record.exc_info:
                data["exception"] = self.formatter.formatException(record.exc_info)

            self.client.send_log(
                caller=record.name,
                level=record.levelname.lower(),
                message=message,
                error=record.exc_text if record.exc_info else None,
                request_id=getattr(record, "request_id", None),
                trace_id=getattr(record, "trace_id", None),
                span_id=getattr(record, "span_id", None),
                data=data,
            )
        except Exception as e:
            self.handleError(record)


class TelegramLogFormatter(logging.Formatter):
    def format(self, record):
        # This formatter is now only used for console output, if needed
        return super().format(record)


def attach_to_logger(
    logger: logging.Logger,
    base_url: Optional[str] = None,
    x_id: Optional[str] = None,
    level: Optional[int] = None,
    show_originating_file: bool = False,
):
    """
    Set up Telegram logging for an existing logger instance.
    :param logger: The logger instance to modify
    :param base_url: The base URL of the Telegram Logger service (optional)
    :param x_id: The X-ID token for authentication (optional)
    :param level: The logging level for the Telegram Logger handler (optional)
    """
    base_url = base_url or os.environ.get(ENV_VAR_TELEGRAM_LOGGER_BASE_URL)
    x_id = x_id or os.environ.get(ENV_VAR_TELEGRAM_LOGGER_X_ID)

    if not base_url or not x_id:
        raise ValueError(
            "Both base_url and x_id must be provided either as arguments or through environment variables."
        )

    telegram_handler = TelegramLoggerHandler(base_url, x_id, show_originating_file)
    telegram_handler.setFormatter(TelegramLogFormatter())

    if level is not None:
        telegram_handler.setLevel(level)

    logger.addHandler(telegram_handler)
    return logger
