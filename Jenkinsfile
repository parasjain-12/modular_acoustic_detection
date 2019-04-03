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
         stage('Generate Report') {
            steps {
                sh 'python genrate_report.py'
            }
        }
    }
}
