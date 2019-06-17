# -*-coding:utf-8 -*-
# @Author : Zhigang

from utils.ParseExcel import ParseExcel
from utils.Log import *
from config.project_var import *
from action.AppAction import *
import traceback

def runScript():
    excel=ParseExcel()
    excel.loadWorkBook(data_file_path)
    sheetObj=excel.getSheetByName("测试用例")
    caseActive=excel.getColumn(sheetObj,testCaseIsExecute)

    for id,id_c in enumerate(caseActive[1:],2):
        testCaseName=excel.getCellOfValue(sheetObj,rowNo=id,colsNo=testCaseDesc)
        testCaseSheet=excel.getCellOfValue(sheetObj,rowNo=id,colsNo=testCaseSheetName)
        if id_c.value=="y":
            "需要执行的用例"
            info("{name}-->测试用例需要执行".format(name=testCaseName))
            caseObj=excel.getSheetByName(testCaseSheet)
            caseStepsNum=excel.getRowsNumber(caseObj)
            caseSuccessNum=0
            for i in range(2,caseStepsNum+1):
                rowObj=excel.getRow(caseObj,i)
                stepDescrible=rowObj[testStepDesc-1].value
                stepKeyword=rowObj[testStepKeyWords-1].value
                stepLocateMode=rowObj[testStepLocateMode-1].value
                stepLocateExp=rowObj[testStepLocateExp-1].value
                stepOperateValue=rowObj[testStepOperateValue-1].value
                # print (stepKeyword,stepLocateMode,stepLocateExp,stepOperateValue)
                if stepKeyword is not None and stepLocateMode is None and stepLocateExp is None \
                    and stepOperateValue is None:
                    command="{word}()".format(word=stepKeyword)
                elif stepKeyword is not None and stepLocateMode is not None and stepLocateExp is not None \
                    and stepOperateValue is None:
                    command="{word}('{id}','{exp}')".format(word=stepKeyword,id=stepLocateMode,
                                                            exp=stepLocateExp)
                elif stepKeyword is not None and stepLocateMode is not None and stepLocateExp is not None \
                    and stepOperateValue is not None:
                    command = "{word}('{id}','{exp}','{content}')".format(word=stepKeyword, id=stepLocateMode,
                                                              exp=stepLocateExp,content=stepOperateValue)
                elif stepKeyword is not None and stepLocateMode is None and stepLocateExp is None \
                    and stepOperateValue is not None:
                    command = "{word}('{content}')".format(word=stepKeyword,content=stepOperateValue)
                try:
                    eval(command)
                except Exception as e:
                    info ("执行测试步骤失败:{step}".format(step=command))
                    excel.writeCell(caseObj,content="fail",rowNo=i,colsNo=testStepExecuteResult,style="red")
                    excel.writeCell(caseObj, content=traceback.format_exc(), rowNo=i, colsNo=testStepErrorInfo, style="red")
                    # 写截图路径
                    sreenShotPath=capture_screen()
                    excel.writeCell(caseObj, content=sreenShotPath, rowNo=i, colsNo=testStepErrorScreenshot, style="red")
                else:
                    info("执行测试步骤成功:{step}".format(step=stepDescrible))
                    caseSuccessNum+=1
                    excel.writeCell(caseObj, content="pass", rowNo=i, colsNo=testStepExecuteResult, style="green")
                finally:
                    excel.writeCellCurrentTime(caseObj,rowNo=i,colsNo=testStepExecuteTime)
            sheetObj = excel.getSheetByName("测试用例")
            if caseSuccessNum==caseStepsNum-1:
                excel.writeCell(sheetObj,content="pass",rowNo=id,colsNo=testCaseExecuteResult,style="green")
            else:
                excel.writeCell(sheetObj,content="fail",rowNo=id,colsNo=testCaseExecuteResult,style="red")
            excel.writeCellCurrentTime(sheetObj,rowNo=id,colsNo=testCaseExecuteTime)
        else:
            info("{name}-->测试用例忽略执行".format(name=testCaseName))

if __name__=="__main__":
    runScript()