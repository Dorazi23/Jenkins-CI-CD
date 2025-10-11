pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Test') {
            steps {
                // For Windows, use 'bat'. For Linux/macOS, use 'sh'.
                bat 'python -m unittest discover'
            }
        }
    }
}