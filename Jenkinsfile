pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'  # If you have dependencies
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'  # If you have tests
            }
        }

        stage('Run') {
            steps {
                sh 'python3 main.py'
            }
        }
    }
}
