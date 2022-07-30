import datetime
import pandas as pd
import time


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
    df = pd.read_csv(file_path, sep=" ", header=None)
    return df


def datetime_to_unix(dt: datetime):
    """Parse datetime to UNIX timestamp.

    Args:
      dt: datetime to convert to UNIX.

    Returns: UNIX timestamp.

    Raises:
        TypeError if date is not of datetime type.

    """
    if type(dt) != 'datetime':
        raise TypeError('Date should be of type datetime.')
    return time.mktime(dt.timetuple()) * 1000


def list_hostnames(file: str, init_datetime: datetime, end_datetime: datetime, hostname: str) -> list:
    """Return list of hostnames connected to a given host during a given period.

    Args:
      file(str): path to file.
      init_datetime(datetime): beginning date.
      end_datetime(datetime): end date.
      hostname(str): destination hostname.

    Returns:
      list: host names connected to destination hostname between the time period specified.

    Raises:

    """
    df = read_file(file)
    df.columns = ['unix_timestamp', 'hostname', 'hostname2']
    df = df.sort_values('unix_timestamp')
    init_unix, end_unix = datetime_to_unix(init_datetime, end_datetime)
    df = df.loc[(df["unix_timestamp"] >= init_unix) & (df["unix_timestamp"] <= end_unix)]
    df = df[df['hostname2'] == hostname]
    return df['hostname'].tolist()
