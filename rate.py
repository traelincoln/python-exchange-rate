import requests
import argparse


def get_json(url, params={}, fallback_url=None, network_retries=3):
    try:
        res = requests.get(url, params)
        res.raise_for_status()
        return res.json()
    except requests.ConnectTimeout:
        if network_retries >= 1:
            print("Network error retrying", end="\r")
            network_retries -= 1
            if fallback_url:
                url, fallback_url = fallback_url, url
            return get_json(
                url, fallback_url, network_retries
            )  # recursively attempt reconnect until for specified number of retries
        return None
    except requests.RequestException:
        return None
    except (ValueError, TypeError, KeyError):
        return None


def fx_all_currencies():
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
    fallback_url = (
        "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    )
    return get_json(url, fallback_url=fallback_url, network_retries=1)


def fx_conversion_rate(FROM, TO):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{FROM}/{TO}.min.json"
    fallback_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{FROM}/{TO}.json"
    return get_json(url, fallback_url=fallback_url, network_retries=3)


def fx_all_rates(base="usd"):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base}.min.json"
    fallback_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base}.json"
    return get_json(url, fallback_url=fallback_url, network_retries=1)


def main():
    parser = argparse.ArgumentParser(
        description="Get foreign currency exchange rates on command line."
    )

    parser.add_argument(
        "cur_from",
        metavar="CURRENCY FROM",
        type=str,
        help="Symbol of currency to convert from.",
    )

    parser.add_argument(
        "cur_to",
        metavar="CURRENCY TO",
        type=str,
        help="Symbol of currency to convert to.",
    )

    parser.add_argument(
        "amount",
        metavar="EXCHANGE AMOUNT",
        nargs="?",
        type=int,
        default=1,
        help="Quantity of currency to convert. Defaults to 1",
    )

    args = parser.parse_args()

    cur_from = args.cur_from.lower()
    cur_to = args.cur_to.lower()
    amount = args.amount

    currencies = fx_all_currencies()

    if currencies is None:
        print(
            "Unable to fetch currency list, please check your network commection and retry"
        )
        exit(1)

    elif cur_from not in currencies.keys():
        print(f"Invalid currency symbol {cur_from}.")
        exit(1)

    elif cur_to not in currencies.keys():
        print(f"Invalid currency symbol {cur_from}.")
        exit((1))

    else:
        print(
            f"{cur_from.upper()}\t{amount}\t{cur_to.upper()}\t{fx_conversion_rate(cur_from, cur_to)[cur_to] * amount:.2f}"
        )

    return 0


if __name__ == "__main__":
    main()
