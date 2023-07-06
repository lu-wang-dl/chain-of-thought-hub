# Databricks notebook source
# MAGIC %pip install tensor_parallel
# MAGIC %pip install einops

# COMMAND ----------

# MAGIC %sh
# MAGIC python run_mmlu_open_source.py --ckpt_dir mosaicml/mpt-7b-instruct --param_size 7b --model_type mpt-7b

# COMMAND ----------

from huggingface_hub import notebook_login

notebook_login()

# COMMAND ----------

# MAGIC %sh
# MAGIC export PYTHONIOENCODING=utf8
# MAGIC python run_mmlu_open_source.py --ckpt_dir decapoda-research/llama-7b-hf --param_size 7b --model_type llama --data_dir /dbfs/FileStore/lu/data/data

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /dbfs/FileStore/lu/data/data/dev/abstract_algebra_dev.csv
# MAGIC #cat /Workspace/Repos/lu.wang@databricks.com/chain-of-thought-hub/MMLU/data/dev/abstract_algebra_dev.csv

# COMMAND ----------

compute_metric(output_filename)
