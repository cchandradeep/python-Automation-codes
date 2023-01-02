
from itertools import count
from operator import countOf
import re
import pandas as pd
import PySimpleGUI as sg
import os

sg.Titlebar('VALIDATION')
working_dir = os.getcwd()

layout=[[sg.Text('Choose C file: ', size=(15,1)), sg.InputText(key="file_to_read" ), sg.FileBrowse(file_types=(("C files", "*.c"),),size=(10,1))],
[sg.Text('Choose location:',size=(15,1)), sg.InputText(key='exportfileName'),sg.FileSaveAs('Save As',file_types=(("xlsx", "*.xlsx"),),size=(10,1))],
[sg.Text('review',visible=False,key='label1',size=(15,1)),sg.Input(key='review',visible=False,size=(15,1)),
sg.Text('passed',visible=False,key='label2',size=(15,1)),sg.Input(key='passed',visible=False,size=(15,1))],
[sg.Text('fail',visible=False,key='label3',size=(15,1)),sg.Input(key='fail',visible=False,size=(15,1)),
sg.Text('percent',visible=False,key='label4',size=(15,1)),sg.Input(key='percent',visible=False,size=(15,1))],
[sg.Push(),sg.Submit("Compare",size=(10,1)), sg.Exit(size=(10,1))]]

def main():
    window = sg.Window('validation',layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        
        elif event == 'Compare':
            file_to_read = values['file_to_read']
            exportfilename = values['exportfileName']
            if file_to_read and exportfilename:
                pas,fai,su,perc=compare(file_to_read,exportfilename)
                sg.popup('success')

            window['label1'].update("Total",visible=True)
            window['review'].update(su,visible=True)
            window['label2'].update("Pass",visible=True)
            window['passed'].update(pas,visible=True)
            window['label3'].update("Fail",visible=True)
            window['fail'].update(fai,visible=True)
            window['label4'].update("Percentage",visible=True)
            window['percent'].update(perc,visible=True)

        else: 
            sg.popup('enter all fields')
        # print()
        # print(event, values)

    window.close()

    # file_to_read = r'C:\Users\229383\Downloads\file1.c'
# print(data)
# print(type(data))

# search_el=re.findall('bool',data)
# print(search_el)
# text = 'Method_name'
# for line in data:
#     print( (line,text),end='')
#     if re.search(line,text):
#         print('matched')
def compare(file_to_read,exportfilename):
    file =open(file_to_read,'r')
    data = file.read()
    with open(file_to_read) as file1:
        data1 = file1.readlines()
    regex = r"([\w\*]+(\s)*?)\(([^;]*?)\)\s*;"
    # regex = r'\w+(?=\()'
    matches = re.finditer(regex, data, re.MULTILINE)
    # matches = re.findall(regex,data)

    list=[]
    # for match in matches:
    #     print(match)

    for matchNum, match in enumerate(matches):
        s="{match}".format(matchNum = matchNum+1, match = match.group())
        # print(s)
        list.append(s)
    # print(list)

    # regex1 = r'\w+(?=\()'
    # mat=re.findall(regex1,data)
    # for match1 in mat:
    #     print(match1)
    q=[]  
    dict={}
    for i in list:
        x=i.partition('(')[0]   #function_name

        q.append(x)
        # print(x)
        # fun = x.split(' ')
        # print(fun[-1])

        o=[]
        y=i.partition('(')[-1]
        z=y.split(',')
    
        for l in z:
            m = l.partition(')')[0]
            n = m.split(' ')
            p =n[-1]
            o.append(p)         #aurguments
        dict[x]=o  
    print(dict)    
    # print(x)
    # print(o)
    
    # y=[]  
    # for j in x:
    #     y=j.partition(',')
    #     print(y)
    # print(data)
    # print(data1)
    
    k=1
    n=0
    pas=[]
    fai=[]
    su=[]
    pas=0
    fai=0
    df1=pd.DataFrame(columns=['Actual_function','Expected_function','Actual_arg','Expected_arg','Status'])
    for a,e in zip(dict,dict.values()):
        for b in range(k,len(data1)):
            # print(data1[b])
            if "METHOD NAME" in data1[b]:
                # print(data1[b])
                if a in data1[b]:
                    df1.loc[len(df1.index)]=[a ,data1[b]," "," ",'correct']
                    # print("correct")
                    # print(a)
                    # print(data1[b])
                    # print(k)
                    pas=pas+1
                    k+=b+1
                    break
                else:
                    df1.loc[len(df1.index)]=[a ,data1[b]," "," ",'incorrect']
                    # print('incorrect')
                    # print(a)
                    # print(data1[b])
                    k+=b+1
                    fai=fai+1
                    break

    # for e in dict.values():
        # print(e)
        for f in range(n,len(data1)):
            # print(data1[f])
            # string=data1[f]+data1[f+1]+data1[f+2]
            if "PARAMETER" in data1[f]:
                # print(data1[f])
                for arg in e:
                    if arg in data1[f]:
                        df1.loc[len(df1.index)]=[" "," ",arg,data1[f],'correct']
                        # print('correct')
                        # print(arg)
                        # print(data1[f])   
                        pas=pas+1
                        f=f+1
                        n=f
                        
                    else:
                        # print('incorrect')
                        df1.loc[len(df1.index)]=[' ',' ',arg,data1[f],'incorrect']

                        # print(arg)
                        # print(data1[f])
                        # print(l)
                    
                        f=f+1
                        n=f
                        fai=fai+1
               
                break  
    print(pas)  #passed cases
    print(fai)  #failed cases   
    su=pas+fai
    print(su) #review total length
    perc=round((pas/su)*100,2)
    print(perc)
    # print(df1)
    df1.to_excel(exportfilename,index=False,engine='openpyxl')
    return pas,fai,su,perc 
    
    # from openpyxl import load_workbook
    # import pandas as pd
    # writer = pd.ExcelWriter('test.xlsx', engine='openpyxl') 
    # wb  = writer.book
    # df = pd.DataFrame({'Expected method name': [],
    #                   'actual method name': [],
    #                   'expected parameter': [],
    #                   'actual parameter': [],
    #                   'status':[]})

    # df.to_excel(writer, index=False)
    # wb.save('test.xlsx')
    # import pandas  

    # data = pandas.DataFrame() 
    # data['expected result'] = s[0::3] 
    # data['actual'] = s[1::3] 
    # data['status'] = s[2::3]
    # data.to_excel('report.xlsx', index = False)

if __name__ == '__main__':
    main()

    
