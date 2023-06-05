# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM `samples`.`tpch`.`customer`;

# COMMAND ----------

# MAGIC
# MAGIC
# MAGIC %sql
# MAGIC SELECT c_name, c_phone FROM `samples`.`tpch`.`customer`
# MAGIC where c_mktsegment = 'BUILDING'
# MAGIC order by c_name;

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC SELECT c_name, c_address, c_phone FROM `samples`.`tpch`.`customer`
# MAGIC where c_mktsegment = 'BUILDING'
# MAGIC order by c_name;
