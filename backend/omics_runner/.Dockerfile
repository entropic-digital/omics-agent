FROM ubuntu:24.04

# Install micromamba
ENV MAMBA_ROOT_PREFIX=/opt/conda
ENV PATH=$MAMBA_ROOT_PREFIX/bin:$PATH

RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget -qO- https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba \
    && mv bin/micromamba /usr/local/bin/ \
    && rm -rf bin

# Copy environment files
WORKDIR /app
COPY environment.yml .
COPY start_runner.sh .

# Initialize micromamba and create environment
RUN micromamba shell init --shell bash && \
    eval "$(micromamba shell hook --shell bash)" && \
    micromamba create -f environment.yml && \
    micromamba clean --all --yes

# Set up entrypoint
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash", "start_runner.sh"]

# Expose Jupyter port
EXPOSE 8888
