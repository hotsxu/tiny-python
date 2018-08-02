class Result:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class AppDetailResponse:
    def __init__(self, RT_F, RT_D, PPLC, DATAMAC, APP_TYPE, DTS):
        self.RT_F = RT_F
        self.RT_D = RT_D
        self.PPLC = PPLC
        self.DATAMAC = DATAMAC
        self.APP_TYPE = APP_TYPE
        self.DTS = DTS


class UploadAppDetailResponse:
    def __init__(self, RT_F, RT_D, PPLC, DATAMAC, IS_DEL):
        self.RT_F = RT_F
        self.RT_D = RT_D
        self.PPLC = PPLC
        self.DATAMAC = DATAMAC
        self.IS_DEL = IS_DEL
