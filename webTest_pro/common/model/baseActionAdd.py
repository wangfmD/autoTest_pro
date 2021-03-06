# coding=utf-8
import sys,os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import Select
import win32com.server.util, win32com.client


sys.path.append(os.environ.get('PY_DEV_HOME'))
from webTest_pro.common.initData import init

import SendKeys
import win32con
import win32api
import time

reload(sys)
sys.setdefaultencoding("utf-8")
base_url = init.base_url
loginInfo =init.loginInfo

def admin_login(driver):
    """
    administrator login
    Args: web driver
    -
    Usage: admin_login(driver)

    """
    # open url
    driver.get(base_url + "/middleclient/index.do")
    driver.maximize_window()
    # select platform and login
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('administrator')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('xungejiaoyu')
    # click login btn
    sleep(0.5)
    driver.find_element_by_name('submit').click()
    sleep(0.5)


def user_login(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    print "loginfo:\nuser:{0}，platform:{1}".format(kwargs['username'],
                                                   kwargs['platformname'])
    # open url
    driver.get(base_url + "/middleclient/index.do")
    driver.maximize_window()
    driver.refresh()
    # select platform and login
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        kwargs['platformname'])
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys(kwargs['username'])
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('111111')
    # click login btn
    driver.find_element_by_name('submit').click()
    sleep(0.5)


def add_tenants(driver, **kwargs):
    """
    添加租户
    Args:administrator operate
    -
    Usage: add_tenants(driver)

    """
    print "add tenant info: 河南教育局"
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"租户管理").click()
        sleep(0.5)
        driver.find_element_by_css_selector("i.fa.fa-plus").click()
        sleep(0.5)
        driver.find_element_by_css_selector(
            "#areaId > div.col-sm-9 > input.form-control").click()
        sleep(2)
        # driver.find_element_by_xpath("//div[@id='treeview']/ul/li[17]").click()
        driver.find_element_by_xpath(kwargs["areaid"]).click()
        sleep(2)
        # driver.find_element_by_css_selector("div.modal-content > div.text-center > button.btn.btn-end").click()
        driver.find_element_by_xpath(
            "//*[@id='treeviews']/div/div/div[2]/button[1]").click()
        sleep(1)
        driver.find_element_by_css_selector(
            "#platmarkName > div.col-sm-9 > input.form-control").clear()
        # driver.find_element_by_css_selector("#platmarkName > div.col-sm-9 > input.form-control").send_keys(u"河南教育局")
        driver.find_element_by_css_selector(
            "#platmarkName > div.col-sm-9 > input.form-control").send_keys(
                kwargs["platmarkName"])
        driver.find_element_by_css_selector(
            "#platmarkCode > div.col-sm-9 > input.form-control").clear()
        # driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").send_keys("001")
        driver.find_element_by_css_selector(
            "#platmarkCode > div.col-sm-9 > input.form-control").send_keys(
                kwargs["platmarkCode"])

        sleep(1)
        driver.find_element_by_id("submit").click()
        sleep(1)
        print "add tenant 河南教育局 end."
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['platmarkName']


# schools = [{'schoolName': u'二中', 'schoolType': u'高中', 'schoolArea': u'郑州市'},
#            {'schoolName': u'三中', 'schoolType': u'中学', 'schoolArea': u'郑州市'},
#            {'schoolName': u'四中', 'schoolType': u'中学', 'schoolArea': u'开封市'},
#            {'schoolName': u'五中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
#            {'schoolName': u'六中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
#            {'schoolName': u'一中', 'schoolType': u'高中', 'schoolArea': u'郑州市'}]

schools = [{
    'schoolName': u'二中',
    'schoolType': u'高中',
    'schoolArea': u'郑州市'
}, {
    'schoolName': u'三中',
    'schoolType': u'中学',
    'schoolArea': u'郑州市'
}]


