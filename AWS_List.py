# For this project I will be starting with an empty list

aws_list =[]
print(aws_list)

# Append (input) items on list

aws_list =[]

aws_list.append ('S3')
aws_list.append ('Lambda')
aws_list.append ('DynamoDB')
aws_list.append ('EC2')
aws_list.append ('Cloudfront')
aws_list.append ('Cloud9')


#Now I will print the length of the list
print(len(aws_list))


#Now I will remove two services from the list

aws_list.remove ('Cloud9')
aws_list.remove ("Cloudfront")


#Next we will print the new length of the list

print(aws_list)
print(len(aws_list))

 