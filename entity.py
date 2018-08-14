class Result:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class Cat:
    def __init__(self, image_id, url):
        self.image_id = image_id
        self.url = url


# 图片实体类
class Image:
    def __init__(self, time_stamp, tag, url):
        self.time_stamp = time_stamp
        self.tag = tag
        self.url = url
