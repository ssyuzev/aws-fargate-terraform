1. Create ECR repository with name "app-repo" in AWS Console
2. Then build and push docker image to ECR. For example:
3. `aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/q7k9e1h5`
4. `docker build -t app-repo .`
5. `docker tag app-repo:latest 612659005028.dkr.ecr.us-east-1.amazonaws.com/app-repo:latest`
6. `docker push 612659005028.dkr.ecr.us-east-1.amazonaws.com/app-repo:latest`
7. Run: `terraform init`
8. Run: `terraform apply`
9. Goto URL from app_url's output 
10. Delete all created AWS resources: `terraform destroy`


How to check docker container:
`docker run -it -p 8000:80 demo:latest`