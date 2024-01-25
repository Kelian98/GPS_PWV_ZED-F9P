"""
Script Name: download_igs_data.py
Author: Kélian SOMMER
Description: This script downloads IGS (International GNSS Service) products (SP3 and CLK files) from the specified IGS data center.
It supports different product types (ultra-rapid, rapid, final) and allows the user to specify the observation date, IGS data center, save path, and display option.
The downloaded files are saved in the specified path, and additional information about the download can be displayed if requested.
Reference : https://igs.org/products/
"""

from ftplib import FTP
from datetime import datetime, timedelta, date
import gzip
import os
import argparse
from utilities import *

def calculate_gps_week_number(observation_datetime):
    """
    Calculate the GPS week number for a given observation datetime.

    Parameters:
        - observation_datetime (datetime): The datetime of the observation.

    Returns:
        int: The GPS week number.

    The GPS week number is calculated based on the given observation datetime.
    The GPS week system started on January 6, 1980.

    Example:
        >>> from datetime import datetime
        >>> calculate_gps_week_number(datetime(2024, 1, 24))
        2135
    """
    epoch = date(1980, 1, 6)
    observation_date = observation_datetime.date()
    epochMonday = epoch - timedelta(epoch.weekday())
    observationMonday = observation_date - timedelta(observation_date.weekday())
    noWeeks = int((observationMonday - epochMonday).days / 7) - 1
    return noWeeks


def download_igs_product(product_type, observation_datetime, igs_data_center, save_path=".", display=True):
    """
    Download IGS products (SP3 and CLK files) from the specified IGS data center.

    Parameters:
        - product_type (str): Type of IGS product ("RAP" or "FIN").
        - observation_datetime (datetime): The datetime of the observation.
        - igs_data_center (str): IGS data center code (e.g., "CDDIS", "IGN", "BKG").
        - save_path (str): Path to save the downloaded files (default is current directory).
        - display (bool): Whether to display information about the download (default is True).

    Returns:
        None

    This function connects to the FTP server of the specified IGS data center, downloads the required SP3
    and CLK files for a given product type and observation datetime, and saves them to the specified path.

    Example:
        >>> from datetime import datetime
        >>> download_igs_product("RAP", datetime(2024, 1, 24), "CDDIS")
    """

    # Map IGS data centers to their respective FTP server details
    igs_ftp_servers = {
        "CDDIS": {"host": "cddis.nasa.gov", "directory": "/archive/gnss/products/"},
        "IGN": {"host": "igs.ign.fr", "directory": "/pub/igs/products/"},
        "BKG": {"host": "ftp.igs-ftp.bkg.bund.de", "directory": "/IGS/products/"},
        "ESA": {"host": "ftp.gssc.esa.int", "directory": "/cddis/gnss/products/"},
        "KASI": {"host": "nfs.kasi.re.kr", "directory": "/gps/products/"},
        "SOPAC": {"host": "garner.ucsd.edu", "directory": "/pub/products/"},
        "Wuhan University": {"host": "igs.gnsswhu.cn", "directory": "/pub/gps/products/"}
    }

    # Convert datetime to the format used in the IGS file names
    date_str = observation_datetime.strftime("%Y%j")

    # Calculate GPS week number for the given observation datetime
    gps_week_number = calculate_gps_week_number(observation_datetime)

    print(product_type)

    # Construct file names
    if product_type == "RAP":
        sp3_file = f"IGS0OPS{product_type}_{date_str}0000_01D_15M_ORB.SP3.gz"
        clk_file = f"IGS0OPS{product_type}_{date_str}0000_01D_05M_CLK.CLK.gz"
    elif product_type == "FIN":
        sp3_file = f"IGS0OPS{product_type}_{date_str}0000_01D_15M_ORB.SP3.gz"
        clk_file = f"IGS0OPS{product_type}_{date_str}0000_01D_30S_CLK.CLK.gz"
    elif product_type == "FIN":
        print(f"{RED}No CLK file for ultra-rapid product type, skipping...{RESET_COLOR}")
        return 1

    if display:
        print(f"{CYAN}Observation date = {date_str}{RESET_COLOR}")
        print(f"{CYAN}GPNSS Week Number = {gps_week_number}{RESET_COLOR}")
        print(f"{CYAN}Queried SP3 file = {sp3_file}{RESET_COLOR}")
        print(f"{CYAN}Queried CLK file = {clk_file}{RESET_COLOR}")

    # Get FTP server details for the specified IGS data center
    ftp_server = igs_ftp_servers.get(igs_data_center)
    if not ftp_server:
        raise ValueError(f"{RED}Invalid IGS data center: {igs_data_center}{RESET_COLOR}")

    # Connect to the IGS FTP server
    with FTP(ftp_server["host"]) as ftp:
        ftp.login()
        ftp.set_pasv(True)

        directory = f"{ftp_server['directory']}{gps_week_number}"

        # Download SP3 file
        download_file(ftp, directory, sp3_file, save_path)

        # Download CLK file
        download_file(ftp, directory, clk_file, save_path)


