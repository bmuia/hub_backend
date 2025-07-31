pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bmuia/hub_backend.git'
            }
        }

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

        stage('Install dependencies') {
            steps {
                sh '''
                    . myenv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Django') {
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
                deactivate || true
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
}
