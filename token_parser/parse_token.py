import requests
import json

from dotenv import dotenv_values

from solana.rpc.api import Client

client = Client("https://api.devnet.solana.com")

config = dotenv_values(".env")


def check_token_data(token:str):
    url = f"https://solsniffer.com/api/v2/token/{token}"

    header = {
    "X-API-KEY": config["sol_sniffer_token"],
    "accept": "application/json"
    }

    response = requests.get(url=url, headers=header)


    response_dict = json.loads(response.text)
    tokne_data = parse_token_info(response_dict)
    return tokne_data


def parse_token_info(token_response):

    token = {}

    token["token_data"] = token_response.get("tokenData")

    token["overview"] = token_response.get("tokenOverview")
    token["market_cap"] = token_response.get("marketCap")
    token["holders"] = token_response.get("ownersList", [])
    token["token_name"] = token_response.get("tokenName")
    token["ticker"] = token_response.get("tokenSymbol")

    token["token_info"] = token_response.get("tokenInfo")

    return token
