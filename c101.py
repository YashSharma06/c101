import dropbox

class TransferFiles:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")

        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "McfFQUW_RWwAAAAAAAAAAd0MW3V1zlnibGo96jPegh4MtIPlodRJBXpi_24uNRk9"
    transferfiles = TransferFiles(access_token)

    file_from = input("Enter the file path to transfer :-")
    file_to = input("Enter the file path where to tranfer :-")

    transferfiles.upload_file(file_from,file_to)
    print("File has been moved")

main()





