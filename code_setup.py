https://docs.snowflake.com/en/developer-guide/snowpark/python/setup

#conda create --name py39_env --override-channels -c https://repo.anaconda.com/pkgs/snowflake python=3.9 numpy pandas pyarrow

#conda create --name py382_env --override-channels -c  python=3.8 numpy pandas pyarrow

conda create --name devenv_py12v --override-channels -c https://repo.anaconda.com/pkgs/snowflake python=3.12 numpy pandas pyarrow

conda init

conda activate devenv_py12v

conda install snowflake-snowpark-python

conda install snowflake-snowpark-python=1.5.0

pip install snowflake-snowpark-python==1.5.0

pip install snowflake -U

pip install snowflake-cli-labs

# Create Project Structure
snow init my_snowpark_project --template example_snowpark



snow snowpark deploy --help