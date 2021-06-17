FROM registry.ardigen.com/biome-forte/dockers/base-docker

WORKDIR /source

ADD . .

RUN conda create --name pub --file environment.yml

# Set conda env as default
ENV ENV_NAME "pub"
RUN echo "source activate $ENV_NAME" >> ~/.bashrc
ENV PATH /opt/conda/envs/"$ENV_NAME"/bin:$PATH

RUN jupyter nbextensions_configurator enable

EXPOSE 8888
CMD jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root --no-browser

