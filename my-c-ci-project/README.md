# My C CI Project

This is a simple C calculator project with CI/CD pipeline using Jenkins and Pytest.

## Structure

my-c-ci-project/
├── src/
│   └── main.c
├── build.sh                # Builds the code
├── run.sh                  # Runs binary with test input
├── test/
│   ├── test_automation.py  # Pytest script
│   └── test_input.txt
├── Jenkinsfile             # Jenkins pipeline
└── README.md

## Usage

- Run `bash build.sh` to build the calculator.
- Run `bash run.sh` to execute the calculator with test input.

## Jenkins Pipeline

The Jenkinsfile defines the following stage:
1. **Build**: Compiles the C code.
