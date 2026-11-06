pipeline {
    agent any

    triggers { githubPush() }   // GitHub webhook trigger

    environment {
        APP_DIR  = '/home/ubuntu/apps/flask-backend'
        APP_NAME = 'flask-backend'
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install & Test (CI)') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/pytest -v
                '''
            }
        }

        stage('Deploy (CD)') {
            steps {
                // pm2 'ubuntu' user ke under chal raha hai, isliye sudo -u ubuntu
                sh '''
                    sudo -u ubuntu -H bash -c "
                      cd ${APP_DIR} &&
                      git pull origin main &&
                      venv/bin/pip install -r requirements.txt &&
                      pm2 restart ${APP_NAME} &&
                      pm2 save
                    "
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 3 && curl -f http://localhost:5000/api/health'
            }
        }
    }

    post {
        success { echo 'Flask deployment SUCCESS' }
        failure { echo 'Flask deployment FAILED' }
    }
}
