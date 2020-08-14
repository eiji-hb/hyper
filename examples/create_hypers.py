
from datetime import datetime
from pathlib import Path

from tableauhyperapi import HyperProcess, Telemetry, \
    Connection, CreateMode, \
    NOT_NULLABLE, NULLABLE, SqlType, TableDefinition, \
    Inserter, \
    escape_name, escape_string_literal, \
    HyperException

# Table Definitions required to create tables
test01_table = TableDefinition(
    # Since the table name is not prefixed with an explicit schema name, the table will reside in the default "public" namespace.
    table_name="test01",
    columns=[
        TableDefinition.Column("ID", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("Mathematics", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("Science", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("English", SqlType.big_int(), NOT_NULLABLE),
        TableDefinition.Column("Japanese", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("History", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("Geography", SqlType.text(), NOT_NULLABLE),
    ]
)

test02_table = TableDefinition(
    # Since the table name is not prefixed with an explicit schema name, the table will reside in the default "public" namespace.
    table_name="test02",
    columns=[
        TableDefinition.Column("ID", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("Mathematics", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("Science", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("English", SqlType.big_int(), NOT_NULLABLE),
        TableDefinition.Column("Japanese", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("History", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("Geography", SqlType.text(), NOT_NULLABLE),
    ]
)




def run_create_hyper_file_from_csv():


  path_to_database = Path("test01_02.hyper")


  process_parameters = {
      # Limits the number of Hyper event log files to two.
      "log_file_max_count": "2",
      # Limits the size of Hyper event log files to 100 megabytes.
      "log_file_size_limit": "100M"
  }

  # Starts the Hyper Process with telemetry enabled to send data to Tableau.
  # To opt out, simply set telemetry=Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU.
  with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU, parameters=process_parameters) as hyper:

      # Optional connection parameters.
      # They are documented in the Tableau Hyper documentation, chapter "Connection Settings"
      # (https://help.tableau.com/current/api/hyper_api/en-us/reference/sql/connectionsettings.html).
      connection_parameters = {"lc_time": "en_US"}

      # Creates new Hyper file "customer.hyper".
      # Replaces file with CreateMode.CREATE_AND_REPLACE if it already exists.
      with Connection(endpoint=hyper.endpoint,
                      database=path_to_database,
                      create_mode=CreateMode.CREATE_AND_REPLACE,
                      parameters=connection_parameters) as connection:

          connection.catalog.create_table(table_definition=test01_table)
          connection.catalog.create_table(table_definition=test02_table)
          # Using path to current file, create a path that locates CSV file packaged with these examples.
          path_to_csv1 = str(Path(__file__).parent / "data" / "csv" /"test01.csv")
          path_to_csv2 = str(Path(__file__).parent / "data" / "csv" /"test02.csv")

          # Load all rows into "Customers" table from the CSV file.
          # `execute_command` executes a SQL statement and returns the impacted row count.
          count_in_customer_table = connection.execute_command(
              command=f"COPY {test01_table.table_name} from {escape_string_literal(path_to_csv1)} with "
              f"(format csv, NULL 'NULL', delimiter ',', header)")
          count_in_customer_table = connection.execute_command(
              command=f"COPY {test02_table.table_name} from {escape_string_literal(path_to_csv2)} with "
              f"(format csv, NULL 'NULL', delimiter ',', header)")
  print("done")



if __name__ == '__main__':
    try:
        run_create_hyper_file_from_csv()
    except HyperException as ex:
        print(ex)
        exit(1)