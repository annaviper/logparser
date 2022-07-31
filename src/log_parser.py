import argparse
from funcs import list_hostnames


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", type=str, help="Path to the log file", required=True)
    parser.add_argument("-i", "--init", type=int, help="Initial datetime as UNIX timestamp", required=False)
    parser.add_argument("-e", "--end", type=int, help="End datetime as UNIX timestamp", required=False)
    parser.add_argument("-host", "--hostname", type=str, help="Target host name", required=True)
    parser.add_argument("-o", "--output", type=str, help="File path to save output", required=False)
    # I tried to make the tool accept datetime instead of UNIX from the CLI,
    # since in the instructions it mentions init_datetime and end_datetime, but ran out of time to
    # implement the acceptance of datetime arguments in the CLI.
    # datetime_format = '%Y-%m-%d %H:%M:%S'
    # parser.add_argument("-idt", "--init_dt", type=lambda s: datetime.datetime.strptime(s, datetime_format),
    #                     help=f"Init datetime in the format {datetime_format}", required=False),
    # parser.add_argument("-edt", "--end_dt", type=lambda s: datetime.datetime.strptime(s, datetime_format),
    #                     help=f"End datetime in the format {datetime_format}", required=False),
    args = parser.parse_args()
    return args


def log_parser():
    args = get_arguments()
    if args.output:
        list_hostnames(args.filepath, args.init, args.end, args.hostname, args.output)
    else:
        list_hostnames(args.filepath, args.init, args.end, args.hostname)


if __name__ == '__main__':
    log_parser()
