#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Binary Model') {
            steps {
                sh 'python multilabel_model.py'
            }
        }
        stage('Genrate Repor') {
            steps {
                sh 'python genrate_report.py'
            }
        }
    }
}
