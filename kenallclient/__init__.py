def main() -> None:
    import argparse
    import dataclasses
    import os
    from pprint import pprint

    from kenallclient.client import KenAllClient

    parser = argparse.ArgumentParser()
    parser.add_argument("--apikey", default=os.environ.get("KENALL_APIKEY"))
    parser.add_argument("postalcode")
    args = parser.parse_args()
    client = KenAllClient(args.apikey)
    pprint(dataclasses.asdict(client.get(args.postalcode)))
