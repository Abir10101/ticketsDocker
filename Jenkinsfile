pipeline {
    agent any
    stages {
        stage('Build Database') { 
            steps {
                sh '''
                docker run --name db -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=myapp -p 127.0.0.1:3306:3306 -v $PWD/database/:/docker-entrypoint-initdb.d -d --rm mysql:8.0.31
                sleep 30s
                '''
            }
        }
        stage('Test Application') { 
            steps {
                sh '''
                python3 -m venv env && . ./env/bin/activate
                pip install -r requirements.txt
                export DB_HOST=127.0.0.1
                export DB_USER=root
                export DB_PASSWORD=admin
                export DB_NAME=myapp
                export SECRET_KEY="secret_key"
                python -m unittest Tests.test_auth
                python -m unittest Tests.test_app
                '''
            }
        }
    }
    post { 
        always {
            sh '''
            docker rm -f db
            '''
        }
    }
}
