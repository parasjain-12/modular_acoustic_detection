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
                sh 'python binary_model.py'
            }
        }
        stage('Genrate Repor') {
            steps {
                sh 'pip install jenkinsapi'
                sh 'python genrate_report.py'
            }
        }
    }
}
