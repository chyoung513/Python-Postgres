import pprint as pp

conn = psycopg2.connect(dbname="dq", user="admin", password="123")
cur = conn.cursor()

cur.execute("CREATE INDEX state_idx ON homeless_by_coc(state)")
cur.execute("EXPLAIN (ANALYZE, format json) SELECT * FROM homeless_by_coc WHERE state = 'CA' and year > '1991-01-01'")
pp.pprint(cur.fetchall())

cur.execute("DROP INDEX IF EXISTS state_idx")
cur.execute("CREATE INDEX state_year_idx ON homeless_by_coc(state, year)")
conn.commit()

cur.execute("EXPLAIN (ANALYZE, format json) SELECT * FROM homeless_by_coc WHERE state = 'CA' and year > '1991-01-01'")
pp.pprint(cur.fetchall())



>>>> The Output is

[([{'Execution Time': 2.933,
    'Plan': {'Actual Loops': 1,
             'Actual Rows': 8946,
             'Actual Startup Time': 0.868,
             'Actual Total Time': 2.522,
             'Alias': 'homeless_by_coc',
             'Exact Heap Blocks': 142,
             'Filter': "(year > '1991-01-01'::date)",
             'Lossy Heap Blocks': 0,
             'Node Type': 'Bitmap Heap Scan',
             'Plan Rows': 144,
             'Plan Width': 480,
             'Plans': [{'Actual Loops': 1,
                        'Actual Rows': 8946,
                        'Actual Startup Time': 0.845,
                        'Actual Total Time': 0.845,
                        'Index Cond': "(state = 'CA'::bpchar)",
                        'Index Name': 'state_idx',
                        'Node Type': 'Bitmap Index Scan',
                        'Parent Relationship': 'Outer',
                        'Plan Rows': 433,
                        'Plan Width': 0,
                        'Startup Cost': 0.0,
                        'Total Cost': 11.54}],
             'Recheck Cond': "(state = 'CA'::bpchar)",
             'Relation Name': 'homeless_by_coc',
             'Rows Removed by Filter': 0,
             'Rows Removed by Index Recheck': 0,
             'Startup Cost': 11.58,
             'Total Cost': 903.33},
    'Planning Time': 0.311,
    'Triggers': []}],)]

[([{'Execution Time': 2.673,
    'Plan': {'Actual Loops': 1,
             'Actual Rows': 8946,
             'Actual Startup Time': 1.014,
             'Actual Total Time': 2.283,
             'Alias': 'homeless_by_coc',
             'Exact Heap Blocks': 142,
             'Lossy Heap Blocks': 0,
             'Node Type': 'Bitmap Heap Scan',
             'Plan Rows': 144,
             'Plan Width': 480,
             'Plans': [{'Actual Loops': 1,
                        'Actual Rows': 8946,
                        'Actual Startup Time': 0.996,
                        'Actual Total Time': 0.996,
                        'Index Cond': "((state = 'CA'::bpchar) AND "
                                      "(year > '1991-01-01'::date))",
                        'Index Name': 'state_year_idx',
                        'Node Type': 'Bitmap Index Scan',
                        'Parent Relationship': 'Outer',
                        'Plan Rows': 144,
                        'Plan Width': 0,
                        'Startup Cost': 0.0,
                        'Total Cost': 5.73}],
             'Recheck Cond': "((state = 'CA'::bpchar) AND (year > "
                             "'1991-01-01'::date))",
             'Relation Name': 'homeless_by_coc',
             'Rows Removed by Index Recheck': 0,
             'Startup Cost': 5.77,
             'Total Cost': 421.57},
    'Planning Time': 0.17,
    'Triggers': []}],)]
