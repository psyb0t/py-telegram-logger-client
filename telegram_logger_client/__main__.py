import argparse
import json
import os
import sys
import logging
from .telegram_logger_client import TelegramLoggerClient


def setup_logging(debug=False):
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger(__name__)
    logger.debug(f"Logging level set to: {logging.getLevelName(log_level)}")
    return logger


def main():
    parser = argparse.ArgumentParser(description="Send logs to telegram-logger service")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--base-url", help="Base URL of the telegram-logger service")
    parser.add_argument("--x-id", help="X-ID token for authentication")
    parser.add_argument(
        "--caller", required=True, help="Name of the calling application or service"
    )
    parser.add_argument(
        "--level", required=True, choices=["info", "warning", "error"], help="Log level"
    )
    parser.add_argument("--message", required=True, help="Log message")
    parser.add_argument("--error", help="Error message or description")
    parser.add_argument("--request-id", help="Request ID for tracing")
    parser.add_argument("--trace-id", help="Trace ID for distributed tracing")
    parser.add_argument("--span-id", help="Span ID for distributed tracing")
    parser.add_argument(
        "--data", type=json.loads, help="Additional data as JSON string"
    )

    args = parser.parse_args()
    logger = setup_logging(args.debug)

    logger.debug(f"Parsed arguments: {args}")

    # Get base_url and x_id from environment variables or command-line arguments
    base_url = args.base_url or os.environ.get("TELEGRAM_LOGGER_BASE_URL")
    x_id = args.x_id or os.environ.get("TELEGRAM_LOGGER_X_ID")

    logger.debug(f"Base URL: {base_url}")
    logger.debug(
        f"X-ID: {'*' * len(x_id) if x_id else None}"
    )  # Mask the actual X-ID for security

    if not base_url:
        logger.error(
            "Base URL is required. Set TELEGRAM_LOGGER_BASE_URL environment variable or use --base-url argument."
        )
        sys.exit(1)

    if not x_id:
        logger.error(
            "X-ID is required. Set TELEGRAM_LOGGER_X_ID environment variable or use --x-id argument."
        )
        sys.exit(1)

    client = TelegramLoggerClient(base_url, x_id)
    logger.debug("TelegramLoggerClient initialized")

    try:
        logger.debug("Attempting to send log")
        response = client.send_log(
            caller=args.caller,
            level=args.level,
            message=args.message,
            error=args.error,
            request_id=args.request_id,
            trace_id=args.trace_id,
            span_id=args.span_id,
            data=args.data,
        )
        logger.debug(f"Log sent successfully. Status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error sending log: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
