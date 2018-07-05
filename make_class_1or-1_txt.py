import os
import random
import xml.dom.minidom
import operator

def searchObject(fileNameList=[],xmlFilePath='',classname=''):
    L = []
    if not fileNameList:
        print('fileNameList is NULL')
        return []
    if not xmlFilePath:
        print('xmlFilePath is NULL')
        return []
    if not classname:
        print('classname is NULL')
        return []
    for fileName in fileNameList:
        xmlname = fileName+'.xml'
        xmlPath = xmlFilePath+xmlname
        
        DOMTree = xml.dom.minidom.parse(xmlPath)
        collection = DOMTree.documentElement
        objects = collection.getElementsByTagName("object")
        result = '-1'
        for object in objects:
            class_name_elements = object.getElementsByTagName("name")[0]
            class_name = class_name_elements.childNodes[0].data
            if operator.eq(class_name,classname):
                result = ' 1'
                break
        L.append(result)
    return L


classNameFilePath = './myvoc/classname.txt'
picForTrain = './myvoc/ImageSets/Main/trainval.txt'


f0 = open(classNameFilePath)
linesClassName = f0.readlines()#all class name
L0 = len(linesClassName)
for i in range(L0):
    linesClassName[i] = linesClassName[i].strip('\n')
f0.close()

f1_train = open(picForTrain)
linesTrain = f1_train.readlines()#train picture set
L1 = len(linesTrain)
for i in range(L1):
    linesTrain[i] = linesTrain[i].strip('\n')
f1_train.close()


for classname in linesClassName:
    filename ='./myvoc/ImageSets/' + classname + '_trainval.txt'
    fp_temp = open(filename,'a+')
    result_list = searchObject(linesTrain,'./myvoc/Annotations/',classname)
    for i in range(L1):
        content = '{} {}\n'.format(linesTrain[i],result_list[i])
        fp_temp.write(content)
    fp_temp.close()
    print('classify the {} success'.format(classname))
print('ALL Finished')
    
    