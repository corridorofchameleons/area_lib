# сделаем связь many to many и left join промежуточной таблицы к категориям

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# таблица продуктов
prod_data = [
    (1, 'hammer'),
    (2, 'hummer'),
    (3, 'hunter'),
]

prod_cols = ['product_id', 'name']

products = spark.createDataFrame(prod_data, prod_cols)

# таблица категорий
cat_data = [
    (1, 'instruments'),
    (2, 'cars'),
    (3, 'toys'),
    (4, 'other'),
]

cat_cols = ['category_id', 'name']

categories = spark.createDataFrame(cat_data, cat_cols)

# связующая таблица
many_to_many_data = [
    (1, 1, 1),
    (2, 1, 3),
    (3, 2, 2),
    (4, 2, 3),
]
many_to_many_cols = ['id', 'product_id', 'category_id']
intermediate = spark.createDataFrame(many_to_many_data, many_to_many_cols)

products.createOrReplaceTempView('products')
categories.createOrReplaceTempView('categories')
intermediate.createOrReplaceTempView('intermediate')

# запрос выводит пары продукт-категория
spark.sql('SELECT products.name, categories.name FROM products '
          'FULL JOIN intermediate USING(product_id)'
          'LEFT JOIN categories USING(category_id)'
          'ORDER BY 1').show()
