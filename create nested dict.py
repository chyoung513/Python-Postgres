from psycopg2.extensions import AsIs
#connect to Postgres
conn = psycopg2.connect(dbname="", user="", password="")
cur = conn.cursor()

readable_description = {}
#table_names is list of names for tables
for table in table_names:
    cur.execute("SELECT * FROM %s LIMIT 0", [AsIs(table)])
    #create nest dictionary
    #type_mappings is object that map type code and type names
    readable_description[table] = dict(
        columns=[
            dict(
                name=col.name,
                type=type_mappings[col.type_code],
                length=col.internal_size
            )
            for col in cur.description #iteract each table and assign table column's value to dict value
        ]
    )
print(readable_description)



# the output of dictionary as bellow
{
    "homeless":
        {
            columns: [
                {
                    name: "id"
                    type: "int4"
                    internal_size: 4
                },
                {
                    name: "year",
                    type: "date",
                    internal_size: 4
                }
            ]
            }
    }
