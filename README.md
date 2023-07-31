# Phenotype Embedding with Autoencoders

This project is an exploration into using autoencoders to embed patient phenotypes into a lower dimensional space for further analysis.

## Overview

The main objective of the project is to build an autoencoder that takes in a sparse vector of ones and zeros, each corresponding to a specific Human Phenotype Ontology (HPO) term that a patient has. The autoencoder embeds this information into a low dimensional space which can be utilized for further analysis.

As a first step, I generate plausible phenotypes by taking a subset of a list of phenotypes from various diseases and building a dataset to train the autoencoder.

