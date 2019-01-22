import s3
import yaml

with open('s3.yaml', 'r') as fi:
    config = yaml.load(fi)

connection = s3.S3Connection(**config['s3'])
storage = s3.Storage(connection)

for bucket in storage.bucket_list():
    print "\nBucket Name: ", bucket.name, " Create Data: ", bucket.creation_date, "\n"
    
    print "File List:"
    files_num = 0
    total_size = 0
    for key in storage.bucket_list_keys(bucket.name):
        files_num = files_num + 1
        print '\t', key.key, key.size, key.last_modified
        total_size = total_size + long(key.size)
    print "Number of files: ", files_num
    print "Total Size of Files: ", total_size, "(Byte)"
    print "--------------------------------------------------------------------------"
