from google_drive_downloader import GoogleDriveDownloader as gdd
import zipfile
gdd.download_file_from_google_drive(file_id='1r0vlG_Pb9Tu-OwJTqmPIL_d_5KyWx-qk',
                                    dest_path='./YoloWeights/yolo.zip',
                                    unzip=False)

with zipfile.ZipFile('YoloWeights/yolo.zip', 'r') as zip_ref:
    zip_ref.extractall('YoloWeights/')
