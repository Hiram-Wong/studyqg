import re
import pymysql

with open('README.md',mode='r',encoding='utf-8') as f:
    res=f.read()

def mysql(sql):
    conn = pymysql.connect(
        host='localhost',
        user='python',
        passwd='python',
        db='python',
        charset='utf8'
    )
    # print(type(choice),type(parameter))
    # sql语句
    # sql = "INSERT INTO study ("+type+") VALUES ('" + parameter + "')"
    # sql = "UPDATE study SET answer = '"+choice+"' WHERE question ='"+parameter+"'"
    # print(sql)
    # 创建游标对象
    cur = conn.cursor()
    # 使用execute方法执行SQL语句
    result = cur.execute(sql)
    conn.commit()
    conn.close()

def question():
    # i = [x for x in range(1,1417)]
    # print(i)
    datalist = []
    for i in range(1,1417):
        pat_question = str(i) + '、(.*?)\n'
        data = re.compile(pat_question,re.S).findall(res)
        datalist.append(data)
    return datalist
    # for i in datalist:
    #     print('正在写入',i[0])
    #     mysql(i[0])
    # print(len(datalist))
# question()

def answers():
    pat_answer = '答案：(.*?)\n'
    data = re.compile(pat_answer,re.S).findall(res)
    print(len(data))
    questions = question()
    for i in range(1416):
        print('正在写入',question()[i][0] ,data[i])
        mysql(data[i],question()[i][0])

# answers()
def choice():
    pat_choice = 'A、(.*?)答案'
    data = re.compile(pat_choice,re.S).findall(res)
    questions = question()
    for i in range(len(data)):
        data_choice = data[i]
        pat_abcd = '(.*?)\n\n'
        data_abcd =re.compile(pat_abcd,re.S).findall(data_choice)
        data_a = data_abcd[0]
        data_b = data_abcd[1][2:]
        try:
            data_c = data_abcd[2][2:]
            data_d = data_abcd[3][2:]
        except:
            pass
        if  data_c:
            if data_d:
                # print(data_a,data_b,data_c,data_d)
                sql = "UPDATE study SET a = '" + data_a + "',b = '"+data_b+"',c = '"+data_c+"',d = '"+data_d+"' WHERE question ='" + questions[i][0] + "'"
                mysql(sql)
                print(sql)
            else:
                # print(data_a, data_b, data_c,'null')
                sql = "UPDATE study SET a = '" + data_a + "',b = '"+data_b+"',c = '"+data_c+"' WHERE question ='" + questions[i][0] + "'"
                mysql(sql)
                print(sql)
        else:
            # print(data_a, data_b,'null','null')
            sql = "UPDATE study SET a = '" + data_a + "',b = '"+data_b+"' WHERE question ='" + questions[i][0] + "'"
            mysql(sql)
            print(sql)
        data_c = ''
        data_d = ''
choice()