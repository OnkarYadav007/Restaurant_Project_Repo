// Declarative Jenkins pipeline (runs on a Linux Jenkins agent with Python 3 and Docker installed)
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'restaurant-website'   // [DOCKER_IMAGE_NAME]
    }

    stages {
        // Stage 1: download the latest code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/OnkarYadav007/Restaurant_Project_Repo.git'
            }
        }

        // Stage 2: create a virtual environment and install packages
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        // Stage 3: run the automated tests; the pipeline fails if a test fails
        stage('Run pytest') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }

        // Stage 4: build the Docker image (tagged with the Jenkins build number)
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully.' }
        failure { echo 'Pipeline failed. Check the console output.' }
    }
}