def add_schools(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:schoolName,schoolType,schoolArea
    '''添加学校'''

    print "添加学校信息：{0}，{1}，{2}".format(
        kwargs['schoolName'], kwargs['schoolType'], kwargs['schoolArea'])

    driver.refresh()
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()

    # select area
    driver.find_element_by_id("choosearea").click()
    sleep(1)
    driver.find_element_by_xpath("//div[@id='treeview']/ul/li").click()
    driver.find_element_by_css_selector(
        "div.col-sm-9.text-center > #submit").click()

    sleep(1)
    # 添加学校btn
    driver.find_element_by_xpath("//*[@id='addSchool']").click()
    sleep(1)
    # 输入学校
    driver.find_element_by_xpath("//*[@id='schoolName']/div/input").clear()
    driver.find_element_by_xpath("//*[@id='schoolName']/div/input").send_keys(
        kwargs['schoolName'])
    # 选择学校类型
    Select(driver.find_element_by_css_selector(
        "select.form-control")).select_by_visible_text(kwargs['schoolType'])
    # 学校选择区域
    # Select(driver.find_element_by_xpath("//div[@id='areaSelect']/select[2]")).select_by_visible_text(kwargs['schoolArea'])
    # //div[@id='schoolTypeId']/div/select
    # click确定
    driver.find_element_by_xpath("//button[@id='submit']").click()
    # self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
    sleep(2)
    print "添加：%s 成功。" % kwargs['schoolName']

    # print "添加：%s 失败。" % kwargs['schoolName']


classromms = [{
    'className': '31className',
    'classAccNumber': '1'
}, {
    'className': '32className',
    'classAccNumber': '1'
}]


def add_classrooms(driver, **kwargs):
    """
    添加教室组
    Args:
    -
    Usage:

    """
    # para:
    print "add info:{0},{1}".format(kwargs['className'],
                                    kwargs['classAccNumber'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"学校管理").click()
        sleep(1)
        # click add btn
        driver.find_element_by_css_selector(u"a[title=\"添加教室\"] > span").click(
        )
        sleep(0.5)
        # operation
        driver.find_element_by_css_selector(
            "#className > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "#className > div.col-sm-9 > input.form-control").send_keys(kwargs[
                'className'])
        driver.find_element_by_css_selector(
            "#classAccNumber > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "#classAccNumber > div.col-sm-9 > input.form-control").send_keys(
                kwargs['classAccNumber'])
        # click 确定
        driver.find_element_by_xpath("(//button[@id='submit'])[3]").click()
        # driver.find_element_by_css_selector(
        #     "css=#classroommodal > div.modal-dialog > div.modal-content > form.form-horizontal > div.modal-body.row > div.form-group > div.col-sm-9 > #submit")
        sleep(1)
        print "add {} end.".format(kwargs['className'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['className'])


integrateds = [{
    'className': '32className',
    'equipment_name': '81lb',
    'ipAddr': '10.1.0.81',
    'locAddr': '10.1.0.81',
    'equipmentLogName': 'admin',
    'equipmentLogPwd': 'admin'
}, {
    'className': '31className',
    'equipment_name': '82lb',
    'ipAddr': '10.1.0.82',
    'locAddr': '10.1.0.81',
    'equipmentLogName': 'admin',
    'equipmentLogPwd': 'admin'
}]

terminals = [{
    'equipmentModel': u'Group系列',
    'className': u'81教室',
    'equipment_name': '81lb',
    'ipAddr': '10.1.0.81',
    'locAddr': '10.1.0.81',
    'equipmentLogName': 'admin',
    'equipmentLogPwd': 'admin'
}, {
    'equipmentModel': u'Group系列',
    'className': u'82教室',
    'equipment_name': '82lb',
    'ipAddr': '10.1.0.82',
    'locAddr': '10.1.0.81',
    'equipmentLogName': 'admin',
    'equipmentLogPwd': 'admin'
}]


def add_terminals(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:       {'equipmentModel': u'Group系列',
    #  'classroom': '32className',
    #       'equipment_name': '81lb',
    #       'ipAddr': '10.1.0.81',
    #       'locAddr': '10.1.0.81',
    #       'equipmentLogName': 'admin',
    #       'equipmentLogPwd': 'admin'},
    '''添加一个终端'''
    print "add info:{0},{1}".format(kwargs['equipment_name'],
                            kwargs['className'])
    # refresh main page

    driver.refresh()

    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"学校管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"教室列表").click()
    sleep(1)
    driver.find_element_by_link_text(kwargs['className']).click()
    sleep(1)
    # driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
    driver.find_element_by_xpath(u"(//a[contains(text(),'设备管理')])[2]").click()
    sleep(1)
    # click add btn
    driver.find_element_by_id("addterminal").click()
    sleep(1)
    # operation
    driver.find_element_by_css_selector(
    "div.modal-body > div > #name > div.col-sm-9 > input.form-control"
    ).clear()
    driver.find_element_by_css_selector(
    "div.modal-body > div > #name > div.col-sm-9 > input.form-control"
    ).send_keys(kwargs['equipment_name'])
    Select(
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentModel > div.col-sm-9 > select"
    )).select_by_visible_text(kwargs['equipmentModel'])
    driver.find_element_by_css_selector(
    "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control"
    ).clear()
    driver.find_element_by_css_selector(
    "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control"
    ).send_keys(kwargs['ipAddr'])
    driver.find_element_by_css_selector(
    "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control"
    ).clear()
    driver.find_element_by_css_selector(
    "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control"
    ).send_keys(kwargs['locAddr'])
    driver.find_element_by_css_selector(
    "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control"
    ).clear()
    driver.find_element_by_css_selector(
    "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control"
    ).send_keys(kwargs['equipmentLogName'])
    driver.find_element_by_css_selector(
    "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control"
    ).clear()
    driver.find_element_by_css_selector(
    "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control"
    ).send_keys(kwargs['equipmentLogPwd'])
    # click OK
    driver.find_element_by_css_selector(
    "#terminal > div.modal-dialog > div.modal-content > #formrole > div.modal-body > div.text-center > #submit"
    ).click()
    sleep(1)
    print "add {} end.".format(kwargs['equipment_name'])
    # except Exception as e:
    #     print e
    #     print "add {} failed.".format(kwargs['equipment_name'])


def add_integrateds(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:
    """
    # para:
    '''添加一体机'''
    print "add info:{0},{1}".format(kwargs['equipment_name'],
                                    kwargs['className'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"学校管理").click()
        driver.find_element_by_link_text(u"教室列表").click()
        sleep(1)
        driver.find_element_by_link_text(kwargs['className']).click()
        sleep(1)
        # 2060bug页面修改
        # driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'设备管理')])[2]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_id("addIntegrated").click()
        sleep(0.5)
        # operation
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #name > div.col-sm-9 > input.form-control"
        ).clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #name > div.col-sm-9 > input.form-control"
        ).send_keys(kwargs['equipment_name'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #ipAddr > div.col-sm-9 > input.form-control"
        ).clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #ipAddr > div.col-sm-9 > input.form-control"
        ).send_keys(kwargs['ipAddr'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #locAddr > div.col-sm-9 > input.form-control"
        ).clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #locAddr > div.col-sm-9 > input.form-control"
        ).send_keys(kwargs['locAddr'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogName > div.col-sm-9 > input.form-control"
        ).clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogName > div.col-sm-9 > input.form-control"
        ).send_keys(kwargs['equipmentLogName'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogPwd > div.col-sm-9 > input.form-control"
        ).clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogPwd > div.col-sm-9 > input.form-control"
        ).send_keys(kwargs['equipmentLogPwd'])
        # click 确定
        driver.find_element_by_css_selector(
            "#Integrated > div.modal-dialog > div.modal-content > #formrole > div.modal-body.row > div.text-center > #submit"
        ).click()
        sleep(1)
        print "add {} end.".format(kwargs['equipment_name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['equipment_name'])


subjectsGroups = [{
    'groupName': u'计算机',
    'groupCode': '001',
    'description': u'计算机'
}, {
    'groupName': u'计算机1',
    'groupCode': '002',
    'description': u'计算机'
}]


def add_groupsubGrps(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:
    '''添加教室组'''
    print "add info:{0},{1}".format(kwargs['groupName'], kwargs['groupCode'],
                                    kwargs['description'])
    # refresh main page
    driver.refresh()
    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"组管理").click()
    sleep(1)
    # click add btn
    driver.find_element_by_xpath("//a[@id='addscgroup']").click()
    sleep(0.5)
    # operation
    driver.find_element_by_xpath("//*[@id='groupName']/div/input").clear()
    driver.find_element_by_xpath("//*[@id='groupName']/div/input").send_keys(
        kwargs['groupName'])
    driver.find_element_by_xpath("//*[@id='groupCode']/div/input").clear()
    driver.find_element_by_xpath("//*[@id='groupCode']/div/input").send_keys(
        kwargs['groupCode'])
    driver.find_element_by_xpath("//*[@id='description']/div/textarea").clear()
    driver.find_element_by_xpath(
        "//*[@id='description']/div/textarea").send_keys(kwargs['description'])
    # click 确定
    driver.find_element_by_xpath("//button[@id='submit']").click()
    sleep(1)
    print "add {} end.".format(kwargs['groupName'])

    # print "add {} failed.".format(kwargs[''])


users = [{
    'loginName': 'user',
    'trueName': 'teacher'
}, {
    'loginName': 'user1',
    'trueName': 'teacher1'
}, {
    'loginName': 'user2',
    'trueName': 'teacher2'
}, {
    'loginName': 'user3',
    'trueName': 'teacher3'
}, {
    'loginName': 'user4',
    'trueName': 'teacher4'
}]


def add_users(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # pra: loginName, trueName
    '''添加用户'''
    print "添加用户的信息：{0},{1}".format(kwargs['loginName'], kwargs['trueName'])
    try:
        # driver.find_element_by_css_selector("#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"用户列表").click()
        driver.find_element_by_id("adduserlist").click()
        sleep(1)
        driver.find_element_by_name("loginName").clear()
        driver.find_element_by_name("loginName").send_keys(kwargs['loginName'])
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("111111")
        driver.find_element_by_name("passwords").clear()
        driver.find_element_by_name("passwords").send_keys("111111")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("13700010001")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("user@3bu.cn")
        driver.find_element_by_name("trueName").clear()
        driver.find_element_by_name("trueName").send_keys(kwargs['trueName'])
        driver.find_element_by_id("determine").click()
        sleep(1)
        print "添加用户{0}成功。".format(kwargs['trueName'])
    except Exception as e:
        print "添加用户{0}失败。".format(kwargs['trueName'])
        print e


def add_userswithschool(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # pra: loginName, trueName
    '''添加用户'''
    print "添加用户的信息：{0},{1}".format(kwargs['loginName'], kwargs['trueName'])
    try:
        # driver.find_element_by_css_selector("#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"用户列表").click()
        driver.find_element_by_id("adduserlist").click()
        sleep(1)
        driver.find_element_by_name("loginName").clear()
        driver.find_element_by_name("loginName").send_keys(kwargs['loginName'])
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("111111")
        driver.find_element_by_name("passwords").clear()
        driver.find_element_by_name("passwords").send_keys("111111")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("13700010001")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("user@3bu.cn")
        driver.find_element_by_name("trueName").clear()
        driver.find_element_by_name("trueName").send_keys(kwargs['trueName'])
        driver.find_element_by_id("determine").click()
        sleep(1)
        print "添加用户{0}成功。".format(kwargs['trueName'])
    except Exception as e:
        print "添加用户{0}失败。".format(kwargs['trueName'])
        print e


roles = [{
    'roleName': 'a2role19',
    'roleCode': '000',
    'description': 'comment role'
}, {
    'roleName': 'a2role11',
    'roleCode': '000',
    'description': 'comment role'
}, {
    'roleName': 'a2role31',
    'roleCode': '000',
    'description': 'comment role'
}, {
    'roleName': 'a2role41',
    'roleCode': '000',
    'description': 'comment role'
}, {
    'roleName': 'a2role21',
    'roleCode': '000',
    'description': 'comment role'
}, {
    'roleName': 'arole51',
    'roleCode': '000',
    'description': 'comment role'
}, {
    'roleName': 'a2role61',
    'roleCode': '000',
    'description': 'comment role'
}, {
    'roleName': 'a2role71',
    'roleCode': '000',
    'description': 'comment role'
}]


def add_roles(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para: driver,roleName, roleCode, description
    '''添加角色'''
    print "添加的角色信息：{0},{1},{2}".format(kwargs['roleName'], kwargs['roleCode'],
                                       kwargs['description'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"角色管理").click()
        sleep(0.5)

        # click addrole button
        driver.find_element_by_xpath("//a[@id='addrole']").click()
        sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='roleName']").clear()
        driver.find_element_by_xpath(".//*[@id='roleName']").send_keys(kwargs[
            'roleName'])
        driver.find_element_by_xpath(".//*[@id='roleCode']").clear()
        driver.find_element_by_xpath(".//*[@id='roleCode']").send_keys(kwargs[
            'roleCode'])
        driver.find_element_by_xpath(".//*[@id='description']").clear()
        driver.find_element_by_xpath(".//*[@id='description']").send_keys(
            kwargs['description'])
        driver.find_element_by_xpath(".//*[@id='insertrole']").click()
        sleep(1)
        print "添加角色{}成功。".format(kwargs['roleName'])
    except Exception as e:
        print e
        print "添加角色{}失败。".format(kwargs['roleName'])


interactgrps = [{
    'grpName': 'grp1',
    'schoolgrTypeId': u'课程组'
}, {
    'grpName': 'grp2',
    'schoolgrTypeId': u'会议组'
}, {
    'grpName': 'grp3',
    'schoolgrTypeId': u'会议组'
}]


def add_interactgrps(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:grpName,schoolgrTypeId
    '''添加教室组'''
    print "add info:{0},{1}".format(kwargs['grpName'],
                                    kwargs['schoolgrTypeId'])

    try:
        # refresh main page
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"互动组管理").click()
        sleep(0.5)

        # click add btn
        driver.find_element_by_xpath("//button[@id='addSchool']").click()
        sleep(0.5)
        # //*[@id='schoolName']/div/input
        # operation
        driver.find_element_by_xpath(
            "//div[@id='schoolName']/div/input").clear()
        driver.find_element_by_xpath(
            "//div[@id='schoolName']/div/input").send_keys(kwargs['grpName'])
        Select(
            driver.find_element_by_xpath("//div[@id='schoolTypeId']/div/select"
                                         )).select_by_visible_text(kwargs[
                                             'schoolgrTypeId'])
        # //*[@id='schoolTypeId']/div/select
        # click 确定
        driver.find_element_by_xpath("//button[@id='submit']").click()
        # driver.find_element_by_xpath("//*[@id='submit']").click()
        sleep(1)
        print "add {} end.".format(kwargs['grpName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['grpName'])


subjects = [{
    'subjectName': u'书法',
    'description': u'学习中国文化'
}, {
    'subjectName': u'计算机',
    'description': u'计算机基础应用'
}]


def add_subjects(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:
    '''添加科目'''
    print "add info:{0},{1}".format(kwargs['subjectName'],
                                    kwargs['description'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"科目管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addsubject']").click()
        # //*[@id='addsubject']
        sleep(0.5)

        # operation
        driver.find_element_by_xpath("//input[@id='subjectName']").clear()
        driver.find_element_by_xpath("//input[@id='subjectName']").send_keys(
            kwargs['subjectName'])
        driver.find_element_by_xpath("//*[@id='description']").clear()
        driver.find_element_by_xpath("//*[@id='description']").send_keys(
            kwargs["description"])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertsubject']").click()
        sleep(1)
        print "add {} end.".format(kwargs['subjectName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['subjectName'])


chapters = [{
    'gradeid': u"二年级",
    'subjectid': u"数学",
    'chapterName': u'第一章a',
    'chapterCode': u'助记码1'
}, {
    'gradeid': u"二年级",
    'subjectid': u"数学",
    'chapterName': u'第一章b',
    'chapterCode': u'助记码1'
}]


def add_chapters(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:
    '''添加章'''
    print "add info:{0},{1},{2},{3}".format(
        kwargs['gradeid'], kwargs['subjectid'], kwargs['chapterName'],
        kwargs['chapterCode'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"章管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addchapter']").click()
        sleep(0.5)

        # operation
        Select(driver.find_element_by_xpath("//select[@id='gradeid']")
               ).select_by_visible_text(kwargs['gradeid'])
        Select(driver.find_element_by_xpath("//select[@id='subjectid']")
               ).select_by_visible_text(kwargs['subjectid'])
        driver.find_element_by_xpath("//input[@id='chapterName']").clear()
        driver.find_element_by_xpath("//input[@id='chapterName']").send_keys(
            kwargs['chapterName'])
        driver.find_element_by_xpath("//input[@id='chapterCode']").clear()
        driver.find_element_by_xpath("//input[@id='chapterCode']").send_keys(
            kwargs['chapterCode'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertchapter']").click()
        sleep(1)
        print "add {} end.".format(kwargs['chapterName'])

    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['chapterName'])


sections = [{
    'gradeid': u"二年级",
    'subjectid': u"数学",
    'chapterid': "zmc11",
    'sectionName': u"第一节",
    'sectionCode': u"第一节zjm"
}, {
    'gradeid': u"二年级",
    'subjectid': u"数学",
    'chapterid': "zmc11",
    'sectionName': u"第二节",
    'sectionCode': u"第二节zjm"
}]


def add_sections(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:
    '''添加节'''
    print "add info:{0},{1},{2},{3},{4}".format(
        kwargs['gradeid'], kwargs['subjectid'], kwargs['chapterid'],
        kwargs['sectionName'], kwargs['sectionCode'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"节管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addsection']/i").click()
        sleep(0.5)

        # operation
        Select(driver.find_element_by_xpath("//select[@id='gradeid']")
               ).select_by_visible_text(kwargs['gradeid'])
        Select(driver.find_element_by_xpath("//select[@id='subjectid']")
               ).select_by_visible_text(kwargs['subjectid'])
        Select(driver.find_element_by_xpath("//select[@id='chapterid']")
               ).select_by_visible_text(kwargs['chapterid'])
        driver.find_element_by_xpath("//input[@id='sectionName']").clear()
        driver.find_element_by_xpath("//input[@id='sectionName']").send_keys(
            kwargs['sectionName'])
        driver.find_element_by_xpath("//input[@id='sectionCode']").clear()
        driver.find_element_by_xpath("//input[@id='sectionCode']").send_keys(
            kwargs['sectionCode'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertsection']").click()
        sleep(1)
        print "add {} end.".format(kwargs['sectionName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['sectionName'])


knowledges = [{
    'gradeid': u'六年级/小学',
    'subjectid': u'自然科学',
    'chapterid': u'第二章',
    'sectionid': u"第二节",
    'knowledgeName': u"双细胞",
    'knowledgeCode': u"双细胞1"
}, {
    'gradeid': u'六年级/小学',
    'subjectid': u'自然科学',
    'chapterid': u'第二章',
    'sectionid': u"第二节",
    'knowledgeName': u"多细胞",
    'knowledgeCode': u"多细胞1"
}]


def add_knowledges(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:
    '''添加知识点'''
    print "add info:{0},{1}".format(kwargs['knowledgeName'],
                                    kwargs['subjectid'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"知识点管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addknowledge']").click()
        sleep(0.5)

        # operation
        Select(driver.find_element_by_xpath("//select[@id='gradeid']")
               ).select_by_visible_text(kwargs['gradeid'])
        Select(driver.find_element_by_xpath("//select[@id='subjectid']")
               ).select_by_visible_text(kwargs['subjectid'])
        Select(driver.find_element_by_xpath("//select[@id='chapterid']")
               ).select_by_visible_text(kwargs['chapterid'])
        Select(driver.find_element_by_xpath("//select[@id='sectionid']")
               ).select_by_visible_text(kwargs['sectionid'])
        driver.find_element_by_xpath("//input[@id='knowledgeName']").clear()
        driver.find_element_by_xpath("//input[@id='knowledgeName']").send_keys(
            kwargs['knowledgeName'])
        driver.find_element_by_xpath("//input[@id='knowledgeCode']").clear()
        driver.find_element_by_xpath("//input[@id='knowledgeCode']").send_keys(
            kwargs['knowledgeCode'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertknowledge']").click()
        sleep(1)
        print "add {} end.".format(kwargs['knowledgeName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['knowledgeName'])


MCUequipments = [{
    'equipmentName': '85mcu',
    'equipIpAddr': '10.1.0.85',
    'mcu_port': '80',
    'mcuLoginName': 'POLYCOM',
    'mcuPasswd': 'POLYCOM'
}, {
    'equipmentName': '95mcu',
    'equipIpAddr': '10.1.0.95',
    'mcu_port': '10000',
    'mcuLoginName': 'POLYCOM',
    'mcuPasswd': 'POLYCOM'
}]


def add_MCUequipments(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:equipmentName，equipIpAddr，mcu_port，mcuLoginName，mcuPasswd
    '''添加mcu'''
    print "add info:{0},{1},{2},{3}".format(
        kwargs['equipmentName'], kwargs['equipIpAddr'], kwargs['mcuLoginName'],
        kwargs['mcuPasswd'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)

        # click add btn
        sleep(1)
        driver.find_element_by_css_selector("i.fa.fa-plus").click()
        sleep(1)
        driver.find_element_by_id("mcuAreaName").click()
        sleep(0.5)

        # operation
        driver.find_element_by_css_selector(
            "li.list-group-item.node-treeview").click()
        sleep(1)
        driver.find_element_by_id("equipmentName").clear()
        driver.find_element_by_id("equipmentName").send_keys(kwargs[
            'equipmentName'])
        driver.find_element_by_id("equipIpAddr").clear()
        driver.find_element_by_id("equipIpAddr").send_keys(kwargs[
            'equipIpAddr'])
        driver.find_element_by_id("mcu_port").clear()
        driver.find_element_by_id("mcu_port").send_keys(kwargs['mcu_port'])
        driver.find_element_by_id("mcuLoginName").clear()
        driver.find_element_by_id("mcuLoginName").send_keys(kwargs[
            'mcuLoginName'])
        driver.find_element_by_id("mcuPasswd").clear()
        driver.find_element_by_id("mcuPasswd").send_keys(kwargs['mcuPasswd'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='submit']").click()
        sleep(1)
        print "add {} end.".format(kwargs['equipmentName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['equipmentName'])


def conf_drivers_child(driver):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # driver = webdriver.Chrome()
    # user_login(driver, 'hnsadmin', u"河南教育局")
    driver.refresh()
    driver.find_element_by_link_text(u"设备管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"中心设备").click()
    sleep(1)
    # 点击MCU管理区域按键
    driver.find_element_by_xpath("(//button[@id='current'])[2]").click()
    sleep(1)
    # 选择区域
    driver.find_element_by_xpath(
        "//div[@id='AreaMcutreeview']/ul/li/span[3]").click()

    sleep(1)
    # save区域
    driver.find_element_by_id("saveAreaMcu").click()
    sleep(1)
    driver.find_element_by_id("xiaoximiddleware").click()
    sleep(1)
    # 选择消息中间件
    driver.find_element_by_xpath(
        "//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
    # //table[@id='middlewaretable']/tbody/tr/td[2]
    sleep(1)
    # failed 1
    driver.find_element_by_css_selector("i.fa.fa-server").click()
    sleep(1)
    # save
    driver.find_element_by_name("ckrelevmcuid").click()
    sleep(1)
    driver.find_element_by_id("saverelevmcumiddleware").click()
    sleep(1)
    # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()  # 选择interact
    # 选择消息中间件管理mcu的时间较长
    sleep(12)
    # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
    driver.find_element_by_css_selector("i.fa.fa-bars").click()
    sleep(1)
    driver.find_element_by_css_selector(
        "#listofschooltable > tr > td > input[type=\"checkbox\"]").click()
    sleep(1)
    driver.find_element_by_id("insertmiddlewareschool").click()
    sleep(1)
    # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
    # sleep(1)
    # driver.find_element_by_id("theschoollist").click()


def conf_drivers_local(driver):
    """
    Func desc: cfg the center interact manager mcu and school
    Args:
    -
    Usage:

    """
    # driver = webdriver.Chrome()
    # user_login(driver, 'hnsadmin', u"河南教育局")
    driver.refresh()
    driver.find_element_by_link_text(u"设备管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"中心设备").click()
    sleep(1)
    # 点击MCU管理区域按键
    driver.find_element_by_xpath("(//button[@id='current'])[2]").click()
    sleep(1)
    # 选择区域
    driver.find_element_by_xpath(
        "//div[@id='AreaMcutreeview']/ul/li/span[3]").click()

    sleep(1)
    # save区域
    driver.find_element_by_id("saveAreaMcu").click()
    sleep(1)
    driver.find_element_by_id("xiaoximiddleware").click()
    sleep(1)
    # 选择消息中间件
    # //table[@id='middlewaretable']/tbody/tr/td[2]  第一个
    # //table[@id='middlewaretable']/tbody/tr[2]/td[2] 第二个
    driver.find_element_by_xpath(
        "//table[@id='middlewaretable']/tbody/tr/td[2]").click()
    sleep(1)
    # 关联MCU
    driver.find_element_by_css_selector("i.fa.fa-server").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@name='ckrelevmcuid']").click()
    sleep(1)
    driver.find_element_by_xpath("(//input[@name='ckrelevmcuid'])[2]").click()
    sleep(1)
    # 点击确定
    driver.find_element_by_id("saverelevmcumiddleware").click()
    sleep(1.5)
    # 关联school
    driver.find_element_by_css_selector("i.fa.fa-bars").click()
    sleep(1)
    driver.find_element_by_xpath("//tbody[@id='listofschooltable']/tr/td/input").click()
    sleep(1)
    driver.find_element_by_xpath("//tbody[@id='listofschooltable']/tr[2]/td/input").click()
    sleep(1)
    # 点击确定
    driver.find_element_by_id("insertmiddlewareschool").click()
    sleep(2)
    ###############
    # driver.find_element_by_css_selector("i.fa.fa-server").click()
    # sleep(1)
    # driver.find_element_by_name("ckrelevmcuid").click()
    # sleep(1)
    # # save
    # driver.find_element_by_id("saverelevmcumiddleware").click()
    # # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()  # 选择interact
    # # 选择消息中间件管理mcu的时间较长
    # sleep(2)
    # # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
    # driver.find_element_by_css_selector("i.fa.fa-bars").click()
    # sleep(1)
    # driver.find_element_by_css_selector(
    #     "#listofschooltable > tr > td > input[type=\"checkbox\"]").click()
    # sleep(1)
    # driver.find_element_by_id("insertmiddlewareschool").click()
    ###################

    # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
    # sleep(1)
    # driver.find_element_by_id("theschoollist").click()


interacts = [{
    'host': '10.1.0.2',
    'port': '80',
    'username': 'administrator',
    'password': 'xungejiaoyu'
}, {
    'host': '10.1.0.3',
    'port': '80',
    'username': 'administrator',
    'password': 'xungejiaoyu'
}]


def add_interacts(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:host,port,username,password
    '''添加消息中间件'''
    print "add info:{0},{1},{2},{3}".format(
        kwargs['host'], kwargs['port'], kwargs['username'], kwargs['password'])
    # refresh main page
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)
        driver.find_element_by_id("xiaoximiddleware").click()
        sleep(1)
        driver.find_element_by_css_selector(
            "#addmiddleware > i.fa.fa-plus").click()
        sleep(1)
        driver.find_element_by_id("host").clear()
        driver.find_element_by_id("host").send_keys(kwargs['host'])
        driver.find_element_by_id("port").clear()
        driver.find_element_by_id("port").send_keys(kwargs['port'])
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(kwargs['username'])
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(kwargs['password'])
        sleep(0.5)
        driver.find_element_by_id("insertmiddleware").click()
        sleep(1)

        print "add {} end.".format(kwargs['host'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['host'])


def conf_interact_local(driver, interactaddr):
    """
    Func desc:local interactmgr platform config
    Args:
    -
    Usage:

    """
    # open url
    driver.get("http://" + interactaddr + "/interact/login.do")
    driver.maximize_window()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("administrator")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("xungejiaoyu")
    sleep(1)
    driver.find_element_by_id("buttlogin").click()
    sleep(2)
    driver.find_element_by_id("sysconfig").click()
    sleep(1)
    # failed 1
    driver.find_element_by_xpath(
        "//table[@id='table']/tbody/tr[2]/td[3]/a/i").click()
    sleep(1)
    driver.find_element_by_id("value").clear()
    driver.find_element_by_id("value").send_keys(interactaddr)
    driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    sleep(1)
    driver.find_element_by_id("sysmiddlewarelocal").click()
    sleep(1)
    driver.find_element_by_id("addLocal").click()  # 获取消息中间件
    sleep(1)
    driver.find_element_by_xpath("(//input[@name='text'])").click()
    sleep(1)
    driver.find_element_by_id("determines").click()
    sleep(2)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"设为本地连接中间件\"]").click()
    sleep(2.5)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"手动连接中间件\"]").click()
    sleep(6)
    try:
        driver.switch_to_alert().accept()
    except NoAlertPresentException as e:
        print e
    sleep(1)


def conf_child_interact(driver, interactaddr, serveraddr):
    """
    Func desc:child interactmgr platform config
    Args:
    -
    Usage:

    """
    #     //tbody[@id='selectLocal']/tr/td     //input[@name='text']              //tbody[@id='selectLocal']/tr/td[4]/input     10.1.0.45
    #     //tbody[@id='selectLocal']/tr[2]/td  xpath=(//input[@name='text'])[2]    //tbody[@id='selectLocal']/tr[2]/td[4]/input  10.1.0.56

    driver.get("http://" + interactaddr + "/interact/login.do")
    driver.maximize_window()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("administrator")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("xungejiaoyu")
    sleep(1)
    driver.find_element_by_id("buttlogin").click()
    sleep(1)
    driver.find_element_by_id("sysconfig").click()
    sleep(1)
    driver.find_element_by_xpath(
        "//table[@id='table']/tbody/tr[2]/td[3]/a/i").click()
    sleep(1)
    driver.find_element_by_id("value").clear()
    driver.find_element_by_id("value").send_keys(serveraddr)
    driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    sleep(1)
    driver.find_element_by_id("sysmiddlewarelocal").click()
    sleep(1)
    # 选择消息中间件弹出页面btn
    driver.find_element_by_id("addLocal").click()
    sleep(1)
    firstIpPageText = driver.find_element_by_xpath(
        "//tbody[@id='selectLocal']/tr/td ").text
    secondIpPageText = driver.find_element_by_xpath(
        "//tbody[@id='selectLocal']/tr[2]/td").text
    print firstIpPageText, secondIpPageText
    sleep(1)
    # 配置本地消息中间件
    if firstIpPageText == interactaddr:
        driver.find_element_by_xpath("//input[@name='text']").click()
        sleep(0.5)
        driver.find_element_by_id("determines").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_css_selector(
            u"button[title=\"设为本地连接中间件\"]").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_css_selector(
            u"button[title=\"手动连接中间件\"]").click()
        sleep(6)
        driver.switch_to_alert().accept()

        sleep(2)
    elif secondIpPageText == interactaddr:
        driver.find_element_by_xpath("(//input[@name='text'])[2]").click()
        sleep(0.5)
        driver.find_element_by_id("determines").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_css_selector(
            u"button[title=\"设为本地连接中间件\"]").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_css_selector(
            u"button[title=\"手动连接中间件\"]").click()
        sleep(6)
        driver.switch_to_alert().accept()
    else:
        print "non-existent:{} local interact".format(interactaddr)

    driver.find_element_by_id("addLocal").click()
    sleep(1)
    firstIpPageText = driver.find_element_by_xpath(
        "//tbody[@id='selectLocal']/tr/td ").text
    secondIpPageText = driver.find_element_by_xpath(
        "//tbody[@id='selectLocal']/tr[2]/td").text
    print firstIpPageText, secondIpPageText
    if firstIpPageText == serveraddr:
        driver.find_element_by_xpath("//input[@name='text']").click()
        sleep(0.5)
        driver.find_element_by_id("determines").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_xpath(
            "//tbody[@id='localQuery']/tr[2]/th[8]/button[4]").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_xpath(
            "//tbody[@id='localQuery']/tr[2]/th[8]/button[2]").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(4)
    elif secondIpPageText == serveraddr:
        driver.find_element_by_xpath("(//input[@name='text'])[2]").click()
        sleep(0.5)
        driver.find_element_by_id("determines").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_xpath(
            "//tbody[@id='localQuery']/tr[2]/th[8]/button[4]").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.find_element_by_xpath(
            "//tbody[@id='localQuery']/tr[2]/th[8]/button[2]").click()
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(4)
    else:
        print "non-existent:{} middle interact".format(serveraddr)


hdk_lesson_cfgs = [{'name': u'互动课模板'}, {'name': u'互动课模板480p'}]
jp_lesson_cfgs = [{'name': u'精品课'}, {'name': u'精品课480p'}]
conference_cfgs = [{'name': u'会议'}, {'name': u'会议480p'}]
speaker_lesson_cfgs = [{'name': u'主讲下课'}, {'name': u'主讲下课_1'}]
listener_lesson_cfgs = [{'name': u'听讲下课'}, {'name': u'听讲下课_1'}]


def add_cfg_listener_lessons(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:name
    '''添加听讲下课模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_link_text(u"听课下课").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addlisteningclass']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[7]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[7]").send_keys(
            kwargs['name'])
        # click 确定
        driver.find_element_by_xpath(
            "//button[@id='insertlectureclass']").click()
        sleep(1)
        print "add {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_speaker_lessons(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:name
    '''添加主讲下课模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_link_text(u"主讲下课").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addlectureclass']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[7]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[7]").send_keys(
            kwargs['name'])
        # click 确定
        driver.find_element_by_id("insertlectureclass").click()
        sleep(1)
        print "add {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_conferences(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:name
    '''添加会议模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(
            u"(//a[contains(text(),'视频会议')])[2]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addvideoconference']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[5]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[5]").send_keys(
            kwargs['name'])
        # click 确定
        driver.find_element_by_xpath(
            "//button[@id='insertvideoconference']").click()
        sleep(1)
        print "add {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_jpks(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:name
    '''添加精品课模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(
            u"(//a[contains(text(),'精品课堂')])[2]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addexcellentclass']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[3]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[3]").send_keys(
            kwargs['name'])
        # click 确定
        driver.find_element_by_xpath(
            "//button[@id='insertexcellentclass']").click()
        sleep(1)
        print "add {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_hdks(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:name
    '''添加互动模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(
            u"(//a[contains(text(),'精品课堂')])[2]").click()
        sleep(1)
        driver.find_element_by_xpath(
            u"(//a[contains(text(),'互动教学')])[2]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addinteractteach']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("//input[@id='name']").clear()
        driver.find_element_by_xpath("//input[@id='name']").send_keys(kwargs[
            'name'])
        # click 确定
        driver.find_element_by_xpath(
            "//button[@id='insertinteractteach']").click()
        sleep(1)
        print "add {} end.".format(kwargs['name'])
    except NoSuchElementException as e:
        print e
        print "add {} failed.".format(kwargs['name'])


emails = [{
    'smtp': 'smtp.162.com',
    'fromName': 'haosea@qq.com',
    'password': '111111'
}, {
    'smtp': 'smtp.163.com',
    'fromName': 'haosea1@qq.com',
    'password': '111111'
}]


def add_emails(driver, **kwargs):
    """
    Func desc
    Args:
    -
    Usage:

    """
    # para:
    '''添加邮箱服务'''
    print "add info:{0},{1},{2}".format(kwargs['smtp'], kwargs['fromName'],
                                        kwargs['password'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"邮箱服务管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath(
            "//button[@id='add_email_setting']").click()
        sleep(0.5)

        # operation
        driver.find_element_by_xpath("//input[@id='smtp']").clear()
        driver.find_element_by_xpath("//input[@id='smtp']").send_keys(kwargs[
            'smtp'])
        driver.find_element_by_xpath("//input[@id='fromName']").clear()
        driver.find_element_by_xpath("//input[@id='fromName']").send_keys(
            kwargs['fromName'])
        driver.find_element_by_xpath("// input[@id='password']").clear()
        driver.find_element_by_xpath("//input[@id='password']").send_keys(
            kwargs['password'])
        driver.find_element_by_xpath("//input[@id='status0']").click()
        # click 确定
        driver.find_element_by_xpath("//button[@id='determine']").click()
        sleep(1)
        print "add {} end.".format(kwargs['smtp'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['smtp'])



def add_hdk_18(driver):
    '''添加互动课'''
    driver.refresh()
    driver.find_element_by_link_text(u"课堂管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"互动教学").click()
    sleep(0.5)
    driver.find_element_by_id("addclassroom").click()
    sleep(1)
    driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
    driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[3]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
    driver.find_element_by_xpath("//div[@id='classOrTeacher']/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_id("teachLesson_input_text").clear()
    driver.find_element_by_id("teachLesson_input_text").send_keys("hdk_long")
    driver.find_element_by_xpath("(//button[@type='button'])[16]").click()
    driver.find_element_by_link_text(u"一年级").click()
    driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
    driver.find_element_by_link_text(u"语文").click()
    driver.find_element_by_xpath("(//button[@type='button'])[18]").click()
    driver.find_element_by_xpath("//div[@id='lesson_infor']/div[3]/div/ul/li[2]/a/span").click()
    driver.find_element_by_id("ptlive_true").click()
    driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"周日").click()
    driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"第七节").click()
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr/td/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr/td[2]/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[2]/td/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[28]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[2]/td[2]/div/div/ul/li[3]/a").click()
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[29]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[3]/td/div/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("(//button[@type='button'])[30]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[3]/td[2]/div/div/ul/li[4]/a/span").click()
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[31]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[4]/td/div/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("(//button[@type='button'])[32]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[4]/td[2]/div/div/ul/li[5]/a/span").click()
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[33]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[5]/td/div/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("(//button[@type='button'])[34]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[5]/td[2]/div/div/ul/li[6]/a/span").click()
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[35]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[6]/td/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[36]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[6]/td[2]/div/div/ul/li[7]/a").click()
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[37]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[7]/td/div/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("(//button[@type='button'])[38]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[7]/td[2]/div/div/ul/li[8]/a/span").click()
    sleep(0.5)
    driver.find_element_by_css_selector("div.middle_content.finalast > button.btn.btn-success").click()
    sleep(2)


def add_hdk(driver):
    '''添加互动课'''
    driver.refresh()
    driver.find_element_by_link_text(u"课堂管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"互动教学").click()
    sleep(0.5)
    driver.find_element_by_id("addclassroom").click()
    sleep(1)
    # 第二个选项
    driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
    driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/div/div/div/div/ul/li[3]/a/span").click()
    # 第一个选项
    # driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
    # driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/div/div/div/div/ul/li[2]/a/span").click()
    # 选择主讲教室
    driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
    driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/div[2]/div/div/ul/li[2]/a/span").click()
    # add lesson name
    driver.find_element_by_id("teachLesson_input_text").clear()
    driver.find_element_by_id("teachLesson_input_text").send_keys("hdk_long")
    # 选择年级
    driver.find_element_by_xpath("(//button[@type='button'])[15]").click()
    driver.find_element_by_link_text(u"一年级").click()
    # 选择科目
    driver.find_element_by_xpath("(//button[@type='button'])[16]").click()
    driver.find_element_by_link_text(u"语文").click()
    # 选择老师
    driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
    driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/div[4]/div[3]/div/ul/li[2]/a/span").click()
    # 打开平台直播开关
    driver.find_element_by_xpath("//input[@id='ptlive_true']").click()
    # 添加起止时间
    driver.find_element_by_xpath("(//button[@type='button'])[22]").click()
    driver.find_element_by_link_text(u"周日").click()
    driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
    driver.find_element_by_link_text(u"第七节").click()
    # 添加接收教室
    driver.find_element_by_xpath("//div[@id='class_table_seedClassroom']/button").click()
    driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr/td/div/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
    # 选择第一个学校
    # driver.find_element_by_link_text(u"132教室").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr/td[2]/div/div/ul/li[2]/a").click()
    # 选择第二个学校
    # driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[2]/td[2]/div/div/ul/li[3]/a").click()
    driver.find_element_by_xpath("//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[2]/td/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
    # 选择第二个学校
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[2]/td[2]/div/div/ul/li[3]/a").click()
    # 添加教室
    driver.find_element_by_xpath("//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    driver.find_element_by_xpath("(//button[@type='button'])[28]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[3]/td/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[29]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[3]/td[2]/div/div/ul/li[4]/a/span").click()
    # 添加教室
    driver.find_element_by_xpath("//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    driver.find_element_by_xpath("(//button[@type='button'])[30]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[4]/td/div/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("(//button[@type='button'])[31]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[4]/td[2]/div/div/ul/li[5]/a").click()
    # 添加教室
    driver.find_element_by_xpath("//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    driver.find_element_by_xpath("(//button[@type='button'])[32]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[5]/td/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[33]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[5]/td[2]/div/div/ul/li[6]/a/span").click()
    # 添加教室
    driver.find_element_by_xpath("//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    driver.find_element_by_xpath("(//button[@type='button'])[34]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[6]/td/div/div/ul/li[2]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[35]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[6]/td[2]/div/div/ul/li[7]/a/span").click()
    # 添加教室
    driver.find_element_by_xpath("//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    driver.find_element_by_xpath("(//button[@type='button'])[36]").click()
    # 选择学校下拉框第一个
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[7]/td/div/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("(//button[@type='button'])[37]").click()
    driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[7]/td[2]/div/div/ul/li[8]/a/span").click()

    # 添加教室
    # driver.find_element_by_xpath("//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    # driver.find_element_by_xpath("(//button[@type='button'])[38]").click()
    # 选择学校下拉框第二个
    # driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[8]/td/div/div/ul/li[3]/a").click()
    # driver.find_element_by_xpath("(//button[@type='button'])[39]").click()
    # driver.find_element_by_xpath("//tbody[@id='theclassroom_value']/tr[8]/td[2]/div/div/ul/li[3]/a").click()

    # click ok btn
    sleep(0.5)
    driver.find_element_by_css_selector("div.middle_content.finalast > button.btn.btn-success").click()
    sleep(2)


def add_lesson(driver):
    """
    Func desc
    Args:
    -
    Usage:

    """
    '''添加互动课'''
    driver.refresh()
    driver.find_element_by_link_text(u"课堂管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"互动教学").click()
    sleep(0.5)
    driver.find_element_by_id("addclassroom").click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//div[@id='main-container']/div/div[2]/div/div[2]/div/div/div/div/div/ul/li[2]/a/span"
    ).click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//div[@id='main-container']/div/div[2]/div/div[2]/div/div[2]/div/div/ul/li[4]/a/span"
    ).click()
    sleep(0.5)
    driver.find_element_by_id("teachLesson_input_text").clear()
    driver.find_element_by_id("teachLesson_input_text").send_keys("hdk_long")
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[15]").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"一年级").click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[16]").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"语文").click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//div[@id='main-container']/div/div[2]/div/div[2]/div/div[4]/div[3]/div/ul/li[2]/a/span"
    ).click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[22]").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"每天").click()
    sleep(0.5)
    driver.find_element_by_id("jinjie_false").click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"第八节").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//div[@id='day_startTime_and_endTime']/div/span[2]").click()
    sleep(2)
    # 选择时间
    # driver.find_element_by_xpath("//div[11]/div[3]/table/tbody/tr[4]/td[7]").click()
    driver.find_element_by_xpath("//div[11]/div[3]/table/tfoot/tr/th").click()
    # driver.find_element_by_xpath("//div[13]/div[3]/table/tfoot/tr/th").click()

    sleep(2)
    driver.find_element_by_xpath(
        "//div[@id='day_startTime_and_endTime']/div[3]/span[2]/span").click()
    sleep(2)
    # 选择时间
    # driver.find_element_by_xpath("//div[19]/div[3]/table/tbody/tr[5]/td[6]").click()
    # driver.find_element_by_xpath("//div[12]/div[3]/table/tbody/tr[4]/td[6]").click()
    # driver.find_element_by_xpath("//div[12]/div[3]/table/tbody/tr[4]/td[7]").click()
    driver.find_element_by_xpath("//div[12]/div[3]/table/tfoot/tr/th").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//tbody[@id='theclassroom_value']/tr/td/div/div/ul/li[2]/a/span"
    ).click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//tbody[@id='theclassroom_value']/tr/td[2]/div/div/ul/li[2]/a/span"
    ).click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//button[@onclick='addClassroomByCheck(null,$(this));']").click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//tbody[@id='theclassroom_value']/tr[2]/td/div/div/ul/li[2]/a").click(
        )
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[27]").click()
    sleep(0.5)
    driver.find_element_by_xpath(
        "//tbody[@id='theclassroom_value']/tr[2]/td[2]/div/div/ul/li[3]/a/span"
    ).click()
    sleep(0.5)
    driver.find_element_by_css_selector(
        "div.middle_content.finalast > button.btn.btn-success").click()
    sleep(3)


def add_jpk_18(driver):
    driver.refresh()
    driver.find_element_by_link_text(u"课堂管理").click()
    driver.find_element_by_link_text(u"精品课堂").click()
    sleep(0.5)
    driver.find_element_by_id("addclassroom").click()
    sleep(0.5)
    driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
    sleep(0.5)
    driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[3]/a/span").click()
    driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
    # driver.find_element_by_link_text(u"81教室").click()
    driver.find_element_by_xpath("//div[@id='classOrTeacher']/div/div/ul/li[2]/a").click()
    driver.find_element_by_id("teachLesson_input_text").clear()
    driver.find_element_by_id("teachLesson_input_text").send_keys("jpk_long")
    driver.find_element_by_xpath("(//button[@type='button'])[16]").click()
    driver.find_element_by_link_text(u"一年级").click()
    driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
    driver.find_element_by_link_text(u"语文").click()
    driver.find_element_by_xpath("(//button[@type='button'])[18]").click()
    driver.find_element_by_xpath("//div[@id='lesson_infor']/div[3]/div/ul/li[2]/a/span").click()
    driver.find_element_by_id("ptlive_true").click()
    driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
    driver.find_element_by_link_text(u"周日").click()
    driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
    driver.find_element_by_link_text(u"第八节").click()
    sleep(1)
    # driver.find_element_by_css_selector("div.middle_content.finalast > button.btn.btn-success").click()
    driver.find_element_by_xpath("//button[@onclick='saveClick();']").click()
    sleep(2)


    
def add_excellentClass(driver):
    """
    Func descriptions: add jpk
    Args: add_excellentClass()
    Return: None
    Usage: add_excellentClass(drvier)
    Author: wangfm
    Date: 2016-11-03 10:10:25
    """

    print "add jpk."

    try:
        driver.refresh()
        driver.find_element_by_link_text(u"课堂管理").click()
        driver.find_element_by_link_text(u"精品课堂").click()
        sleep(0.5)
        driver.find_element_by_id("addclassroom").click()
        sleep(0.5)
        # select school btn
        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"郑州一中").click()
        sleep(0.5)
        # select classroom
        driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
        sleep(0.5)
        #  driver.find_element_by_link_text(u"130教室").click()
        driver.find_element_by_xpath("//div[@id='classOrTeacher']/div/div/ul/li[2]/a").click()
        #  sleep(0.5)
        # second class
        #  driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
        #  sleep(0.5)
        #  driver.find_element_by_link_text(u"131教室").click()
        sleep(0.5)
        # input lesson name
        driver.find_element_by_id("teachLesson_input_text").clear()
        sleep(0.5)
        driver.find_element_by_id("teachLesson_input_text").send_keys("jpk")
        sleep(0.5)
        # lesson info
        driver.find_element_by_xpath("(//button[@type='button'])[15]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"一年级").click()
        sleep(0.5)
        driver.find_element_by_xpath("(//button[@type='button'])[16]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"语文").click()
        sleep(0.5)
        driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
        sleep(0.5)
        driver.find_element_by_xpath("//div[3]/div/ul/li[2]/a/span").click()
        sleep(0.5)
        # platform live
        driver.find_element_by_xpath("//input[@id='ptlive_true']").click()
        sleep(0.5)
        # select time
        driver.find_element_by_xpath("(//button[@type='button'])[22]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"周日").click()
        sleep(0.5)
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"第八节").click()
        sleep(0.5)
        # commit btn
        driver.find_element_by_xpath(
            "//button[@onclick='saveClick();']").click()
        sleep(2)
    except NoSuchElementException as e:
        print e
        print "add jpk failed."
        
announcementData = [{
 "add_title":u"测试公告",
 "noticeType_select":u"网站公告",
 "schoolName_select":u"河南省教育局",
 'disk': 'Z:\\testResource\py\pic',
 'fileNames': 'banner01.jpg'
 }]

def add_announcement(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"网站管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"公告管理").click()
    sleep(0.5)
    driver.find_element_by_id("addNotice").click()
    sleep(0.5)
    driver.find_element_by_id("add_title").clear()
    driver.find_element_by_id("add_title").send_keys(kwargs["add_title"])
    Select(driver.find_element_by_id("noticeType_select")).select_by_visible_text(kwargs["noticeType_select"])
#     Select(driver.find_element_by_id("schoolName_select")).select_by_visible_text(kwargs["schoolName_select"])
    driver.find_element_by_id("file").click()
    sleep(0.5)
    file_upload(kwargs["disk"],kwargs["fileNames"])
    sleep(0.5)
    driver.find_element_by_id("clipBtn").click()
    driver.find_element_by_id("add_sure").click() 
    
#文件上传方法
def file_upload(disk,fileNames):
    sleep(1)
    ################################点击文件操作######################################
    #shift+alt
#     win32api.keybd_event(16, 0, 0, 0)  # shift
#     win32api.keybd_event(18, 0, 0, 0)  # L键位码是73
#     win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#     win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
#     sleep(2)
    # ctrl+L
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(76, 0, 0, 0)  # L键位码是73
    win32api.keybd_event(76, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(disk)  # 输入磁盘
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    sleep(4)
    # ALT+N
    win32api.keybd_event(18, 0, 0, 0)  # ALT键位码是18
    win32api.keybd_event(78, 0, 0, 0)  # N键位码是78
    win32api.keybd_event(78, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(fileNames)  # 发送文件地址
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    ################################点击文件操作########################################


columnData = [{
 "navigationName_add":u"测试栏目名",
 "url_add":"10.1.0.19",
 "navTypeAdd":u"页眉导航",
 'sort_add': '10',
 'remark_add': '测试描述'
 }]

def add_column(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"网站管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"栏目管理").click()
    sleep(0.5)
    driver.find_element_by_id("addBtn").click()
    sleep(0.5)
    driver.find_element_by_id("navigationName_add").clear()
    driver.find_element_by_id("navigationName_add").send_keys(kwargs["navigationName_add"])
    driver.find_element_by_id("url_add").clear()
    driver.find_element_by_id("url_add").send_keys(kwargs["url_add"])
    Select(driver.find_element_by_id("navTypeAdd")).select_by_visible_text(kwargs["navTypeAdd"])
    driver.find_element_by_xpath("sort_add").clear()
    driver.find_element_by_xpath("sort_add").send_keys(kwargs["sort_add"])
    
    driver.find_element_by_id("add_sure").click()


modelData = [{
 "addname":u"测试名称",
 "addurl":u"测试地址",
 "addremark":u"测试描述",
 'addnId': u'在线课堂'
 }]
def add_model(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"网站管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"模板管理").click()
    sleep(0.5)
    driver.find_element_by_id("addschool").click()
    sleep(0.5)
    driver.find_element_by_xpath("//input[@name='addname']").clear()
    driver.find_element_by_xpath("//input[@name='addname']").send_keys(kwargs["addname"])
    driver.find_element_by_xpath("//input[@name='addurl']").clear()
    driver.find_element_by_xpath("//input[@name='addurl']").send_keys(kwargs["addurl"])
    driver.find_element_by_xpath("//input[@name='addremark']").clear()
    driver.find_element_by_xpath("//input[@name='addremark']").send_keys(kwargs["addremark"])
    Select(driver.find_element_by_id("addnId")).select_by_visible_text(kwargs["addnId"])
    
    driver.find_element_by_xpath("//div[6]/button").click()
    
liveData = [{
 "endDate":u"2017-12-06 23:50",
 "pd_lessionId":u"测试直播标题",
 "pd_sd":"480",
 'pd_hd': '820',
 "pd_uhd":"1280",
 'pd_classroom': u'测试主讲教室',
 "subject_all_option":"数学",
 "pd_order":u"第二节",
 "pd_lessionType":u"视频会议",
 "pd_province":u"安徽省",
 "pd_city":u"芜湖市",
 "pd_area":u"镜湖区",
 'disk': 'Z:\\testResource\\py\\pic',
 'fileNames': 'banner01.png'
 }]

class win32Doc:
     _public_methods_ = ['write']
     def write(self, s):
             print s

def add_live(driver, **kwargs):
    '''添加直播管理'''
    driver.refresh()
    driver.find_element_by_link_text(u"内容管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"直播管理").click()
    sleep(0.5)
    driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/button[3]").click()
    driver.find_element_by_id("addList").click()
    sleep(0.5)
#     driver.find_element_by_id("startDate").clear()
    #获取当前时间
    dataTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     driver.find_element_by_id("startDate").send_keys(startdataTime)
    startTime="$(\"#startDate\").removeAttr('readonly');$(\"#startDate\").val('"+dataTime+"')"
    stopTime="$(\"#endDate\").removeAttr('readonly');$(\"#endDate\").val('"+kwargs["endDate"]+"')"
    driver.execute_script(startTime)
    driver.execute_script(stopTime)
    
    driver.find_element_by_id("pdLession_id").clear()
    driver.find_element_by_id("pdLession_id").send_keys(kwargs["pd_lessionId"])
    driver.find_element_by_id("sd_url").clear()
    driver.find_element_by_id("sd_url").send_keys(kwargs["pd_sd"])
    driver.find_element_by_id("hd_url").clear()
    driver.find_element_by_id("hd_url").send_keys(kwargs["hd_url"])
    driver.find_element_by_id("uhd_url").clear()
    driver.find_element_by_id("uhd_url").send_keys(kwargs["pd_uhd"])
    driver.find_element_by_id("file_1").click()
    file_upload(kwargs["disk"],kwargs["fileNames"])
    sleep(0.5)
    driver.find_element_by_id("clipBtn_1").click()
    driver.find_element_by_id("classroom_name").clear()
    driver.find_element_by_id("classroom_name").send_keys(kwargs["pd_classroom"])
    Select(driver.find_element_by_id("school_name")).select_by_visible_text(kwargs["pd_schoolName"])
    Select(driver.find_element_by_id("subject_all_option")).select_by_visible_text(kwargs["subject_all_option"])
    Select(driver.find_element_by_id("order_name_option")).select_by_visible_text(kwargs["pd_order"])
    Select(driver.find_element_by_id("class_type_option")).select_by_visible_text(kwargs["pd_lessionType"])
    Select(driver.find_element_by_id("province_option")).select_by_visible_text(kwargs["pd_province"])
    sleep(0.5)
    Select(driver.find_element_by_id("city_option")).select_by_visible_text(kwargs["pd_city"])
    sleep(0.5)
    Select(driver.find_element_by_id("area_option")).select_by_visible_text(kwargs["pd_area"])
    sleep(10)
    driver.find_element_by_id("sureAdd").click()
    sleep(10)
    
#     driver.find_element_by_id("pd_lessionId").clear()
#     driver.find_element_by_id("pd_lessionId").send_keys(kwargs["pd_lessionId"])
#     driver.find_element_by_id("pd_sd").clear()
#     driver.find_element_by_id("pd_sd").send_keys(kwargs["pd_sd"])
#     driver.find_element_by_id("pd_hd").clear()
#     driver.find_element_by_id("pd_hd").send_keys(kwargs["pd_hd"])
#     driver.find_element_by_id("pd_uhd").clear()
#     driver.find_element_by_id("pd_uhd").send_keys(kwargs["pd_uhd"])
#     driver.find_element_by_id("file_2").click()
#     file_upload(kwargs["disk"],kwargs["fileNames"])
#     driver.find_element_by_id("clipBtn_2").click()
#     driver.find_element_by_id("pd_classroom").clear()
#     driver.find_element_by_id("pd_classroom").send_keys(kwargs["pd_classroom"])
#     Select(driver.find_element_by_id("pd_schoolName")).select_by_visible_text(kwargs["pd_schoolName"])
#     Select(driver.find_element_by_id("pd_order")).select_by_visible_text(kwargs["pd_order"])
#     Select(driver.find_element_by_id("pd_lessionType")).select_by_visible_text(kwargs["pd_lessionType"])
#     Select(driver.find_element_by_id("pd_province")).select_by_visible_text(kwargs["pd_province"])
#     Select(driver.find_element_by_id("pd_city")).select_by_visible_text(kwargs["pd_city"])
#     Select(driver.find_element_by_id("pd_area")).select_by_visible_text(kwargs["pd_area"])
#      
#     driver.find_element_by_id("sureUpdate").click()

#文件上传方法
def file_upload(disk,fileNames):
    sleep(1)
    ################################点击文件操作######################################
    #shift+alt
#     win32api.keybd_event(16, 0, 0, 0)  # shift
#     win32api.keybd_event(18, 0, 0, 0)  # L键位码是73
#     win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#     win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
#     sleep(2)
    # ctrl+L
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(76, 0, 0, 0)  # L键位码是73
    win32api.keybd_event(76, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(disk)  # 输入磁盘
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    sleep(4)
    # ALT+N
    win32api.keybd_event(18, 0, 0, 0)  # ALT键位码是18
    win32api.keybd_event(78, 0, 0, 0)  # N键位码是78
    win32api.keybd_event(78, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(fileNames)  # 发送文件地址
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    ################################点击文件操作########################################

if __name__ == '__main__':
    driver = webdriver.Chrome()
    user_login(driver, **loginInfo)
    # conf_child_interact(driver, '10.1.0.45', '10.1.0.56')
    # conf_mcu(driver)
    # conf_drivers_local(driver)
    for terminal in announcementData:
        add_announcement(driver, ** terminal)
