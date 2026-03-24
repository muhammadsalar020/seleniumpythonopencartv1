pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/muhammadsalar020/seleniumpythonopencartv1.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest -v -s --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                export PATH=$PATH:/opt/homebrew/bin
                allure generate allure-results -o allure-report --clean
                '''
            }
        }
    }

    post {
        success {
            echo "Build Successful 🎉"

            // Optional auto open
            sh '''
            bash ~/open_allure.sh &
            '''
        }

        failure {
            echo "Build Failed ❌"
        }
    }
}