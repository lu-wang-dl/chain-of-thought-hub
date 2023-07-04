# Databricks notebook source
# MAGIC %pip install tensor_parallel
# MAGIC %pip install einops

# COMMAND ----------

# MAGIC %sh
# MAGIC python run_mmlu_open_source.py --ckpt_dir mosaicml/mpt-7b-instruct --param_size 7b --model_type mpt-7b

# COMMAND ----------


