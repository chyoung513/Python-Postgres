import pprint

conn = psycopg2.connect(dbname="dq", user="hud", password="123")
cur = conn.cursor()

cur.execute("EXPLAIN (format json) SELECT COUNT(*) FROM homeless_by_coc WHERE year > '2012-01-01'")
pprint.pprint(cur.fetchall())


>>>> The Output is 
[([{'Plan': {'Node Type': 'Aggregate',
             'Plan Rows': 1,
             'Plan Width': 0,
             'Plans': [{'Alias': 'homeless_by_coc',
                        'Filter': "(year > '2012-01-01'::date)",
                        'Node Type': 'Seq Scan',
                        'Plan Rows': 50645,
                        'Plan Width': 0,
                        'Relation Name': 'homeless_by_coc',
                        'Startup Cost': 0.0,
                        'Total Cost': 2363.61}],
             'Startup Cost': 2490.23,
             'Strategy': 'Plain',
             'Total Cost': 2490.24}}],)]
