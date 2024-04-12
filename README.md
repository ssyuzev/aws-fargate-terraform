1. Create ECR repository with name "app-repo" in AWS Console
2. Then build and push docker image to ECR. (check ECR recommendation)  
3. Run: `terraform init`
4. Run: `terraform apply`
5. Goto URL from app_url's output 
6. Delete all created AWS resources: `terraform destroy`


How to check docker container locally run:
`docker run -it -p 8000:80 demo:latest`