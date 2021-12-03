# Links
* awesome human pose estimation : https://github.com/wangzheallen/awesome-human-pose-estimation.git
* CMU Pose Estimation :https://github.com/CMU-Perceptual-Computing-Lab/openpose
* CMU Pose Estimation windows binary download : https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases

* 주의 : pose_iter_584000.caffemodel 파일 필요 아래 링크에서 Download할 것
https://drive.google.com/file/d/15l16KxGsVrCLL2xxdJ6gwc6PiZeWLTCT/view?usp=sharing

## Command
* OpenPoseDemo.exe
```
--video
--write_video
--write_json
--write_images
--num_gpu
--num_gpu_start
--tracking
--number_people_max
--display 0
```
* Example
```
OpenPoseDemo.exe --video  /d/org/2020_0727_133000_001.MP4 --write_video /d/2020_0727_133000_001.avi --write_json .. --num_gpu 1 --num_gpu_start 0   --tracking 10  --number_people_max 1
```
