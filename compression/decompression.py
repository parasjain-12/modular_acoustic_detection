"""
Decompresses back the compressed audio file format into wav file format
"""
import subprocess
import os
import glob
import argparse

# parsing the inputs given
DESCRIPTION = 'Input the path of the compressed audio files \
              and path to write the decompressed audio files'
HELP = 'Decompresses back to wav format'
PARSER = argparse.ArgumentParser(description=DESCRIPTION)
PARSER.add_argument('-path_to_compressed_audio_files', '--path_to_compressed_audio_files',
                    action='store', help='Input the path')
PARSER.add_argument('-path_to_decompressed_audio_files', '--path_to_decompressed_audio_files',
                    action='store', help='Input the path')
PARSER.add_argument('-codec_type', '--codec_type',
                    action='store', help='Input the format of compresses files')
RESULT = PARSER.parse_args()

#give the path where the compressed files are stored
COMPRESSED_FILES_PATH = RESULT.path_to_compressed_audio_files
#give the path to write the decompressed files
DECOMPRESSED_FILES_PATH = RESULT.path_to_decompressed_audio_files
TYPE_OF_COMPRESSION = RESULT.codec_type

# Read the balanced data and the get the wav files list
# which are to be compressed and decompressed into list
COMPRESSED_FILES_LIST = glob.glob(COMPRESSED_FILES_PATH+'*.'+TYPE_OF_COMPRESSION)

# create seperte directories if not present to store compressed and decompressed files
if not os.path.exists(DECOMPRESSED_FILES_PATH):
    os.makedirs(DECOMPRESSED_FILES_PATH)

# decompressing opus files back into wav format
for COMPRESSED_FILE in COMPRESSED_FILES_LIST:
    if os.path.exists(DECOMPRESSED_FILES_PATH+(COMPRESSED_FILE.split('/')[-1])[:-4]+'wav'):
        print COMPRESSED_FILE.split('/')[-1] + 'has already been decompressed'
    else:
        try:
            subprocess.call('ffmpeg -i ' + COMPRESSED_FILE + ' '+
                            DECOMPRESSED_FILES_PATH+ (COMPRESSED_FILE.split('/')[-1])[:-4]+'wav',
                            shell=True)
            print 'De-compression : ' + COMPRESSED_FILE.split('/')[-1] + ' is done..'
        except ValueError:
            print 'Warning : Skipped ' + COMPRESSED_FILE + " as file format is wrong "

print 'De-Compressing the opus files into wav files is Completed..!!'
