#coding=utf-8
import sys
sys.path.append('C:\\Users\\邱步一\\PycharmProjects\\51test')
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()       
        handle_excel = ExcelUtil('C:\\Users\\邱步一\\PycharmProjects\\51test\\config\\keyword.xls')
        case_lines = handle_excel.get_lines()#获取行数
        if case_lines:#如果取到行数
            for i in range(1,case_lines):#遍历每一行
                is_run = handle_excel.get_col_value(i,3)#获取每一行的第四个单元格其中的值
                if is_run == 'yes':#第四个单元格放置是否为yes，如果为yes运行case
                    except_result_method = handle_excel.get_col_value(i,7)#获取第i行第八列单元格内的预期结果
                    except_result = handle_excel.get_col_value(i,8)#获取第i行第九个单元格内的实际结果
                    method = handle_excel.get_col_value(i,4)#第5个单元格内的执行方法
                    send_value = handle_excel.get_col_value(i,5)#第6个单元格内的输入的数据
                    handle_value = handle_excel.get_col_value(i,6)#第七个单元格内的操作元素
                    self.run_method(method,send_value,handle_value)#使用run_method方法
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print("没有else")
                    else:
                        print('预期结果为空')
                    


                        
    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method)#获取action_methon类中method的值，methon是执行方法
        if send_value == '' and handle_value !='':#输入数据为空，操作数据不为空
            result = method_value(handle_value)#
        elif send_value == '' and handle_value =='':#都为空
            result = method_value()#返回执行方法名称
        elif send_value != '' and handle_value =='':#数据不为空，操作数据为空
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result

if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()