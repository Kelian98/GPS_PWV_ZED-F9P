import os
import struct
import glob

def concatenate_bin_files(folder_path, output_file):
    file_list = glob.glob(os.path.join(folder_path, '2024*.bin'))
    # Important to sort in order to generate the RINEX file later
    file_list = sorted(file_list) 
    
    with open(output_file, 'wb') as outfile:
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            
            with open(file_path, 'rb') as infile:
                data = infile.read()
                outfile.write(data)

    print(f'Concatenation complete. Result saved to {output_file}')

# Example usage:
folder_path = '/home/sommer/Documents/PWV/TEST_CONVERSION'
output_file = os.path.join(folder_path, "concatenated.bin")

concatenate_bin_files(folder_path, output_file)
