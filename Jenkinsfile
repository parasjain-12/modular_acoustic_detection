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
}