def download_file(ftp, directory, file_name, save_path):
    """
    Download a file from the specified FTP directory and optionally decompress it if it has a '.gz' extension.

    Parameters:
        - ftp (FTP): The FTP connection.
        - directory (str): The remote directory on the FTP server.
        - file_name (str): The name of the file to download.
        - save_path (str): Path to save the downloaded file.

    Returns:
        None

    This function checks if the specified file exists in the FTP directory, downloads it using the RETR command,
    and saves it to the specified local path. If the file has a '.gz' extension, it also decompresses the file.

    Example:
        >>> from ftplib import FTP
        >>> ftp = FTP('ftp.example.com')
        >>> ftp.login('username', 'password')
        >>> download_file(ftp, '/remote/directory', 'example.txt.gz', '/local/directory')
    """

    local_file_path = os.path.join(save_path, file_name)

    # Check if the file exists in the FTP directory
    try:
        ftp.cwd(directory)
        file_list = ftp.nlst()
        if file_name in file_list:
            # If the file exists, retrieve it using RETR command
            with open(local_file_path, 'wb') as file:
                ftp.retrbinary(f"RETR {file_name}", file.write)
            print(f"{GREEN}Downloaded {file_name}{RESET_COLOR}")
            downloaded = True
        else:
            print(f"{RED}File {file_name} does not exist in the FTP directory.{RESET_COLOR}")
            downloaded = False
    except Exception as e:
        print(f"{RED}Error occurred while downloading remote file {file_name}: {e}{RESET_COLOR}")
        return 1

    if downloaded:
        # Check if the file has a .gz extension
        if file_name.endswith(".gz"):
            # Decompress the file
            # Using os.path.splitext to remove the file extension
            decompressed_file_path = os.path.splitext(local_file_path)[0]
            with gzip.open(local_file_path, "rb") as f_in, open(decompressed_file_path, "wb") as f_out:
                f_out.write(f_in.read())
            print(f"{GREEN}Decompressed {file_name}{RESET_COLOR}")
    else:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download IGS products from an FTP server.")
    parser.add_argument("--product-type", choices=["ultra-rapid", "rapid", "final"], default="rapid",
                        help="Type of IGS product (ultra-rapid, rapid, or final). Default is rapid.")
    parser.add_argument("--observation-date", type=lambda s: datetime.strptime(s, "%Y-%m-%d"), required=True,
                        help="Observation date in the format YYYY-MM-DD.")
    parser.add_argument("--data-center", choices=["CDDIS", "IGN", "BKG", "ESA", "KASI", "SOPAC", "Wuhan University"],
                        default="IGN", help="IGS data center code. Default is IGN.")
    parser.add_argument("--save-path", default=os.path.join(os.path.dirname(os.getcwd()), "data/"),
                        help="Path to save the downloaded files. Default is the 'data' directory.")
    parser.add_argument("--display", action="store_false", help="Display information about the download.")

    args = parser.parse_args()

    product_types = {"ultra-rapid": "ULT", "rapid": "RAP", "final": "FIN"}
    product_type = product_types[args.product_type]

    download_igs_product(
        product_type=product_type,
        observation_datetime=args.observation_date,
        igs_data_center=args.data_center,
        save_path=args.save_path,
        display=args.display
    )

    # Example
    # python download_igs_data.py --product-type rapid --observation-date 2024-01-22 --data-center IGN --save-path /path/to/save --display