#### 视频场景切割

* 使用软件

  * ###### PySceneDetect

    * 安装

    ~~~
    pip install scenedetect
    ~~~

    * 使用场景进行切割 速度很慢

    ~~~
    scenedetect --input test.mp4  --output test_content  detect-content list-scenes save-images  split-video
    ~~~

    

    * 使用视频阈值进行切割

    ~~~
    scenedetect --input test.mp4 detect-threshold 20 list-scenes save-images  split-video
    ~~~

    

