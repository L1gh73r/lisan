# -*- coding:gbk -*-

sInput = '' #��������⹫ʽ�ַ���
sParse = '' #������sInput
variable = [] #���湫ʽ�еı���
ornl = [] #����ȡ��ʽ��С��
andnl = [] #����ȡ��ʽ�����
fore = '' #����ǰ��Ĳ���
back = '' #���ź���Ĳ���

def myinput():
    global sInput
    print("������һ���������⹫ʽ(ԭ����������ĸ��ʾ,'~'��ʾ�� '&'��ʾ��ȡ '|'��ʾ��ȡ '>'��ʾ�̺� ':'��ʾ�ȼ� '@'��ʾ���,��������'()'):")
    sInput = input()

def getVariale():
    global sInput,variable
    for c in sInput:
        if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z' :
            if c not in variable:
                variable.append(c)
        elif c!='~' and c!='&' and c!='|' and c!='(' and c!=')' and c!='>' and c!=':' and c!='@':
            print('�������󣡣�')
    variable = sorted(variable)

def getFB(c):
    global sInput,sParse,fore,back
    slen = len(sParse)
    for i in range(0,slen):  #����sParse�������ַ�
        if sParse[i] is c:
            if sParse[i-1] != ')': #�ҵ�fore
                fore = sParse[i-1]
            else:
                flag = 1
                j = i-2
                while flag != 0:
                    if sParse[j] == '~':
                        j-=1
                    if sParse[j] == '(':
                        flag-=1
                    if sParse[j] == ')':
                        flag+=1
                    j-=1
                fore = sParse[j+1:i]
            if sParse[i+1] != '(': #�ҵ�back
                back = sParse[i+1]
            else:
                flag = 1
                j = i+2
                while flag != 0:
                    if sParse[j] == '~':
                        j+=1
                    if sParse[j] == ')':
                        flag-=1
                    if sParse[j] == '(':
                        flag+=1
                    j+=1
                back = sParse[i+1:j]
            if c == '>':
                sParse = sParse.replace(fore+'>'+back,'('+'~'+fore+'|'+back+')')
            elif c == ':':
                sParse = sParse.replace(fore+':'+back,'('+fore+'&'+back+')|(~'+fore+'&~'+back+')')
            elif c == '@':
                sParse = sParse.replace(fore+'@'+back,'~('+'('+fore+'&'+back+')|(~'+fore+'&~'+back+')'+')')

def parseInput():
    global sInput,sParse
    sParse = sInput
    getFB('>')
    getFB(':')
    getFB('@')

def cal():
    global sInput,sParse,variable,ornl,andnl,orResult,andResult
    vlen = len(variable) #��������
    n = 2**vlen   #�����������
    print('��ֵ�����£�')
    print(variable,sInput+'��',sParse)
    for nl in range(0,n):      #��ȡ��ֵ��
        value = []    #��ֵ
        j = nl   #��ֵ��ǰ��
        for i in range(0,vlen):
            value.append(0)
        i = 0
        while j!=0:
            value[i]=j%2
            j=j//2
            i+=1
        value.reverse()
        value = list(map(str,value))
        s = sParse
        for x in range(0,vlen):
            s = s.replace(variable[x],value[x])
        result = eval(s)&1
        if result == 1:
            ornl.append(nl)
        else:
            andnl.append(nl)
        print(value,result)

def outprint():
    print('����ȡ��ʽ��')
    print('��',ornl,sep='')
    print('����ȡ��ʽ��')
    print('��',andnl,sep='')

def main():
    myinput()
    getVariale()
    parseInput()
    cal()
    outprint()

if __name__=='__main__':
    main()

