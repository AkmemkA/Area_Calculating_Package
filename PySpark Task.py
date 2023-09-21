from pyspark.sql import SparkSession

# Создание Spark сессии
spark = SparkSession.builder.getOrCreate()

# Создание датафрейма для продуктов
products_data = [("Product1", 1), ("Product2", 1), ("Product3", 2), ("Product4", None)]
products_df = spark.createDataFrame(products_data, ["Product", "ProductID"])

# Создание датафрейма для категорий
categories_data = [(1, "Category1"), (2, "Category2"), (3, "Category3")]
categories_df = spark.createDataFrame(categories_data, ["CategoryID", "Category"])

# Объединение датафреймов по полю ProductID
result_df = products_df.join(categories_df, products_df.ProductID == categories_df.CategoryID, "left_outer")

# Выбор нужных столбцов
result_df = result_df.select(products_df.Product, categories_df.Category)

# Вывод результирующего датафрейма
result_df.show()