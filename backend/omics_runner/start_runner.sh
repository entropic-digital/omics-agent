eval "$(micromamba shell hook --shell bash)"

# Check if environment exists, if not create it
if ! micromamba env list | grep -q "omics-runner"; then
    echo "Creating omics-runner environment..."
    micromamba create -f environment.yml
else
    echo "omics-runner environment already exists"
fi

micromamba activate omics-runner

# Install the current environment as a Jupyter kernel
python -m ipykernel install --user --name omics-runner --display-name "Python (omics-runner)"

# Start Jupyter server
jupyter notebook --port 8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.disable_check_xsrf=True