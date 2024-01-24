from ftplib import FTP
from datetime import datetime, timedelta, date
import gzip
from pathlib import Path

def calculate_gps_week_number(observation_datetime):
    epoch = date(1980, 1, 6)
    observation_date = observation_datetime.date()
    epochMonday = epoch - timedelta(epoch.weekday())
    observationMonday = observation_date - timedelta(observation_date.weekday())
    noWeeks = int((observationMonday - epochMonday).days / 7) - 1
    return noWeeks

def download_igs_product(product_type, observation_datetime, igs_data_center, save_path="."):
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

    # Construct file names
    sp3_file = f"IGS0OPSRAP_{date_str}0000_01D_15M_ORB.SP3.gz"
    clk_file = f"IGS0OPSRAP_{date_str}0000_01D_05M_CLK.CLK.gz"

    # Get FTP server details for the specified IGS data center
    ftp_server = igs_ftp_servers.get(igs_data_center)
    if not ftp_server:
        raise ValueError(f"Invalid IGS data center: {igs_data_center}")

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
    local_file_path = Path(save_path) / file_name

    with open(local_file_path, "wb") as file:
        ftp.cwd(directory)
        ftp.retrbinary(f"RETR {file_name}", file.write)
    print(f"Downloaded {file_name}")

    # Check if the file has a .gz extension
    if file_name.endswith(".gz"):
        # Decompress the file
        decompressed_file_path = local_file_path.with_suffix("")
        with gzip.open(local_file_path, "rb") as f_in, open(decompressed_file_path, "wb") as f_out:
            f_out.write(f_in.read())
        print(f"Decompressed {file_name}")


# Example usage:
product_type = "RAP"
observation_datetime = datetime(2024, 1, 22)  # Replace with your desired datetime
igs_data_center = "IGN"  # Replace with your desired IGS data center

download_igs_product(product_type, observation_datetime, igs_data_center)
