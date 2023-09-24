#CIL-Academy Project 
##Overview
I created a CloudFormation stack with a Yaml file template. The CFN template helped to automate the creation of an EC2 instance called 'CILEC2Ass' with an IAM role given for SSM and S3 access and an S3 bucket called 'Cilbucket'. I uploaded picture files into the S3 bucket through my management console, then connected via SSM to my EC2 instance and copied the picture files in the s3 bucket to a directory called 'backs3objects' in my EC2's home directory. Finally, I wrote a python script to automatically copy the contents of my s3 bucket to my directory on execution and a cron job to run the python script at 5 pm everyday.

##Amazon Elastic Cloud Compute (Amazon EC2)
Amazon EC2 is the building block of compute systems in Amazon Web Services (AWS). Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 reduces hardware costs so you can develop and deploy applications faster. In simple terms, EC2 allows you to handle complex workloads in the cloud without having to physically manage and provision data centres.  
![image](https://github.com/ChereeteeCodes/CIL_CFN_C6/assets/139123056/c0db5be9-9b8c-46b8-8cd2-52be8d7d4027)

##Amazon Simple Storage Service (Amazon S3)
Amazon S3 is a highly durable, available and scalable object storage service. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. 
![image](https://github.com/ChereeteeCodes/CIL_CFN_C6/assets/139123056/bce3aaf4-8b55-4c9f-9e58-0659593395ab)

##AWS Identity and Access Management (AWS IAM)
AWS IAM is a web service that helps you securely control access to your AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources. With IAM, you can also create roles that allows access to specific resources. IAM roles can be given to AWS resources to allow them access other resources, or other users in an organization.
![image](https://github.com/ChereeteeCodes/CIL_CFN_C6/assets/139123056/fd5662a4-b155-4305-94ee-0735a94e6223)

##Amazon CloudFormation 
AWS CloudFormation is a service that helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and CloudFormation takes care of provisioning and configuring those resources for you. You don't need to individually create and configure AWS resources and figure out what's dependent on what; CloudFormation handles that.
![image](https://github.com/ChereeteeCodes/CIL_CFN_C6/assets/139123056/fa63cae9-ea27-4204-813d-8af7452a2501)

##Session Manager
Sessions manager allowed me to connect to my EC2 instance without key-pairs. Here's a screenshot of the code I used to copy files from my s3 bucket to a directory in my EC2 instance: 
<img width="947" alt="Copys3objectscode" src="https://github.com/ChereeteeCodes/CIL_CFN_C6/assets/139123056/eb5ac8eb-52f1-4390-b309-21ee064b191b">

