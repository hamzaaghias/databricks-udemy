import dlt

@dlt.table(
    name = "basic_tbl"
)
def basic_tbl():
    return spark.range(100)