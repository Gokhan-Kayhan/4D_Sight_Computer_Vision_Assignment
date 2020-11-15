#Gökhan Kayhan
import cv2

minimum_values=[]

main_image=cv2.imread("StarMap.png",0)
small_image=cv2.imread("Small_area.png",0)
rotated_small=cv2.imread("Small_area_rotated.png",0)

def get_size(input_image):
    
    h,w=(input_image).shape
    rot_center_x=int(w/2)
    rot_center_y=int(h/2)
    return h,w,rot_center_x,rot_center_y


def find_rotation_angle(input_image):
    
    h,w,rot_center_x,rot_center_y = get_size(input_image)

    for i in range(360):
        print(i)
        rotation_matrix = cv2.getRotationMatrix2D( (rot_center_x,rot_center_y),i,1 )
        rotated_image = cv2.warpAffine(input_image,rotation_matrix,(h,w))

        res = cv2.matchTemplate(main_image, rotated_image, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        minimum_values.append(min_val)


    min_value=min(minimum_values)
    print(min_value)
    print("--------------------  ")
    min_index = minimum_values.index(min_value)
    print(min_index)
    print("--------------------  ")

    return min_index


def find_result(input_image):
    
    min_index=find_rotation_angle(input_image)
    h,w,rot_center_x,rot_center_y = get_size(input_image)

    rotation_matrix = cv2.getRotationMatrix2D( (rot_center_x,rot_center_y),min_index,1  )
    rotated_image = cv2.warpAffine(input_image,rotation_matrix,(h,w))

    res = cv2.matchTemplate(main_image, rotated_image, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


    top_left = min_loc 
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(main_image, top_left, bottom_right, 255, 2)

    cv2.imshow("Matched image", main_image)
    cv2.imwrite('output2.png',main_image)
    cv2.waitKey()
    cv2.destroyAllWindows()


find_result(rotated_small)
