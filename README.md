# Auto Tag S3 Bucket on Creation

## Overview
Automatically tags every new S3 bucket with Owner = devops student
using AWS CloudTrail, EventBridge, and Lambda.

## Architecture
User → S3 Bucket → CloudTrail → EventBridge → Lambda → Tag Applied

## Steps
1. Create CloudTrail Trail
2. Create EventBridge Rule
3. Create Lambda Function
4. Add IAM Permissions
5. Test by creating a new S3 bucket

## Result
Every new S3 bucket gets tagged with:
- Key: Owner
- Value: devops student
