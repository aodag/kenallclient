import argparse
import os


def make_parser() -> argparse.ArgumentParser:
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
    get_houjin_parser = subparsers.add_parser("get-houjin")
    get_houjin_parser.add_argument("houjinbangou")
    search_houjin_parser = subparsers.add_parser("search-houjin")
    search_houjin_parser.add_argument("query")
    search_houjin_parser.add_argument("--offset", type=int)
    search_houjin_parser.add_argument("--limit", type=int)
    search_houjin_parser.add_argument("--mode")
    search_houjin_parser.add_argument("--facet-area")
    search_houjin_parser.add_argument("--facet-kind")
    search_houjin_parser.add_argument("--facet-process")
    search_houjin_parser.add_argument("--facet-close-cause")

    return parser

    
def main() -> None:
    import dataclasses
    from pprint import pprint

    from kenallclient.client import KenAllClient
    parser = make_parser()
    args = parser.parse_args()
    client = KenAllClient(args.apikey, api_url=args.apiurl)
    if args.command == "get":
        pprint(dataclasses.asdict(client.get(args.postalcode)))
    elif args.command == "search":
        pprint(
            dataclasses.asdict(
                client.search(
                    q=args.query,
                    t=args.text,
                    facet=args.facet,
                    offset=args.offset,
                    limit=args.limit,
                ),
            ),
        )
    elif args.command == "get-houjin":
        pprint(dataclasses.asdict(client.get_houjin(args.houjinbangou)))
    elif args.command == "search-houjin":
        pprint(
            dataclasses.asdict(
                client.search_houjin(
                    args.query,
                    offset=args.offset,
                    limit=args.limit,
                    mode=args.mode,
                    facet_area=args.facet_area,
                    facet_kind=args.facet_kind,
                    facet_process=args.facet_process,
                    facet_close_cause=args.facet_close_cause,
                ),
            ),
        )
