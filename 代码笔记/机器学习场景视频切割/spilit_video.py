from __future__ import print_function

from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector

import cv2

def build_scenes(video_path):
	#定义re_scene_list 为视频切分场景的列表结果
    re_scene_list = []
    cap = cv2.VideoCapture(video_path)

	#创建一个video_manager指向视频文件
    video_manager = VideoManager([video_path])
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)
    #＃添加ContentDetector算法（构造函数采用阈值等检测器选项）。
    scene_manager.add_detector(ContentDetector())
    base_timecode = video_manager.get_base_timecode()

    try:
        frames_num = cap.get(7)
        # 设置缩减系数以提高处理速度。
        video_manager.set_downscale_factor()

        # 启动 video_manager.
        video_manager.start()

        # 在video_manager上执行场景检测。
        scene_manager.detect_scenes(frame_source=video_manager)

        # 获取检测到的场景列表。
        scene_list = scene_manager.get_scene_list(base_timecode)
        #与FrameTimecodes一样，如果是，则可以对scene_list中的每个场景进行排序
        #场景列表变为未排序。

        print('List of scenes obtained:')
        # print(scene_list)
        #如果scene_list不为空，整理结果列表，否则，视频为单场景
        if scene_list:
            for i, scene in enumerate(scene_list):
                # print('%d , %d' % (scene[0].get_frames(), scene[1].get_frames()))
                re_scene = (scene[0].get_frames(), scene[1].get_frames())
                re_scene_list.append(re_scene)
        else:
            re_scene=(0,frames_num)
            re_scene_list.append(re_scene)
        #输出切分场景的列表结果
        print(re_scene_list)
    finally:
        video_manager.release()
    return re_scene_list

if __name__ == "__main__":
    build_scenes('test.mp4')
