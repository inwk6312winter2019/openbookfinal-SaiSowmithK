from collections import Counter
def file_logs(file):
    opened_file = open(file, 'r')
    content = opened_file.readlines()
    content = [x.strip() for x in content]
    get_log = open("get.log", "w")
    post_log = open("post.log", "w")
    put_log = open("put.log", "w")
    delete_log = open("delete.log", "w")
    for i in content:
        if "GET" in i:
            get_log.write(str(i))
            get_log.write("/n")
        if "POST" in i:
            post_log.write(str(i))
            post_log.write("/n")
        if "PUT" in i:
            put_log.write(str(i))
            put_log.write("/n")
        if "DELETE" in i:
            delete_log.write(str(i))
            delete_log.write("/n")
    get_log.close()
    post_log.close()
    put_log.close()
    delete_log.close()
    opened_file.close()
    return True
file_logs("access.log")

