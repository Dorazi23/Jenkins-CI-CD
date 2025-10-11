pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Test') {
            steps {
                // For Linux/macOS based containers, use 'sh'. For Windows, use 'bat'.
                sh 'python -m unittest discover'
            }
        }
    }
}