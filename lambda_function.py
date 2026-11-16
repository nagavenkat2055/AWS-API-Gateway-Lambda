
import json

def lambda_handler(event, context):
    try:
        # Read student details from API Gateway request
        body = event.get("body", "{}")

        if isinstance(body, str):
            student_data = json.loads(body)
        else:
            student_data = body

        student_id = student_data.get("StudentID")
        student_name = student_data.get("Student_Name")
        department = student_data.get("Department")

        # Prepare response
        response = {
            "message": "Student information processed successfully",
            "StudentID": student_id,
            "Student_Name": student_name,
            "Department": department
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"error": str(e)})
        }
