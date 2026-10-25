// Declarative Jenkins pipeline for a Windows Jenkins agent
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'restaurant-website'   // [DOCKER_IMAGE_NAME]
    }

    stages {
        // Stage 1: get the latest code from GitHub (uses the repo set in the job)
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2: create a virtual environment and install packages
        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        // Stage 3: run the automated tests; the pipeline fails if a test fails
        stage('Run pytest') {
            steps {
                bat 'venv\\Scripts\\python -m pytest'
            }
        }

        // Stage 4: build the Docker image, tagged with the Jenkins build number
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully.' }
        failure { echo 'Pipeline failed. Check the console output.' }
    }
}