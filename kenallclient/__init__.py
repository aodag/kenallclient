from .client import KenAllClient


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("apikey")
    parser.add_argument("postalcode")
    args = parser.parse_args()
    client = KenAllClient(args.apikey)
    print(client.get(args.postalcode))
