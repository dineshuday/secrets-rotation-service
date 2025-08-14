# Secrets Rotation Service

A secure, API-driven microservice for storing, retrieving, and rotating secrets in AWS Secrets Manager, built with **FastAPI**, **Terraform**, and AWS infrastructure.  
Designed for internal teams to easily integrate secret management without directly handling credentials, improving security posture and reducing human error.

---

## 🚀 Features
- **Secure API Endpoints** for retrieving and rotating secrets
- **AWS Secrets Manager Integration** for encrypted storage
- **Automated Rotation** via AWS EventBridge
- **Infrastructure-as-Code** with Terraform
- **JWT Authentication** for API requests
- **Least Privilege IAM Policies**
- **CloudWatch Logging** for audit and compliance

---

## 🏗 Architecture
![Architecture Diagram](docs/architecture.png)

**Flow:**
1. Client authenticates via JWT and calls `/get-secret/{name}` or `/rotate-secret/{name}`.
2. API Gateway routes the request to a Lambda function (FastAPI app).
3. Lambda uses IAM Role with *least privilege* to access AWS Secrets Manager.
4. Secrets are retrieved or rotated, then returned securely to the client.
5. EventBridge triggers periodic secret rotation to enforce key hygiene.

---

## 📂 Project Structure
```plaintext
secrets-rotation-service/
│── src/
│   ├── main.py           # FastAPI app entry point
│   ├── secrets.py        # AWS Secrets Manager functions
│   ├── auth.py           # JWT authentication
│── infra/
│   ├── main.tf           # AWS provider, Lambda, Secrets Manager
│   ├── iam.tf            # IAM roles & policies
│   ├── variables.tf      # Config variables
│── requirements.txt      # Python dependencies
│── README.md
│── docs/
│   ├── architecture.png  # Architecture diagram


⸻

⚙ Deployment

1️⃣ Provision AWS Resources

cd infra
terraform init
terraform apply

2️⃣ Deploy FastAPI to Lambda

Use AWS SAM, Zappa, or Docker-based Lambda packaging.

Example (Zappa):

pip install zappa
zappa init
zappa deploy dev


⸻

🔐 Security Considerations
	•	No Secrets in Code: All secrets are stored in AWS Secrets Manager.
	•	Least Privilege: IAM roles only allow access to specific secrets.
	•	Encryption at Rest & In Transit: AWS KMS + HTTPS.
	•	JWT Auth: Ensures only authorized clients can call the API.
	•	Logging & Monitoring: CloudWatch for request tracing and auditing.
	•	Regular Rotation: Automated via EventBridge.

⸻

🧪 Example API Usage

Get Secret

curl -H "Authorization: Bearer <jwt_token>" \
     https://<api_gateway_url>/get-secret/api_key

Response:

{
  "secret": "some-secret-value"
}

Rotate Secret

curl -X POST -H "Authorization: Bearer <jwt_token>" \
     https://<api_gateway_url>/rotate-secret/api_key

Response:

{
  "status": "rotated",
  "new_secret": "new-random-value"
}


⸻

📜 License

MIT License

---