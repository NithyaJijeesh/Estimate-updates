from django.db import connection
def get_next_auto_id(model):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nextval('app1_estimate_estimateid_seq')")
        next_id = cursor.fetchone()[0]
    return next_id
