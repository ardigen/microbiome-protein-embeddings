FROM continuumio/miniconda3

# PYTHONDONTWRITEBYTECODE prevents python from creation of .pyc files - lighter images!
ENV PYTHONDONTWRITEBYTECODE=true
ENV CONDA_DIR=/opt/conda

# install and configure Ubuntu-relevant packages
RUN apt-get update && \
    apt-get install -y apt-file apt-utils  && \
    apt-file update && \
    apt-get install -y --no-install-recommends --fix-missing \
        build-essential \
        gcc \
        git \
        htop \
        vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /source

ADD . .

RUN conda env create --file environment.yml

# Set conda env as default
ENV ENV_NAME "mpe"
RUN echo "source activate $ENV_NAME" >> ~/.bashrc
ENV PATH /opt/conda/envs/"$ENV_NAME"/bin:$PATH

EXPOSE 8888
CMD jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root --no-browser

