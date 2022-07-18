# Microbiome Protein Embeddings

The repository contains code to reproduce analyses included in our publication: [Deep embeddings to comprehend and visualize microbiome protein space](https://www.biorxiv.org/content/10.1101/2021.07.21.452490v1)


## Download data

To download data (embeddings) used in the notebooks run:
```bash
./download-data.sh
```
Data will be downloaded to `data` folder.

# How to set up environment

## Install required tools
```
- [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- timelimit (sudo apt install timelimit)
```

## Create environment and install dependencies
```bash
conda env create --file environment.yml
```

## Activate the environment
```
conda activate mpe
```

Now environment is ready to run the notebooks.

## Citation Guidelines

If you find the repository useful, please cite our paper. 

```
@article{odrzywolek2022,
  title={Deep embeddings to comprehend and visualize microbiome protein space},
  author={Odrzywolek, Krzysztof and Karwowska, Zuzanna and Majta, Jan and Byrski, Aleksander and Milanowska-Zabel, Kaja and Kosciolek, Tomasz},
  journal={Scientific reports},
  volume={12},
  number={1},
  pages={1--15},
  year={2022},
  publisher={Nature Publishing Group}
}
```
