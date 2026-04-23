# ai-cicd-pipeline
# AI-Powered CI/CD Pipeline 🤖🚀

## Overview
A complete end-to-end CI/CD pipeline that uses **Claude AI API** to automatically 
review code quality before every deployment. Built from scratch using Jenkins, 
Docker, and AWS EC2.

## Live App
http://54.164.125.87:5000/

## How It Works
Every time code is pushed to GitHub, the pipeline automatically:
1. Clones latest code from GitHub
2. Runs AI-powered code review using Claude API
3. Builds Docker image
4. Tests the application
5. Deploys to AWS EC2

## Architecture
```
GitHub Push → Webhook → Jenkins → AI Review → Docker Build → Test → Deploy → AWS EC2
```

## Pipeline Stages
| Stage | Description |
|-------|-------------|
| Code | Clones latest code from GitHub |
| AI Code Review | Claude AI reviews code for bugs & security issues |
| Build | Builds Docker image from Dockerfile |
| Test | Runs application inside container |
| Deploy | Docker Compose deploys to production |

## Tech Stack
- **Application:** Python Flask
- **AI Integration:** Claude AI API (Anthropic)
- **CI/CD:** Jenkins Declarative Pipeline
- **Containerization:** Docker, Docker Compose
- **Cloud:** AWS EC2 (Ubuntu 22.04)
- **Version Control:** GitHub + Webhooks

## Project Structure
```
ai-cicd-pipeline/
├── app.py              # Flask application
├── ai_review.py        # Claude AI code review script
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
├── docker-compose.yml  # Service configuration
└── Jenkinsfile         # CI/CD pipeline definition
```

## What I Learned
- Jenkins Declarative Pipeline with 5 stages
- Integrating AI API into DevOps pipeline
- Docker containerization of Python Flask app
- GitHub Webhook auto-trigger setup
- AWS EC2 disk space management (EBS resize)
- Debugging real-world DevOps issues

## Real Challenges Solved
- Fixed Jenkins 403 webhook error
- Resolved EC2 disk space (expanded EBS 7.6GB → 11GB)
- Fixed Python pip installation in Jenkins pipeline
- Debugged Docker quotes syntax issues in Jenkinsfile

## How to Run Locally
1. Clone this repo
2. Add your Anthropic API key in Jenkins credentials
3. Setup Jenkins Pipeline from SCM
4. Push code — pipeline runs automatically!

## Author
**Jibran Siddiki** — DevOps Engineer  
GitHub: github.com/jibransiddiki313  
LinkedIn: linkedin.com/in/jibran-siddiki-411733230
