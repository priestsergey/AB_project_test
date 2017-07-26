import pymysql

dbconfig = {

}

connection = pymysql.connect(**dbconfig, cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELCT group_id, group_name, group_header, group_footer FROM group_list"
        cursor.execute(sql)
        result = cursor.fetchall()


finally:
    connection.close()