# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com

import sys, os, socket
import time
import threading
from flask import Flask, request
import subprocess
from PyQt5.QtWidgets import QApplication
from iSendServerUI import WindowUI
from PyQt5.QtGui import QTextCursor
import urllib.request
from queue import Queue
import configparser


q = Queue()
cf = configparser.ConfigParser()
cf.add_section('Host Address')


class Main(WindowUI):
    def __init__(self):
        super().__init__()
        # self.show()

        self.save_path = 'uploads_file'
        self.config_path = os.path.join(os.getenv('AppData'), 'iSendServer_Config.ini')
        self.flag = 1
        self.log_message = None
        self.ip_list = self.get_ip_list()

        self.combobox.addItems(self.ip_list)
        self.init_data()

        self.btn_start.clicked.connect(self.server_manage)
        self.combobox.currentTextChanged.connect(self.sava_config)
        self.line_edit.textChanged.connect(self.sava_config)

    def init_data(self):
        # 当修改过ip或端口后，读取用户上次修改的
        if os.path.exists(self.config_path):
            try:
                cf.read(self.config_path)
                host = cf.get('Host Address', 'last_host')
                port = cf.get('Host Address', 'last_port')
                self.combobox.setCurrentIndex(self.ip_list.index(host))
                self.line_edit.setText(port)
            except:
                pass
        else:
            self.line_edit.setText('5000')

    def get_ip_list(self):
        ip_list = socket.gethostbyname_ex(socket.gethostname())[-1]
        cur_ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                  [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
        if cur_ip in ip_list:
            ip_list.remove(cur_ip)
        ip_list.insert(0, cur_ip)
        return ip_list

    def start_server(self):
        host = self.combobox.currentText()
        port = self.line_edit.text()
        save_path = self.save_path
        return run_server(host, port, save_path)

    def start_server_threading(self):
        threads = [threading.Thread(target=self.start_server), threading.Thread(target=self.get_log)]
        for thread in threads:
            thread.setDaemon(True)
            thread.start()

    def stop_server(self):
        urllib.request.urlopen(
            'http://{host}:{port}/shutdown'.format(host=self.combobox.currentText(), port=self.line_edit.text()))

    def get_log(self):
        while True:
            log_message = q.get()
            if log_message:
                self.print_info(log_message)
                # 将光标定位到最后，以刷新显示最后一行
                cursor = self.text_edit.textCursor()
                cursor.movePosition(QTextCursor.End)
                self.text_edit.setTextCursor(cursor)

    def server_manage(self):
        cur_server_addr = 'http://{host}:{port}/'.format(host=self.combobox.currentText(), port=self.line_edit.text())
        if self.flag:
            self.start_server_threading()
            self.print_info('服务已启动，测试地址：%s\n' % cur_server_addr)

            self.flag = 0
            self.btn_start.setText('Stop')
            self.btn_start.setStyleSheet('QPushButton#btn_start{background-color: rgb(244, 84, 84)}'
                                         'QPushButton#btn_start:hover{background-color: rgb(243,63,63);}')
        else:
            self.stop_server()
            self.flag = 1
            self.print_info('服务已停止!\n')
            self.btn_start.setText('Start')
            self.btn_start.setStyleSheet('QPushButton#btn_start{background-color: rgb(18, 150, 17);}'
                                         'QPushButton#btn_start:hover{background-color: rgb(13,115,13);}')

    def sava_config(self):
        # 保存用户的配置信息
        cf.set('Host Address', 'last_host', self.combobox.currentText())
        cf.set('Host Address', 'last_port', self.line_edit.text())
        cf.write(open(self.config_path, 'w'))

    def print_info(self, text):
        cur_time = time.strftime('[%H:%M:%S] ')
        self.text_edit.append(cur_time + text)


flask_app = Flask('myapp')


@flask_app.route('/', methods=['GET'])
def test():
    return '<h1>iSendServer works!</h1>'


@flask_app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['file']
    if upload_file:
        filename = upload_file.filename
        file_path = os.path.join(flask_app.root_path, flask_app.config['UPLOAD_FOLDER'], filename)
        upload_file.save(file_path)
        q.put(file_path)

        if '.' in filename and filename.rsplit('.', 1)[1] in ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tif', 'tiff']:
            subprocess.Popen('rundll32.exe shimgvw.dll,ImageView_Fullscreen {}'.format(file_path), shell=True)

        return 'upload success'
    else:
        return 'upload failed'


# 主要用来停止web服务的
@flask_app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


def run_server(host, port, save_path):
    flask_app.config['UPLOAD_FOLDER'] = save_path

    if not os.path.exists(save_path):
        os.mkdir(save_path)
    flask_app.run(host=host, port=port)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
