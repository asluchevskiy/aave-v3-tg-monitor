TELEGRAM_BOT_ACCESS_KEY = ''
AAVE_MARKET = 'Scroll'  # Ethereum | Arbitrum | Scroll

try:
    from local_settings import *
except ImportError:
    ...
