# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com

ui_style = """
QWidget
{
    color: rgb(255, 255, 255);
    background-color: #31363b;
    selection-background-color:#3daee9;
    selection-color: #eff0f1;
    background-clip: border;
    border-image: none;
    border: 0px transparent black;
    outline: 0;
    font: 18px;

}
QWidget:focus
{
    border: 1px solid #3daee9;
}

QPushButton:focus
{
    border: none;
}


QPushButton#btn_close:hover
{
    background-color: rgb(244, 84, 84);
}

QPushButton#btn_min:hover
{
    background-color: rgb(35, 38, 41);
}


QPushButton#btn_start
{
    background-color: rgb(18, 150, 17);
    padding: 5px;
    border-radius: 5px;
    outline: none;
}

QPushButton#btn_start:hover
{
    background-color: rgb(13,115,13);
}

QPushButton#btn_start:pressed
{
    /*background-color: rgb(244, 84, 84);*/
    padding-top: -15px;
    padding-bottom: -17px;
}

QComboBox
{
    selection-background-color: #3daee9;
    border-STYLE: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    padding: 5px;
}



QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}


QComboBox QAbstractItemView
{
    background-color: #232629;
    border-radius: 2px;
    border: 1px solid #76797C;
    selection-background-color: #18465d;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-STYLE: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow
{
    image: url(:rc/down_arrow_disabled.png);
}

QComboBox::down-arrow:on, QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    image: url(:rc/down_arrow.png);
}

QLineEdit
{
    padding: 5px;
    border-STYLE: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    color: #eff0f1;
}

QTextEdit
{
    border: 1px solid #76797C;
    color: rgb(123,136,143);
    font: 15px
}
QTextEdit:focus
{
    border: 1px solid #76797C;
}
"""