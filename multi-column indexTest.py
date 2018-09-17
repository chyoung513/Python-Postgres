import pprint

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()

cur.execute("EXPLAIN (ANALYZE, format json) DELETE from state_household_incomes")
pprint.pprint(cur.fetchall())

conn.rollback()



>>>> The Output is

[([{'Execution Time': 0.089,
    'Plan': {'Actual Loops': 1,
             'Actual Rows': 0,
             'Actual Startup Time': 0.066,
             'Actual Total Time': 0.066,
             'Alias': 'state_household_incomes',
             'Node Type': 'ModifyTable',
             'Operation': 'Delete',
             'Plan Rows': 230,
             'Plan Width': 6,
             'Plans': [{'Actual Loops': 1,
                        'Actual Rows': 52,
                        'Actual Startup Time': 0.015,
                        'Actual Total Time': 0.024,
                        'Alias': 'state_household_incomes',
                        'Node Type': 'Seq Scan',
                        'Parent Relationship': 'Member',
                        'Plan Rows': 230,
                        'Plan Width': 6,
                        'Relation Name': 'state_household_incomes',
                        'Startup Cost': 0.0,
                        'Total Cost': 12.3}],
             'Relation Name': 'state_household_incomes',
             'Startup Cost': 0.0,
             'Total Cost': 12.3},
    'Planning Time': 0.354,
    'Triggers': []}],)]
