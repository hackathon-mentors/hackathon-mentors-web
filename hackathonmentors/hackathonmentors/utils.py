from google.cloud import storage


class GCPHelper():
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket("hm-store")

    def upload_blob(self, source, dest):
        """
        Uploads given file to the bucket.

        Params:
            - source (str) file to upload, i.e. "local/path/to/file"
            - dest (str) the destination file name, i.e. "storage-object-name"

        Reference:
            https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python

        """
        blob = self.bucket.blob(dest)
        return blob.upload_from_filename(source)

