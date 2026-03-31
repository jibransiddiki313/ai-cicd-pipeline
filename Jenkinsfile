pipeline {
    agent any
    
    environment {
        ANTHROPIC_API_KEY = credentials('anthropic-api-key')
    }
    
    stages {
        stage('Code') {
            steps {
                echo "Cloning repository"
                git url: 'https://github.com/jibransiddiki313/ai-cicd-pipeline.git', branch: 'main'
            }
        }
        stage('AI Code Review') {
            steps {
                echo "Running AI Code Review..."
                sh '''
            sudo apt-get install -y python3-pip python3-requests 2>/dev/null || true
            python3 ai_review.py app.py
          '''
            }
        }
        stage('Build') {
            steps {
                echo "Building Docker image"
                sh 'docker build -t ai-cicd-pipeline .'
            }
        }
        stage('Test') {
            steps {
                echo "Testing application"
                sh 'docker run --rm ai-cicd-pipeline python -c "import flask; print(\"Flask OK\")"'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to production"
                sh 'docker-compose down && docker-compose up -d'
            }
        }
    }
}
