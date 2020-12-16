from google_drive_downloader import GoogleDriveDownloader as gdd
import zipfile
gdd.download_file_from_google_drive(file_id='10OvDsL0rND5Z_VPkYpiP4fRF36G0rv7i',
                                    dest_path='./Tesseract/tesseract.zip',
                                    unzip=False)

with zipfile.ZipFile('Tesseract/tesseract.zip', 'r') as zip_ref:
    zip_ref.extractall('Tesseract/')
