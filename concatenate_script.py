import os
import struct

def concatenate_bin_files(folder_path, output_file):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.bin')]
    
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
