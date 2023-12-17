import cv2
import numpy as np
import sys

# test 이미지
img = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE)

# 기준 이미지 empire_state_building
dst = cv2.imread("city6.jpg", cv2.IMREAD_GRAYSCALE)

#사진 크기 맞춤
img = cv2.resize(img, (400, 400))
dst = cv2.resize(dst, (400, 400))

# 이미지 전처리
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
edges = cv2.Canny(blurred_img, 30, 100)

# 엣지를 특징점으로 변환
keypoints = np.argwhere(edges > 0)
keypoints = [cv2.KeyPoint(float(x[1]), float(x[0]), 1) for x in keypoints]

# 특징점 추출
orb = cv2.ORB_create()  # 객체생성

keypoints1, desc1 = orb.detectAndCompute(img, None) # 특징점 기술자 정의
keypoints2, desc2 = orb.detectAndCompute(dst, None)

# 특징점 매칭
bfmtacher = cv2.BFMatcher(cv2.NORM_HAMMING)
matching = bfmtacher.knnMatch(desc1, desc2, k=2)

# 최소 거리 비율 설정
ratio = 0.9

# 가장 거리가 작은 기술자만 선택
success_matching = []
for m, n in matching:
    if m.distance < ratio * n.distance:
        success_matching.append(m)

# RANSAC을 이용한 기하학 검증
img2 = np.float32([keypoints1[m.queryIdx].pt for m in success_matching]).reshape(-1, 1, 2)
dst2 = np.float32([keypoints2[m.trainIdx].pt for m in success_matching]).reshape(-1, 1, 2)

# RANSAC 파라미터 설정
ransac_threshold = 4
_, mask = cv2.findHomography(img2, dst2, cv2.RANSAC, ransac_threshold)

# 개수 계산
num = np.sum(mask)

# 검출 여부 확인
num_threshold = 11
if num >= num_threshold:
    print("True")
else:
    print("False")
