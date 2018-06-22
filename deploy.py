import boto3, os, mimetypes as mime


def upload_files(path):
	bucket_name = "webworks.ninja"
	session = boto3.Session(profile_name='aakash')
	
	s3 = session.client('s3')
	print("s3 client initialised.")
 
	for subdir, dirs, files in os.walk(path):
		for file in files:
			full_path = os.path.join(subdir, file)
			mime_type = mime.guess_type(full_path)
			
			print("Uploading {} ".format(full_path[len(path):]))
			s3.upload_file(
				full_path,
				bucket_name,
				full_path[len(path):],
				ExtraArgs={'ACL':'public-read', 'ContentType': mime_type[0] or 'binary/octet'})

 
upload_files("./")