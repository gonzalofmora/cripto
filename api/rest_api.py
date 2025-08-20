from dotenv import dotenv_values
import logging
from binance_common.configuration import ConfigurationRestAPI
from binance_common.constants import WALLET_REST_API_PROD_URL
from binance_sdk_wallet.wallet import Wallet
from binance_sdk_wallet.rest_api.models import AccountInfoResponse

variables = dotenv_values()
logging.basicConfig(level=logging.INFO)
configuration = ConfigurationRestAPI(api_key=variables.get("API_KEY"), api_secret=variables.get("SECRET_KEY"), base_path=WALLET_REST_API_PROD_URL)

client = Wallet(config_rest_api=configuration)

def account_info():
    try:
        response = client.rest_api.account_info()

        data: AccountInfoResponse = response.data()
        logging.info(f"account_info() response: {data}")
    except Exception as e:
        logging.error(f"account_info() error: {e}")

def daily_account_snapshot():
    try:
        response = client.rest_api.daily_account_snapshot(
                type="SPOT",
        )

        rate_limits = response.rate_limits
        logging.info(f"daily_account_snapshot() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"daily_account_snapshot() response: {data}")
    except Exception as e:
        logging.error(f"daily_account_snapshot() error: {e}")
        
