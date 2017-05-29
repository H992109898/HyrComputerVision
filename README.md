# HyrComputerVision

这是一个计算机视觉展示的网站，结合web技术和机器学习      
                                
工具：
- web前端：h5+css+js和前端框架bootstrap
- web后端：django+mySQL
- 机器学习相关：主要scikit-learn库
- 图像处理相关：opencv, dlib, skimage，均用其python接口                     

要实现的功能有：                
- 表情识别
- 人脸识别
- 物体识别
- 车牌识别 
- 基本的用户管理（本来是想做成像微软认知服务一样然后放在网上让用户购买服务的）

各部分详细说明：    

每个独立的模块，都是上传一张图片，右边给出服务器的json格式返回。如下图；   
![image](https://github.com/H992109898/HyrComputerVision/blob/master/img/emotion_show.png)       

支持3种放入图片方式：   
- 网站上提供的备选图片
- 图片的url
- 本地上传   

0. 用户管理     
- 账号管理：               
用户注册，登录，修改信息（密码，邮箱，头像）
- 购买管理：   
注册用户可购买服务，购买服务记录在数据库   

1. 表情识别                        
训练两个表情识别模型：    
- 模型输入：48*48灰度像素
- 模型输出：happinsee, sadness, netural, surprise 4种表情估分

模型1：
- 预处理：均衡直方化消除关照影响
- 降维：PCA直接降到169维
- 训练：浅层神经网络直接训练  
模型文件：pipe_nn.pkl(joblib读取)

模型2：
- 预处理：
1. 均衡直方化消除关照影响
2. gabor多方向多尺度滤波
3. AAM模型找出68关键点
4. 找出关键点上对象滤波值
- 降维：
PCA->169维
- 训练：  
浅层神经网络
模型文件：pipe_gabor.pkl(joblib读取)


2. 人脸识别
使用AAM模型标记了68个特征点，直接返回特征点。

3. 物体识别
（未完成）
4. 车牌识别
（未完成）
