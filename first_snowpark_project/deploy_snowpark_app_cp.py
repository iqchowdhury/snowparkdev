import os
import sys
import subprocess

def run(cmd: str):
    """Run a shell command and stream output live."""
    print(f"\n>>> Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)

def validate_env_vars():
    """Ensure all required Snowflake environment variables are present."""
    required_vars = [
        "SNOWFLAKE_ACCOUNT",
        "SNOWFLAKE_USER",
        "SNOWFLAKE_PASSWORD",
        "SNOWFLAKE_ROLE",
        "SNOWFLAKE_WAREHOUSE",
        "SNOWFLAKE_DATABASE"
    ]

    missing = [v for v in required_vars if not os.getenv(v)]
    if missing:
        print(f"Missing required environment variables: {missing}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python deploy_snowpark_app.py first_snowpark_project/")
        sys.exit(1)

    directory_path = sys.argv[1]
    print(f"Directory path: {directory_path}")

    validate_env_vars()

    # Change into the Snowpark project directory
    os.chdir(directory_path)

    # Step 1: Build Snowpark artifact (creates app.zip)
    run("snow snowpark build")

    # Step 2: Deploy using temporary connection (no config.toml needed)
    deploy_cmd = (
        "snow snowpark deploy "
        "--replace "
        "--temporary-connection "
        f"--account {os.getenv('SNOWFLAKE_ACCOUNT')} "
        f"--user {os.getenv('SNOWFLAKE_USER')} "
        f"--password {os.getenv('SNOWFLAKE_PASSWORD')} "
        f"--role {os.getenv('SNOWFLAKE_ROLE')} "
        f"--warehouse {os.getenv('SNOWFLAKE_WAREHOUSE')} "
        f"--database {os.getenv('SNOWFLAKE_DATABASE')} "
        "--schema PUBLIC"
    )

    run(deploy_cmd)

    print("\n🎉 Deployment completed successfully!")

if __name__ == "__main__":
    main()
