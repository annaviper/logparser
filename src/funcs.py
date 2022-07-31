import datetime
import pandas as pd


def read_file(file_path: str) -> pd.DataFrame:
    """Read file content.

    Args:
      file_path(str): path to file.

    Returns:
        contents of the file with the following column names:
        'unix_timestamp', 'hostname', 'hostname2'.

    Raises:
        TypeError if file_path is not a string.
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path argument must be a string")
    df = pd.read_csv(file_path, sep=" ", header=None, names=['unix_timestamp', 'hostname', 'hostname2']
                     )
    return df.sort_values('unix_timestamp')


def datetime_to_unix(dt):
    """Parse datetime to UNIX timestamp in milliseconds.

    Args:
      dt: datetime to convert to UNIX.

    Returns: UNIX timestamp.

    Raises:
        TypeError if date is not of datetime type.

    """
    if not isinstance(dt, datetime.datetime):
        raise TypeError('Date should be of type datetime.')
    return dt.timestamp() * 1000


def list_hostnames(file: str, init_datetime, end_datetime, hostname: str, output_path: str = None) -> list:
    """Return list of hostnames connected to a given host during a given period.

    Args:
      file(str): path to file.
      init_datetime(datetime or UNIX): beginning date.
      end_datetime(datetime or UNIX): end date.
      hostname(str): destination hostname.
      output_path(str): where to write output.

    Returns:
      list: host names connected to destination hostname between the time period specified.

    Raises:
        TypeError if dates are not unixtimestamp or datetime.datetime.
    """
    df = read_file(file)

    # handle time periods. I tried to make the tool accept datetime instead of UNIX from the CLI,
    # since in the instructions it mentions init_datetime and end_datetime, but ran out of time to
    # implement the acceptance of datetime arguments in the CLI.
    if isinstance(init_datetime, datetime.datetime) & isinstance(init_datetime, datetime.datetime):
        init_datetime = datetime_to_unix(init_datetime)
        end_datetime = datetime_to_unix(end_datetime)
    elif not (isinstance(init_datetime, int) & isinstance(init_datetime, int)):
        raise TypeError("Date arguments (-i, -e) should be UNIX timestamp or datetime types.")

    df = df.loc[(df["unix_timestamp"] >= init_datetime) & (df["unix_timestamp"] <= end_datetime)]

    # filter by hostname
    df = df[df['hostname2'] == hostname]

    # output
    hostnames_list = df['hostname'].tolist()
    if output_path:
        df.to_csv(output_path, header=None, index=None, sep=' ')
        print(f"Output saved to {output_path}")

    print(f"Hosts connections to {hostname}: {hostnames_list}")
    return hostnames_list
