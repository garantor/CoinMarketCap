from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import requests

main, _ = loadUiType('newPrice.ui')
CMC_API_KEY = 'a8f73877-e12b-4e93-9683-e213e4a42379'

fiat = ("USD","DZD","ARS","AMD","AUD","AZN","BHD", "BDT","BYN","BMD","CNY","EGP","EUR","INR","NZD",
"NGN","GBP","QAR","KRW","UGX")

class MainAll(QMainWindow, main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(359, 568)
        self.show()
        for i in range(1, 100):
            self.comboBox.addItem(str(i))
        for i in fiat:
            self.comboBox_2.addItem(str(i)) 

        self.pushButton.clicked.connect(self.cmc_api_func)


    def cmc_api_func(self):       
        currency = self.comboBox_2.currentText()
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '',
            'limit': '1',
            'convert': currency
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': CMC_API_KEY,
        }
        parameters['start'] = self.comboBox.currentText()
        try:
            page = requests.get(url, parameters, headers=headers).json()
            price = page['data'][0]['quote'][currency]['price']
            name = page['data'][0]['name']
            rank = page['data'][0]['cmc_rank']
            max_sup = page['data'][0]['max_supply']
            int_page = int(price)
            int_page2 = ("The price for " + str(name).upper() + " is " + str(int_page) + (currency).lower() + " and it Ranked " + str(rank) + " With a Max Supply of " + str(max_sup))
            self.textEdit.setText(int_page2)
            self.statusBar().showMessage(str(price) + str(currency))
        except:
            self.statusBar().showMessage('Please Check Your internet')
        
        




def RunMain():
    app =QApplication(sys.argv)
    window = MainAll()
    window.show()
    app.exec()


if __name__ == '__main__':
    RunMain()
