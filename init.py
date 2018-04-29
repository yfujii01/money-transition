from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from json import load
from today import get_today


def execute():
    # パラメータ読み込み
    rf = open('config.json', 'r')
    conf = load(rf)
    rf.close()

    # web_driver作成
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(15)

    try:
        # ログイン
        driver.get('https://moneyforward.com/users/sign_in')
        driver.find_element_by_css_selector('#sign_in_session_service_email').send_keys(conf.get('id'))
        driver.find_element_by_css_selector('#sign_in_session_service_password').send_keys(conf.get('ps'))
        driver.find_element_by_css_selector('#login-btn-sumit').click()

        # 詳細画面表示
        driver.get('https://moneyforward.com/bs/history/list/' + get_today())

        # 詳細データ
        tab_list = []

        # テーブル内容取得
        table_elem = driver.find_element_by_class_name("table")
        trs = table_elem.find_elements(By.TAG_NAME, "tr")
        for i in range(1, len(trs)):
            tds = trs[i].find_elements(By.TAG_NAME, "td")
            line = ""
            for j in range(0, len(tds)):
                if j < len(tds) - 1:
                    line += ("%s\t" % tds[j].text).replace('円', '')
                else:
                    line += ("%s\n" % tds[j].text)
            tab_list.append(line)

        # ファイル出力
        wf = open('data/out%s.txt' % get_today(), 'w')
        for t in tab_list:
            wf.writelines(t)
            print(t)
        wf.close()

    finally:
        driver.quit()


if __name__ == '__main__':
    execute()
