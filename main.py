import os
import argparse

from pydub import AudioSegment
import send2trash
from mutagen.easyid3 import EasyID3
from mutagen.asf import ASF


def get_args():
    parser = argparse.ArgumentParser(description='Convert your wma files to mp3 with ID3 tags.')
    parser.add_argument('input_path', type=str, default='.',
                        help='path to the music folder')
    parser.add_argument('output_path', nargs='?', type=str, default=None,
                        help='path to the output folder')
    parser.add_argument('-d', '--delete', action='store_true',
                        help='delete the wma files after conversion')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    # path to the music folder
    path = args.input_path

    # Tag name conversion list if general conversion is not enough
    tag_convert_list = {
        'albumtitle': 'album',
        'author': 'artist',
        'year': 'date',
        'track': 'tracknumber',
    }

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.wma'):
                wma_file = os.path.join(root, file)
                if args.output_path is not None:
                    final_output_path = os.path.join(args.output_path, os.path.relpath(root, path))
                    if not os.path.exists(final_output_path):
                        os.makedirs(final_output_path)
                    mp3_file = os.path.join(final_output_path, os.path.splitext(file)[0] + '.mp3')
                else:
                    mp3_file = os.path.splitext(wma_file)[0] + '.mp3'
                try:
                    if os.path.exists(mp3_file):
                        print('Skipped: ' + wma_file)
                        continue
                    # Convert wma to mp3
                    AudioSegment.from_file(wma_file).export(mp3_file, format='mp3', bitrate='128k')
                    # Transfer tags from the wma file to the mp3 file
                    wma_tags = ASF(wma_file).tags.as_dict()
                    mp3_tags = EasyID3(mp3_file)
                    for k, v in wma_tags.items():
                        # Adjust the tag name
                        if k.startswith('WM/'):
                            tag_name = k[3:]
                        else:
                            tag_name = k
                        tag_name = tag_name.lower()
                        if tag_name in tag_convert_list.keys():
                            tag_name = tag_convert_list[tag_name]
                        # Set the tag value
                        if v is not None:
                            if tag_name in EasyID3.valid_keys.keys():
                                mp3_tags[tag_name] = str(v[0])
                    mp3_tags.save()
                    print('Converted: ' + wma_file)
                    # Remove the wma file to recycle bin
                    if args.delete:
                        send2trash.send2trash(wma_file)
                        print('Removed: ' + wma_file)
                except IOError as e:
                    print('Error: ' + e.strerror)
    print('\nDone!')
