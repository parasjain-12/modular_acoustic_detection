#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install jenkinsapi'
                sh 'python --version'
            }
        }
        stage('Multilabel Model And storing it into ') {
            steps {
                sh 'python multilabel_model.py'
            }
        }
         stage('Read 2 Report') {
            steps {
                sh 'python read_report.py'
            }
        }
    }
post {
        always {
            echo 'Build Started...!'
           /* archiveArtifacts artifacts: '/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output.txt', onlyIfSuccessful: true */
        }
        success {
            echo 'Succeeeded...!'
            slackSend (color: '#00FF00', message: "SUCCESSFUL...! Job ")
            slackSend(echo "current build number: ${currentBuild.number}")
        }
    }
}
