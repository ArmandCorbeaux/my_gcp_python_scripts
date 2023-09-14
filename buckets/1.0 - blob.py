    """ For Google Cloud Platform,

        There are simple examples to check if files or folders exist or not in a bucket
        
        Date : 2023-09-12
        Author : Armand CORBEAUX
        Mail : armand.corbeaux@gmail.com
    """

from google.cloud import storage # used to interact with the bucket

# This is where you declarate your various names
# You have just to cut and paste the informations from the bucket page
BUCKET_NAME = "change_me_to_your_bucket_name" # this is the targetted bucket
PATH_NAME = "change_me_to_your_path_name" # this is the targetted path in your bucket
FILE_NAME = "change_me_to_your_file_name" # this is the targetted filename

storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

def it_is_just_a_simple_function_test(blob, TARGET):
    """ This is a function to show the blob result

    Args:
        blob (_type_): the name of the blob
        More informations at this link :
        https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob
        
        TARGET (_type_): this is the type of the target
    """
    print("You try to see if this target exists:")
    print(blob.name+"\n")

    if blob.exists():
        print(f"Yes - the '{TARGET}' exists in the bucket.\n")
        return
    else:
        print(f"No - the '{TARGET}' doesn't exist in the bucket.\n")
        return

def show_me_the_results():
    """ It return you the result :
            - for a path to a folder
            - for a path to a filename
    """    
    blob = bucket.blob(PATH_NAME + "/")
    it_is_just_a_test(blob,PATH_NAME)

    blob = bucket.blob(PATH_NAME + "/" + FILE_NAME)
    it_is_just_a_test(blob,FILE_NAME)    

if __name__ == "__main__" :
    show_me_the_results()
