# faster-rcnn-voc-
主要用来为faster rcnn 制作提供训练数据集
特此声明：此资源引自https://github.com/EddyGao/make_VOC2007
参考了其中的部分代码，原资源没有生成各目标是否存在在图片的1或者-1表示的txt文件
首先介绍一下voc 2007数据集：

faster rcnn voc数据集制作方式如下：
1)JPEGImages文件夹（所有图片）

2)Annatations文件夹（xml格式的标签文件，xml文件名对应了每张图片名称）

3)ImageSets文件夹

  3.1 Action存放的是人的动作，我们暂时不用
  
  3.2 Layout存放的人体部位的数据。我们暂时不用
  
  3.3 Main存放的是图像物体识别的数据，分为20类
  
	  Main里面有test.txt , train.txt, val.txt ,trainval.txt这四个文件我们后面会用（make_main_txt.py）生成
	  
4）Segmentation存放的是可用于分割的数据

如果你下载了VOC2007数据集，那么把它解压，把各个文件夹里面的东西删除，保留文件夹名字。如果没下载，那么就仿照他的文件夹格式，自己建好空文件夹就行。

步骤：
1)把你的图片放到JPEGSImages里面，在VOC2007里面，人家的图片文件名都是000001.jpg类似这样的，我们也统一格式，把我们的图片名字重命名成这样的，如果你的文件太多怎么办，请看我的另一篇文章http://blog.csdn.NET/gaohuazhao/article/details/60324715 能批量重命名文件

2)labelImg手动标注，会自动生成图片信息的xml文件（我在windows7下做的），xml文件存在Annatations文件夹
  一张张的慢慢画框。。。。。。。。。大约过了几个小时，好继续下一步

3)搞定ImageSets文件夹中的Main文件夹中的四个文件test.txt , train.txt, val.txt ,trainval.txt
  用make_main_txt.py生成

4)搞定每一张图片是否包含某个目标，文件比如为：dog_test.txt, dog_train.txt, dog_val.txt, dog_trainval.txt
  用make_class_1or-1_txt.py生成
OK，制作完成。



