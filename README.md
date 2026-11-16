
# AWS API Gateway and Lambda Integration

## SOA Assignment

**Assignment:** Integrate API Gateway with AWS Lambda  
**Language:** Python  
**Cloud Platform:** Amazon Web Services (AWS)

## 1. Objective

To create an AWS Lambda function using Python to process student information and integrate it with Amazon API Gateway REST API.

## 2. AWS Services Used

- AWS Lambda
- Amazon API Gateway
- AWS IAM

## 3. Implementation

1. Created a Lambda function named `StudentInfoFunction`.
2. Selected Python as the runtime.
3. Implemented Python code to process student details in JSON format.
4. Created a REST API named `StudentManagementAPI`.
5. Created a resource named `/student`.
6. Configured a POST method with Lambda proxy integration.
7. Granted API Gateway permission to invoke Lambda.
8. Deployed the API to the `test` stage.
9. Tested the API using the API Gateway console.

## 4. Sample JSON Input

```json
{
  "StudentID": "2410080012",
  "Student_Name": "MELAGIRI NAGA VENKATESHWARA RAO",
  "Department": "AI & DS"
}
```

## 5. Expected Output

```json
{
  "message": "Student information processed successfully",
  "StudentID": "2410080012",
  "Student_Name": "MELAGIRI NAGA VENKATESHWARA RAO",
  "Department": "AI & DS"
}
```

## 6. Result

Successfully created and deployed an AWS Lambda function and integrated it with Amazon API Gateway. The POST request was tested successfully and returned HTTP status code 200.

## 7. Project Files

- `lambda_function.py` – Python AWS Lambda function.
- `README.md` – Project documentation.
