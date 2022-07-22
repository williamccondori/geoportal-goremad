from fastapi import UploadFile, File

from shared.exceptions.zip_exception import NotZipException, ZipTooBigException


async def get_zip_file_upload(file: UploadFile = File(...)):
    zip_extensions = ['application/zip', 'application/x-zip-compressed', 'application/x-zip']
    if file.content_type not in zip_extensions:
        raise NotZipException()
    contents = await file.read()
    if len(contents) > 20 * 1024 * 1024:
        raise ZipTooBigException()
    await file.close()
    return contents
