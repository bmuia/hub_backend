pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                echo 'Starting Django CI/CD Pipeline...'
                sh '''
                    python -m venv myenv
                    . myenv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bmuia/hub_backend.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    . myenv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run FastAPI') {
            steps {
                sh '''
                    . myenv/bin/activate
                    python manage.py runserver 0.0.0:8000 &
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh '''
                . myenv/bin/activate
                deactivate
                rm -rf myenv
            '''
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }