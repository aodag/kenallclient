def main() -> None:
    import argparse
    import dataclasses
    import os
    from pprint import pprint

    from kenallclient.client import KenAllClient

    parser = argparse.ArgumentParser()
    parser.add_argument("--apikey", default=os.environ.get("KENALL_APIKEY"))
    parser.add_argument("--apiurl", default=os.environ.get("KENALL_APIURL"))
    subparsers = parser.add_subparsers(dest="command")
    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("postalcode")
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("--query", "-q")
    search_parser.add_argument("--text", "-t")
    search_parser.add_argument("--offset", type=int)
    search_parser.add_argument("--limit", type=int)
    search_parser.add_argument("--facet")
    args = parser.parse_args()
    client = KenAllClient(args.apikey, api_url=args.apiurl)
    if args.command == "get":
        pprint(dataclasses.asdict(client.get(args.postalcode)))
    elif args.command == "search":
        pprint(dataclasses.asdict(client.search(q=args.query, t=args.text, facet=args.facet, offset=args.offset, limit=args.limit)))
