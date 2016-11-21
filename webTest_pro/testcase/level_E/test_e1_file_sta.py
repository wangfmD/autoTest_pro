# coding=utf-8import sysfrom time import sleepimport unittestfrom selenium import webdriverfrom selenium.common.exceptions import NoAlertPresentException, \    NoSuchElementExceptionfrom _env import addPathsaddPaths('.')import common.init as initfrom common.init import execEnv, loginInfofrom model.baseActionAdd import user_loginfrom model.baseUploadFile import add_UploadVideo, add_videoTask, select_teskList, add_Streamingreload(sys)sys.setdefaultencoding("utf-8")'''添加节目数据'''videoData = [ {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频mp4)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'001.mp4',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '001.mp4',    'sleepTime': '45'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频asf)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'002.asf',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '002.asf',    'sleepTime': '20'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频3gp)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'003.3gp',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '003.3gp',    'sleepTime': '10'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频mpg)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'004.mpg',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '004.mpg',    'sleepTime': '15'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频mov)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'005.mov',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '005.mov',    'sleepTime': '10'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频wmv)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'006.wm',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '006.wmv',    'sleepTime': '10'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频flv)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'007.flv',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '007.flv',    'sleepTime': '45'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频avi)',    'addFileDesc': u'测试备注信息',    'videoType': u'视频',    'fileName': u'008.avi',    'uploadType': 'video',    'disk': 'Z:\\testResource\\py',    'fileNames': '008.avi',    'sleepTime': '10'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档docx)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'001.docx',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '001.docx',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档pptx)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'002.pptx',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '002.pptx',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档ppt)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'003.ppt',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '003.ppt',    'sleepTime': '4'},  {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档xlsx)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'004.xlsx',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '004.xlsx',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档doc)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'005.doc',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '005.doc',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档txt)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'006.txt',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '006.txt',    'sleepTime': '20'},{    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档txt)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'006zh.tx',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '006zh.txt',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档pdf)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'007.pdf',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '007.pdf',    'sleepTime': '4'},      {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名1(文档xls)',    'addFileDesc': u'测试备注信息1',    'videoType': u'文档',    'fileName': u'008.xls',    'uploadType': 'doc',    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '008.xls',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名2(图片)',    'addFileDesc': u'测试备注信息2',    'videoType': u'图片',    'fileName': u'banner01.png',    'uploadType': 'pictrue',    'disk': 'Z:\\testResource\\py\\pic',    'fileNames': 'banner01.png',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名2(图片PNG)',    'addFileDesc': u'测试备注信息2',    'videoType': u'图片',    'fileName': u'banner01.jpg',    'uploadType': 'pictrue',    'disk': 'Z:\\testResource\\py\\pic',    'fileNames': 'banner01.jpg',    'sleepTime': '4'},{    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名2(图片PNG)',    'addFileDesc': u'测试备注信息2',    'videoType': u'图片',    'fileName': u'banner03.jpg',    'uploadType': 'pictrue',    'disk': 'Z:\\testResource\\py\\pic',    'fileNames': 'banner03.jpg',    'sleepTime': '4'},{    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名2(水印)',    'addFileDesc': u'测试备注信息3',    'videoType': u'水印',    'fileName': u'文件名3',    'uploadType': 'watermark',    'disk': 'Z:\\testResource',    'fileNames': '002.PNG',    'sleepTime': '4'}, {    'addTypeSelect': u'公共资源库',    'addFileN': u'测试节目名2(资料)',    'addFileDesc': u'测试备注信息4',    'videoType': u'资料',    'fileName': u'文件名4',    'uploadType': 'data',    'disk': 'Z:\\testResource',    'fileNames': '002.PNG',    'sleepTime': '4'}]'''添加视频任务'''videoTaskData = [{    'taskName': u'测试任务名1',    'taskRemark': u'测试描述',    'pTypeSelect': u'公共资源库',    'addFileN': u'测试节目名(视频)',    'fileName': u'测试文件名',    'fileType': u'视频',    'fileFormat': u'mp4',    'FileDesc': u'测试描述',    'clarity': '720p',    'startTiem': '00:00:01',    'endTiem': '00:00:30'}]'''查询任务列表'''teskListData = [{'taskName': u'测试任务名1'}]'''添加流媒体地址管理'''streamingData = [{'addName': u'19流媒体地址',"ipAdd":init.db_conf["hostadd"],"serverIps":init.streaming_media["serverIps"],"addType":u"内网"}]'''添加节目数据'''contntVideoData = [{    'disk': 'Z:\\testResource\\py',    'fileNames': '001.mp4',    'fileName': '001mp4',    'sleepTime': '45',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '002.asf',    'fileName': '002asf',    'sleepTime': '20',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '003.3gp',    'fileName': '0033gp',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '004.mpg',    'fileName': '004mpg',    'sleepTime': '15',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '005.mov',    'fileName': '005mov',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '006.wmv',    'fileName': '006wmv',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '007.flv',    'fileName': '007flv',    'sleepTime': '45',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '008.avi',    'fileName': '008avi',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'视频管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '001.docx',    'fileName': '001docx',    'sleepTime': '4',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '002.pptx',    'fileName': '002pptx',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '003.ppt',    'fileName': '003ppt',    'sleepTime': '6',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '004.xlsx',    'fileName': '004xlsx',    'sleepTime': '6',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '005.doc',    'fileName': '005doc',    'sleepTime': '6',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '006.txt',    'fileName': '006txt',    'sleepTime': '6',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'},{    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '006zh.txt',    'fileName': '006zhtxt',    'sleepTime': '6',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '007.pdf',    'fileName': '007pdf',    'sleepTime': '6',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'}, {    'disk': 'Z:\\testResource\\py\\wd',    'fileNames': '008.xls',    'fileName': '008xls',    'sleepTime': '6',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'文档管理'},{    'disk': 'Z:\\testResource\\py',    'fileNames': '001.mp4',    'fileName': '001mp4',    'sleepTime': '45',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '002.asf',    'fileName': '002asf',    'sleepTime': '20',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '003.3gp',    'fileName': '0033gp',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '004.mpg',    'fileName': '004mpg',    'sleepTime': '15',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '005.mov',    'fileName': '005mov',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '006.wmv',    'fileName': '006wmv',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '007.flv',    'fileName': '007flv',    'sleepTime': '45',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, {    'disk': 'Z:\\testResource\\py',    'fileNames': '008.avi',    'fileName': '008avi',    'sleepTime': '10',    'gradetype':'小学',    'gradename':'一年级',    'subjectname':'音乐',    'Schapter':'音乐第一章',    'Ssection':'',    'sknow':'',    'remark':'测试描述',    'type_click':'微课管理'}, ]class videoList(unittest.TestCase):    ''''节目上传管理'''    def setUp(self):        if execEnv['execType'] == 'local':            print "\n", "=" * 20, "local exec testcase", "=" * 19            self.driver = webdriver.Chrome()            self.driver.implicitly_wait(8)            self.verificationErrors = []            self.accept_next_alert = True            print "start tenantmanger..."        else:            print "\n", "=" * 20, "remote exec testcase", "=" * 18            browser = webdriver.DesiredCapabilities.CHROME            self.driver = webdriver.Remote(command_executor=execEnv['remoteUrl'], desired_capabilities=browser)            self.driver.implicitly_wait(8)            self.verificationErrors = []            self.accept_next_alert = True            print "start tenantmanger..."    def tearDown(self):        self.driver.quit()        self.assertEqual([], self.verificationErrors)        print "schoolmanager end!"        print "=" * 60            def test_add_Streaming(self):        '''添加流媒体地址管理'''        print "exec：test_add_Streaming..."        driver = self.driver        user_login(driver, **loginInfo)                for itme in streamingData:            add_Streaming(driver, **itme)        sleep(0.5)        print "exec：test_add_Streaming success."    def test_add_video(self):        '''添加节目数据'''        print "exec：test_add_video..."        driver = self.driver        user_login(driver, **loginInfo)                for itme in videoData:            add_UploadVideo(driver, **itme)        sleep(0.5)        print "exec：test_add_video success."            def test_add_contntVideo(self):        '''添加节目数据'''        print "exec：test_add_video..."        driver = self.driver        user_login(driver, **loginInfo)                for itme in contntVideoData:            add_ContntVideo(driver, **itme)        sleep(0.5)        print "exec：test_add_video success."#     def test_add_videoTask(self):#         ''''添加视频任务'''#         print "exec：test_add_videoTask"# #         driver = self.driver#         user_login(driver, **loginInfo)#         for itme in videoTaskData:#             add_videoTask(driver, **itme)#         print "exec: test_add_videoTask success."#         sleep(0.5)# #     def test_search_tesk(self):#         '''查询任务列表'''#         print "exec：test_search_tesk"#         driver = self.driver#         user_login(driver, **loginInfo)#         for itme in teskListData:#             select_teskList(driver, **itme)#         print "exec: test_search_tesk success."#         sleep(0.5)if __name__ == '__main__':    unittest.main()