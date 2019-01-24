import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print("\n[Bucket Name]:", bucket["Name"], "[Create Data]:", bucket["CreationDate"], "\n")

    files_num = 0
    total_size = 0
    print("File List:")
    resp = s3.list_objects_v2(Bucket=bucket["Name"])
    for obj in resp['Contents']:
        files_num += 1
        total_size = total_size + int(obj["Size"])
        print(obj["Key"], obj["Size"], obj["LastModified"])
    print("\nNumber of files: ", files_num)
    print("Total Size of Files: ", total_size, "(Byte)")
    print("--------------------------------------------------------------------------")

