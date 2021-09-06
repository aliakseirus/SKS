# This program can find prices on materials from user's inputs, 
#
# and put it in Excel file.
#
# Program create only for First Number LLC usage.


# import libraries
from tkinter import *
from tkinter import ttk
from tkinter import Radiobutton
from tkinter import Checkbutton
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from bs4 import BeautifulSoup
import numpy as np
import math
import pandas as pd
import xlsxwriter
import datetime
import urllib.request
import os
import shutil
import requests


# download Datastream price
def download_datastream():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')

    if not os.path.isfile('Datastream_price.xls'):
        try:
            site = urllib.request.urlopen("https://datastream.by/files/Datastream_price.xls").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/Datastream_price.xls', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Datastream price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong!')


# download Avant Video price
def download_avant_video():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')
    
    if not os.path.isfile('/home/' + str(os.environ.get( "USERNAME" )) + 
        '/Documents/Prices/avant-tehno-prais-list-video.xlsx'):
        try:
            site = urllib.request.urlopen("https://avant.by/upload/iblock/529/"
                "avant_tehno_prais_list_video.xlsx").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/avant-tehno-prais-list-video.xlsx', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Avant Video price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong! I think, tnat '
                'Avant change way to price again.')


# download Avant Skd price
def download_avant_skd():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')
    
    if not os.path.isfile('/home/' + str(os.environ.get( "USERNAME" )) + 
        '/Documents/Prices/avant-tehno-prais-list-dostup.xlsx'):
        try:
            site = urllib.request.urlopen("https://avant.by/upload/iblock/4f1/"
                "avant_tehno_prais_list_dostup.xlsx").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/avant-tehno-prais-list-dostup.xlsx', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Avant Skd price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong! I think, tnat '
                'Avant change way to price again.')


# download Netair price
def download_netair():
    if not os.path.exists('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices'):
        os.mkdir('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')

    if not os.path.isfile('/home/' + str(os.environ.get( "USERNAME" )) + 
        '/Documents/Prices/price_netair_b2b_sp.xls'):
        try:
            site = urllib.request.urlopen("https://netair.by/price/price_no_data/"
                "price_netair_b2b_sp.xls").read()
            file = open('/home/' + str(os.environ.get( "USERNAME" )) + 
                '/Documents/Prices/price_netair_b2b_sp.xls', 'wb')
            file.write(site)
            file.close()
            messagebox.showinfo('Good!', 'Netair price has beed downloaded!')
        except:
            messagebox.showinfo('Warning!', 'Something went wrong!')


# delete folder with prices
def delete_prices():
    try:
        shutil.rmtree('/home/' + str(os.environ.get( "USERNAME" )) + '/Documents/Prices')
        messagebox.showinfo('Good!', 'All prices has been removed!')
    except:
        messagebox.showinfo('Ohh!', 'There is no folder with prices!')


# closing program
def close_program():
    root.quit()


# get information from enter fields
def get_input():
    
    def make_doc():
        if os.path.exists("Documents/"):                                            # проверка существования директории
            pass
        else:
            os.mkdir("Documents/")                                                  # создать директорию

        # создание файла Excel
        workbook = xlsxwriter.Workbook('Documents/' + str(name_of_file.get()) + ' ' + str(datetime.date.today()) + '.xlsx')
        worksheet1 = workbook.add_worksheet('КП FNS')
        worksheet2 = workbook.add_worksheet('Расшифровка работ')

    # заполнение вкладки 1 (КП FNS)
        worksheet1.insert_image('B3', 'Pictures/FN.png')

        worksheet1.set_column('A:A', 3.86)
        worksheet1.set_column('B:B', 3.71)
        worksheet1.set_column('C:C', 79.86)
        worksheet1.set_column('D:D', 6.29)
        worksheet1.set_column('E:E', 16.71)
        worksheet1.set_column('F:F', 19.29)
        worksheet1.set_column('G:G', 19.14)

        # настройка шапки
        line=0  # строка 1
        worksheet1.set_row(line, 14.25)
        line += 1 # строка 2 
        worksheet1.set_row(line, 14.25)
        line += 1 # строка 3
        worksheet1.set_row(line, 14.25)
        style=workbook.add_format({'bold': True, 'font_name': 'Cambria'})
        worksheet1.write(line, 4, 'ООО «Первый номер сервис»', style)
        line += 1 # строка 4
        worksheet1.set_row(line, 14.25)
        style=workbook.add_format({'font_name': 'Cambria', 'font_size': 10})
        worksheet1.write(line, 4, '220005, Республика Беларусь, г.Минск,', style)
        line += 1 # строка 5
        worksheet1.set_row(line, 14.25)
        worksheet1.write(line, 4, 'ул. Платонова 36', style)
        line += 1 # строка 6
        worksheet1.set_row(line, 14.25)
        worksheet1.write(line, 4, 'IBAN: BY44PJCB30120395771000000933', style)
        line += 1 # строка 7
        worksheet1.set_row(line, 14.25)
        worksheet1.write(line, 4, 'BIC SWIFT: PJCBBY2X', style)
        line += 1 # строка 8
        worksheet1.set_row(line, 14.25)
        worksheet1.write(line, 4, 'в «Приорбанк» ОАО ЦБУ 102,', style)
        line += 1 # строка 9
        worksheet1.set_row(line, 14.25)
        worksheet1.write(line, 4, 'г. Минск, Логойский тракт, 15/1', style)
        line += 1 # строка 10
        worksheet1.set_row(line, 14.25)
        worksheet1.write(line, 4, 'УНП 192558673', style)
        line += 1 # строка 11
        worksheet1.set_row(line, 14.25)
        style=workbook.add_format({'bold': True, 'font_name': 'Cambria', 'underline': True})
        worksheet1.write(line, 4, '+375-29-6494090', style)

        # оглавление
        line += 1 # строка 12
        worksheet1.set_row(line, 14.25)

        line += 1 # строка 13
        worksheet1.merge_range(line, 1 , line, 6, None)
        worksheet1.set_row(line, 18.75)
        style=workbook.add_format({'text_wrap': True,
            'bold'          : True,
            'font_name'     : 'Cambria',
            'font_size'     : 12,
            'bg_color'      : 'D3D3D3',
            'center_across' : True,
            'valign'        : 'top'})
        worksheet1.write(line, 1, "Предложение по монтажным и пуско-наладочным работам, включая материалы и оборудование,", style)
        
        line += 1 # строка 14
        worksheet1.merge_range(line, 1 , line, 6, None)
        worksheet1.set_row(line, 18.75)
        worksheet1.write(line, 1, str(name_of_file.get()), style)

        # таблица материалы и оборудование
        line += 1 # строка 15
        worksheet1.set_row(line, 14.25)      
        line += 1 # строка 16
        worksheet1.merge_range(line, 1, line, 6, None)
        style=workbook.add_format({'bold': True,
            'font_name'     : 'Cambria',
            'font_size'     : 12,
            'center_across' : True,
            'valign'        : 'top'})
        worksheet1.write(line, 1, "МАТЕРИАЛЫ И ОБОРУДОВАНИЕ", style)
        
        line += 1 # строка 17
        worksheet1.set_row(line, 6.00)
        # шапка таблицы

        line += 1 # строка 18
        style=workbook.add_format({'bold': True,
            'font_name'     : 'Cambria',
            'font_size'     : 10,
            'align'         : 'center',
            'valign'        : 'vcenter',
            'top'           : 2,
            'bottom'        : 2,
            'left'          : 2,
            'right'         : 1})
        worksheet1.write(line, 1, "№", style)
        style=workbook.add_format({'bold': True,
            'font_name'     : 'Cambria',
            'font_size'     : 9,
            'align'         : 'center',
            'valign'        : 'vcenter',
            'top'           : 2,
            'bottom'        : 2,
            'left'          : 1,
            'right'         : 1})
        worksheet1.write(line, 2, "Описание", style)
        worksheet1.write(line, 3, "К-во", style)
        worksheet1.write(line, 4, "Цена, руб. без НДС", style)
        worksheet1.write(line, 5, "Сумма, руб. без НДС", style)
        style=workbook.add_format({'bold': True,
            'font_name'     : 'Cambria',
            'font_size'     : 9,
            'align'         : 'center',
            'valign'        : 'vcenter',
            'top'           : 2,
            'bottom'        : 2,
            'left'          : 1,
            'right'         : 2})
        worksheet1.write(line, 6, "Сумма, руб. с НДС 20%", style)
        line += 1 # строка 19
        worksheet1.merge_range(line, 1, line, 6, None)
        style=workbook.add_format({'bold': True,
            'font_name'     : 'Cambria',
            'font_size'     : 10,
            'bg_color'      : 'D3D3D3',
            'align'         : 'left',
            'valign'        : 'vcenter',
            'left'          : 2,
            'bottom'        : 2,
            'italic'        : True})
        worksheet1.write(line, 1, "Материалы и оборудование", style)
        worksheet1.write(line, 2, None, style)
        worksheet1.write(line, 3, None, style)
        worksheet1.write(line, 4, None, style)
        worksheet1.write(line, 5, None, style)
        style=workbook.add_format({'bold': True,
            'font_name'     : 'Cambria',
            'font_size'     : 10,
            'bg_color'      : 'D3D3D3',
            'align'         : 'left',
            'valign'        : 'vcenter',
            'left'          : 2,
            'bottom'        : 2,
            'right'         : 2,
            'italic'        : True})
        worksheet1.write(line, 6, None, style)

        # заполнение таблицы
        line += 1
        count = 1
        # заполнение столбца номер по порядку
        style=workbook.add_format({'font_name': 'Cambria',
            'font_size'     : 10,                         
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'left'          : 2,
            'bottom'        : 1,
            'right'         : 1})                         
        for material in material_list:         
            worksheet1.write(line, 1, count, style)       
            line += 1 
            count+=1
        # заполнение столбца с материалами
        line -= len(material_list)        
        style = workbook.add_format({'font_name': 'Cambria',
            'font_size': 10,    
            'align': 'left',    
            'valign': 'vcenter',
            'left': 1,          
            'bottom': 1,        
            'right': 1,         
            'text_wrap': True}) 
        for material in material_list:      
            worksheet1.write(line, 2, material, style)           
            line += 1 
        # заполнение столбца с количеством
        line -= len(material_list)        
        style = workbook.add_format({'font_name': 'Cambria',
            'font_size'     : 10,                         
            'align'         : 'center',                   
            'valign'        : 'vcenter',                  
            'left'          : 1,
            'bottom'        : 1,
            'right'         : 1})                         
        for kolvo in kolvo_list:         
            worksheet1.write(line, 3, kolvo, style)           
            line += 1 
        # заполнение столбца с ценой без НДС
        line -= len(material_list)        
        for cena in cena_bez_nds_list:  
            if cena == 0:
                style = workbook.add_format({'num_format': '0.00',    
                    'bg_color'      : 'FFFF00',           
                    'font_name'     : 'Cambria',          
                    'font_size'     : 10,                 
                    'align'         : 'right',            
                    'valign'        : 'vcenter',          
                    'left'          : 1,                  
                    'bottom'        : 1,                  
                    'right'         : 1})                 
            else:   
                style = workbook.add_format({'num_format': '0.00',
                    'font_name'     : 'Cambria',          
                    'font_size'     : 10,                 
                    'align'         : 'right',            
                    'valign'        : 'vcenter',          
                    'left'          : 1,                  
                    'bottom'        : 1,                  
                    'right'         : 1})                 
            worksheet1.write(line, 4, cena, style)               
            line += 1 
        # заполнение столбца со стоимостью без НДС
        number = 20 
        line -= len(material_list)        
        for cena in cena_bez_nds_list:  
            if cena == 0:
                style = workbook.add_format({'num_format': '0.00',    
                    'bg_color'      : 'FFFF00',           
                    'font_name'     : 'Cambria',          
                    'font_size'     : 10,                 
                    'align'         : 'right',            
                    'valign'        : 'vcenter',          
                    'left'          : 1,                  
                    'bottom'        : 1,                  
                    'right'         : 1})                 
            else:   
                style = workbook.add_format({'num_format': '0.00',    
                    'font_name'     : 'Cambria',          
                    'font_size'     : 10,                 
                    'align'         : 'right',            
                    'valign'        : 'vcenter',          
                    'left'          : 1,                  
                    'bottom'        : 1,                  
                    'right'         : 1})                 
            worksheet1.write(line, 5, '=D'+str(number)+'*E'+str(number), style)                 
            line += 1 
            number += 1           
        # заполнение столбца со стоимостью c НДС
        number = 20 
        line -= len(material_list)        
        for cena in cena_bez_nds_list:  
            if cena == 0:
                style = workbook.add_format({'num_format': '0.00',    
                    'bg_color'      : 'FFFF00',           
                    'font_name'     : 'Cambria',          
                    'font_size'     : 10,                 
                    'align'         : 'right',            
                    'valign'        : 'vcenter',          
                    'left'          : 1,                  
                    'bottom'        : 1,                  
                    'right'         : 2})                 
            else:   
                style = workbook.add_format({'num_format': '0.00',    
                    'font_name'     : 'Cambria',          
                    'font_size'     : 10,                 
                    'align'         : 'right',            
                    'valign'        : 'vcenter',          
                    'left'          : 1,                  
                    'bottom'        : 1,                  
                    'right'         : 2})                 
            worksheet1.write(line, 6, '=F'+str(number)+'*1.2', style) 
            line += 1 
            number += 1           
        # строка ИТОГО
        style = workbook.add_format({'top': 2,            
            'bottom'        : 0,
            'right'         : 2,
            'left'          : 0})                         
        worksheet1.write(line, 1, None, style)            
        style = workbook.add_format({
            'bold'          : True,                       
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 2,
            'bottom'        : 2})                         
        worksheet1.write(line, 2, "ИТОГО", style)         
        style = workbook.add_format({'bold': True,        
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})       
        worksheet1.write(line, 3, None, style)            
        worksheet1.write(line, 4, None, style)            
        # вычисление суммы без НДС
        style = workbook.add_format({'num_format':'0.00', 
            'bold'          : True,                       
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})   
        worksheet1.write(line, 5, '=SUM(F'+str(20)+':F'+str(number-1)+')', style)               
        # вычисление суммы с НДС
        style = workbook.add_format({'num_format':'0.00', 
            'bold'          : True,                       
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'right'         : 2,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})  
        worksheet1.write(line, 6, '=SUM(G'+str(20)+':G'+str(number-1)+')', style)    

        # таблица РАБОТЫ
        line+=2
        worksheet1.merge_range(line, 1, line, 6, None)    
        style=workbook.add_format({'bold': True,          
            'font_name'     : 'Cambria',                  
            'font_size'     : 12,                         
            'center_across' : True,                       
            'valign'        : 'top'})                       
        worksheet1.write(line, 1, "РАБОТЫ", style)        
        line+=1
        worksheet1.set_row(line, 6.00)                    
        # шапка таблицы
        line+=1
        style=workbook.add_format({'bold': True,          
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'center',                   
            'valign'        : 'vcenter',                  
            'top'           : 2,
            'bottom'        : 2,
            'left'          : 2,
            'right'         : 1})                         
        worksheet1.write(line, 1, "№", style)             
        style=workbook.add_format({'bold': True,          
            'font_name'     : 'Cambria',                  
            'font_size'     : 9,
            'align'         : 'center',                   
            'valign'        : 'vcenter',                  
            'top'           : 2,
            'bottom'        : 2,
            'left'          : 1,
            'right'         : 1})       
        worksheet1.write(line, 2, "Описание", style)      
        worksheet1.write(line, 3, "К-во", style)          
        worksheet1.write(line, 4, "Цена, руб. без НДС", style)        
        worksheet1.write(line, 5, "Сумма, руб. без НДС", style)       
        style=workbook.add_format({'bold': True,          
            'font_name'     : 'Cambria',                  
            'font_size'     : 9,
            'align'         : 'center',                   
            'valign'        : 'vcenter',                  
            'top'           : 2,
            'bottom'        : 2,
            'left'          : 1,
            'right'         : 2}) 
        worksheet1.write(line, 6, "Сумма, руб. с НДС 20%", style)     
        line+=1
        worksheet1.merge_range(line, 1, line, 6, None)    
        style=workbook.add_format({'bold': True,          
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'italic'        : True,                       
            'top'           : 0,
            'bottom'        : 2,
            'left'          : 2,
            'right'         : 0}) 
        worksheet1.write(line, 1, "Работы", style)        
        worksheet1.write(line, 2, None, style)            
        worksheet1.write(line, 3, None, style)            
        worksheet1.write(line, 4, None, style)            
        worksheet1.write(line, 5, None, style)            
        style=workbook.add_format({'bold': True,          
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'italic'        : True,                       
            'top'           : 0,
            'bottom'        : 2,
            'left'          : 2,
            'right'         : 2})
        worksheet1.write(line, 6, None, style)            
        
        # заполнение таблицы РАБОТЫ
        line+=1
        style=workbook.add_format({'bold': False,         
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'top'           : 0,
            'bottom'        : 1,
            'left'          : 2,
            'right'         : 1})       
        worksheet1.write(line, 1, "1", style)             
        style=workbook.add_format({'bold': False,         
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'text_wrap'     : True,                       
            'top'           : 0,
            'bottom'        : 1,
            'left'          : 1,
            'right'         : 1})           
        worksheet1.write(line, 2, description_of_work, style)
        style=workbook.add_format({'bold': False,         
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'center',                    
            'valign'        : 'vcenter',                  
            'text_wrap'     : True,                       
            'top'           : 0,
            'bottom'        : 1,
            'left'          : 1,
            'right'         : 1})         
        worksheet1.write(line, 3, "1", style)             
        style=workbook.add_format({'bold': False,         
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'num_format'    : '0.00',                     
            'top'           : 0,
            'bottom'        : 1,
            'left'          : 1,
            'right'         : 1})         
        worksheet1.write(line, 4, "='Расшифровка работ'!G1", style)   
        worksheet1.write(line, 5, '=D'+str(number+6)+'*E'+str(number+6), style)                 
        style=workbook.add_format({'bold': False,         
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'num_format'    : '0.00',                     
            'top'           : 0,
            'bottom'        : 1,
            'left'          : 1,
            'right'         : 2})    
        worksheet1.write(line, 6, '=F'+str(number+6)+'*1.2', style)   # добавление НДС к работам 
        # строка ИТОГО
        line+=1
        style = workbook.add_format({'top': 2,            
            'bottom'        : 0,
            'right'         : 2,
            'left'          : 0})                         
        worksheet1.write(line, 1, None, style)            
        style = workbook.add_format({'bold': True,        
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 2,
            'bottom'        : 2})                         
        worksheet1.write(line, 2, "ИТОГО", style)         
        style = workbook.add_format({'bold': True,        
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})       
        worksheet1.write(line, 3, None, style)            
        worksheet1.write(line, 4, None, style)            
        # вычисление суммы без НДС
        style = workbook.add_format({'num_format': '0.00',
            'bold'          : True,                       
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})   
        worksheet1.write(line, 5, '=F'+str(number+6), style)          
        # вычисление суммы с НДС
        style = workbook.add_format({'num_format': '0.00',
            'bold'          : True,                       
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'bg_color'      : 'D3D3D3',                   
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'right'         : 2,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})  
        worksheet1.write(line, 6, '=G'+str(number+6), style)          
        # вычисление общей суммы (материалы + работы)
        line+=3
        style = workbook.add_format({'bold': True,        
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 2,
            'bottom'        : 2})         
        worksheet1.write(line, 2, "ИТОГО СТОИМОСТЬ МАТЕРИАЛОВ, ОБОРУДОВАНИЯ И РАБОТ с НДС 20%:", style)
        style = workbook.add_format({'bold': True,        
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})         
        worksheet1.write(line, 3, None, style)            
        worksheet1.write(line, 4, None, style)            
        worksheet1.write(line, 5, None, style)            
        style = workbook.add_format({'bold': True,        
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'num_format'    : '0.00',                     
            'right'         : 2,
            'top'           : 2,
            'left'          : 0,
            'bottom'        : 2})           
        worksheet1.write(line, 6, '=G'+str(number)+'+G'+str(number+7), style)                   
        line+=1
        style = workbook.add_format({'bold': False,       
            'font_name'     : 'Cambria',                  
            'font_size'     : 11,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'right'         : 0,
            'top'           : 0,
            'left'          : 0,
            'bottom'        : 0})      
        worksheet1.write(line, 2, "в том числе НДС 20%:", style)      
        style = workbook.add_format({
            'bold'          : False,                      
            'font_name'     : 'Cambria',                  
            'font_size'     : 10,                         
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'num_format'    : '0.00',                     
            'right'         : 0,
            'top'           : 0,
            'left'          : 0,
            'bottom'        : 0 
            })         
        worksheet1.write(line, 6, '=F'+str(number)+'*0.2'+'+F'+str(number+7)+'*0.2', style)     
        # вывод дополнительной текстовой информации
        line+=2
        style = workbook.add_format({                     
            'font_name'     : 'Cambria',                  
            'font_size'     : 11,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            })
        worksheet1.write(line, 1, "Условия оплаты: 100% оплата за материалы и оборудование, 30% аванс за работы или услуги", style)
        line+=2
        worksheet1.write(line, 1, "Условия поставки: в течение 10-ти рабочих дней после поступления денежных средств на расчетный счет Исполнителя", style)
        line+=1
        style = workbook.add_format({                     
            'font_name'     : 'Cambria',                  
            'font_size'     : 11,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            'text_wrap'     : True                        
            })             
        worksheet1.set_row(line, 31.00)                   
        worksheet1.merge_range(line, 1, line, 6, None)    
        worksheet1.write(line, 1, "Срок выполнения работ: в течение 10-ти рабочих дней после получения в работу всех материалов и оборудования и поступления денежных средств на расчетный счет Исполнителя", style)
        line+=1
        worksheet1.set_row(line, 24.00)                   
        line+=1
        style = workbook.add_format({                     
            'font_name'     : 'Cambria',                  
            'font_size'     : 11,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            })                     
        worksheet1.write(line, 1, "Срок действия предложения - 5 рабочих дней", style)          
        line+=3
        style = workbook.add_format({                     
            'bold'          : True,                       
            'font_name'     : 'Cambria',                  
            'font_size'     : 12,                         
            'align'         : 'left',                     
            'valign'        : 'vcenter',                  
            })  
        worksheet1.write(line, 1, "Имеем все необходимые для проведения работ компетенции, аттестаты и лицензии", style)
        line+=1
        worksheet1.write(line, 1, "Гарантируем высокое качество выполнения работ", style)       
        line+=1
        style = workbook.add_format({                     
            'font_name'     : 'Cambria',                  
            'font_size'     : 11,                         
            'align'         : 'right',                    
            'valign'        : 'vcenter',                  
            'num_format'    : 'dd.mm.yyyy',               # формат ячейки
            })  
        worksheet1.write(line, 6, "=TODAY()", style)       # запись текущей даты в ячейку
    # заполнение вкладки 2 (Расшифровка работ)
        # ширина столбцов
        worksheet2.set_column('A:A', 85)                                                        
        worksheet2.set_column('B:B', 10)                                                        
        worksheet2.set_column('C:C', 10)                                                        
        worksheet2.set_column('D:D', 10)                                                        
        worksheet2.set_column('E:E', 1)                                                         
        worksheet2.set_column('F:F', 23)                                                        
        worksheet2.set_column('G:G', 10)                                                        
        # шапка таблицы
        line=0                                                                                  
        style = workbook.add_format({                                                           
            'bold'          : 'True',                                                           
            'font_name'     : 'Cambria',                                                        
            'font_size'     : 10,                                                               
            'align'         : 'left',
            'valign'        : 'vcenter',
            'right'         : 1,                       
            'top'           : 1,                                         
            'left'          : 1,                                   
            'bottom'        : 1                                         
            })          
        worksheet2.write(line, 0, "Наименование работ", style)                    
        style = workbook.add_format({                                                           
            'bold'          : 'True',                                                           
            'font_name'     : 'Cambria',                                                        
            'font_size'     : 10,                                                               
            'align'         : 'center',                                       
            'valign'        : 'vcenter',
            'right'         : 1,                       
            'top'           : 1,                                         
            'left'          : 1,                                   
            'bottom'        : 1                                         
            }) 
        worksheet2.write(line, 1, "Кол-во", style)                                
        worksheet2.write(line, 2, "Цена за 1", style)                             
        worksheet2.write(line, 3, "Сумма", style)                                 
        # заполнение таблицы
        line+=1                                                             
        # наименование работы
        style = workbook.add_format({                                                           
            'bold'          : 'True',                                                           
            'font_name'     : 'Cambria',                                                        
            'font_size'     : 10,                                                               
            'align'         : 'left',
            'valign'        : 'vcenter',
            'right'         : 1,                       
            'top'           : 1,                                         
            'left'          : 1,                                   
            'bottom'        : 1                                         
            })  
        for name in name_of_work:                                                  
            worksheet2.write(line, 0, name, style)                                  
            line+=1                                                         
        line-=len(name_of_work)                                                  
        # количество работы
        for kolvo in kolvo_of_work:                                                 
            if kolvo == 0:                                                      
                style = workbook.add_format({                                                   
                    'font_name'     : 'Cambria',                                                
                    'font_size'     : 10,                                                       
                    'align'         : 'center',                               
                    'valign'        : 'vcenter',                                    
                    'right'         : 1,               
                    'top'           : 1,                                 
                    'left'          : 1,                           
                    'bottom'        : 1                                 
                    })  
            else:                                                                         
                style = workbook.add_format({                                                   
                    'bg_color'      : '00FF00',                                           
                    'font_name'     : 'Cambria',                                                
                    'font_size'     : 10,                                                       
                    'align'         : 'center',                               
                    'valign'        : 'vcenter',                                    
                    'right'         : 1,               
                    'top'           : 1,                                 
                    'left'          : 1,                           
                    'bottom'        : 1                                   
                    })                        
            worksheet2.write(line, 1, kolvo, style)                                           
            line+=1                                                         
        # цена за единицу работы
        line-=len(name_of_work)                                                  
        style = workbook.add_format({                                                           
            'font_name'     : 'Cambria',                                                        
            'font_size'     : 10,                                                               
            'align'         : 'center',                                       
            'valign'        : 'vcenter',
            'right'         : 1,                       
            'top'           : 1,                                         
            'left'          : 1,                                   
            'bottom'        : 1                                         
            })  
        for price in price_per_one:                                                                                        
            worksheet2.write(line, 2, price, style)                                           
            line+=1                                                         
        # стоимость работы
        line-=len(name_of_work)                                                  
        number=2                                                                           
        for price in price_per_one:                                                     
            worksheet2.write(line, 3, '=B'+str(number)+'*C'+str(number), style)            
            line+=1                                                         
            number+=1                                                                     
        # расчет итоговой стоимости работ
        line=0                                                                                  
        style = workbook.add_format({                                                           
            'bold'          : 'True',                                                           
            'font_name'     : 'Cambria',                                                        
            'font_size'     : 10,                                                               
            'align'         : 'left',
            'valign'        : 'vcenter',
            'right'         : 1,                       
            'top'           : 1,                                         
            'left'          : 1,                                   
            'bottom'        : 1                                         
            })         
        worksheet2.write(line, 5, "Стоимость работ без НДС", style)                        
        style = workbook.add_format({                                                           
            'bold'          : 'True',                                                           
            'font_name'     : 'Cambria',                                                        
            'font_size'     : 10,                                                               
            'align'         : 'center',                                       
            'valign'        : 'vcenter',
            'right'         : 1,                       
            'top'           : 1,                                         
            'left'          : 1,                                   
            'bottom'        : 1                                         
            })            
        worksheet2.write(line, 6, '=SUM(D1:D50)', style)                                   
        workbook.close()

# variables
    material_list       = []    # наименование
    short_name_list     = []    # короткое название
    kolvo_list          = []    # количество
    cena_bez_nds_list   = []    # цена без НДС
    cena_s_nds_list     = []    # цена с НДС
    name_of_work        = []    # наименование работы
    kolvo_of_work       = []    # количество работы
    price_per_one       = []    # цена за единицу работы
    price_of_work       = []    # цена за всю работу


# check of datastream price
    try:
        datastream_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/Datastream_price.xls')
    except:
        download_datastream()

# check of avant video price
    try:
        avant_video_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/avant-tehno-prais-list-video.xlsx')
    except:
        download_avant_video()

# check of avant skd price
    try:
        avant_skd_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/avant-tehno-prais-list-dostup.xlsx')
    except:
        download_avant_skd()

# check of netair price
    try:
        netair_price = pd.ExcelFile('/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Prices/price_netair_b2b_sp.xls')
    except:
        download_netair()


# find price of material in Datastream price
    class DATASTREAM():
        
        def __init__(self, enter, vkladka, artikul, description, short_description):
            self.enter = enter
            self.vkladka = vkladka
            self.artikul = artikul
            self.description = description
            self.short_description = short_description
        
        def find_price(self): 
            if self.enter:
                df = datastream_price.parse(self.vkladka)
                df = df[['Unnamed: 0', 'Unnamed: 3']]
                df = df.rename(columns={'Unnamed: 0': 'Line0'})
                df = df.rename(columns={'Unnamed: 3': 'Line3'})
                df = df[df.Line0 == self.artikul]
                df = df[['Line3']]
                try:
                    cena_bez_nds = float(df.mean())
                except:
                    cena_bez_nds = 0
                cena_s_nds = round(cena_bez_nds*1.2,2)
                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)

# find price of material on ETP site
    class ETPROM():
        
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description
        
        def find_price(self):
            if self.enter:
                header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','accept-encoding':'gzip, deflate, br','accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'no-cache','dnt': '1','pragma': 'no-cache','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
                session = requests.Session()
                session.headers = header
                try:
                    r = session.get(self.url)
                    html = r.text
                    soup = BeautifulSoup(html, 'lxml')
                    cena_bez_nds = soup.find('span', class_="price_value").get_text()
                except:
                    cena_bez_nds = 0
                try:
                    cena_bez_nds = float(cena_bez_nds)
                except:
                    cena_bez_nds = 0
                cena_bez_nds = round(cena_bez_nds*1.2,2)
                cena_s_nds = round(cena_bez_nds*1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)

# класс Авант видео
    class AVANT():
        def __init__(self, enter, vkladka, artikul, description, short_description):
            self.enter = enter
            self.vkladka = vkladka
            self.artikul = artikul
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                df = Avant_price.parse(self.vkladka)
                df = df[['#', 'BYN с НДС']]
                df = df[df['#'] == self.artikul]
                df = df[['BYN с НДС']]

                try:
                  cena_s_nds = (df.iat[0,0])
                  cena_bez_nds = round(cena_s_nds/1.2,2)
                except:
                  cena_s_nds = 0
                  cena_bez_nds = round(cena_s_nds/1.2,2)                    

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс Авант скуд
    class AVANT_SKD():
        def __init__(self, enter, vkladka, artikul, description, short_description):
            self.enter = enter
            self.vkladka = vkladka
            self.artikul = artikul
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                df = Avant_price_skud.parse(self.vkladka)
                df = df[['Unnamed: 1', 'Unnamed: 3']]
                df = df.rename(columns={'Unnamed: 1': 'Line1'})
                df = df.rename(columns={'Unnamed: 3': 'Line3'})
                df = df[df.Line1 == self.artikul]
                df = df[['Line3']]
                cena_s_nds = (df.iat[0,0])
                cena_bez_nds = round(cena_s_nds/1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс Сфера
    class SFERA():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description

        def find_price(self):
            if self.enter == 0:
                pass
            else:
                print('Стучимся на сайт СФЕРЫ')
                header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','accept-encoding':'gzip, deflate, br','accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'no-cache','dnt': '1','pragma': 'no-cache','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
                session = requests.Session()
                session.headers = header
                r = session.get(self.url)
                html = r.text
                soup = BeautifulSoup(html, 'lxml')
                price =  soup.find('p', class_="price shk-price").get_text()
                print('Достучались')
                price = price.split(',')
                pr1=str(price[0])
                pr2=str(price[1])
                pr2=(pr2[0:2])
                if len(pr1)==2:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==3:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==5:
                    pr1=pr1.split(' ')
                    price=float(pr1[0]+pr1[1]+'.'+pr2)
                else:
                    messagebox.showinfo('Внимание!', 'Есть вопрос с ценой на сайте!')
                    print('Есть вопрос с ценой на сайте!')  
                cena_s_nds = float(price)
                cena_bez_nds = round(cena_s_nds/1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс СОБ
    class SOB():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description

        def find_price(self):
            if self.enter == 0:
                pass
            else:
                print('Стучимся на сайт СОБ')
                session = requests.Session()
                r = session.get(self.url)
                html = r.text                                                           
                soup = BeautifulSoup(html, 'lxml')
                price =  soup.find('span', class_="count").get_text()
                print('Достучались')
                price=price.split(',')
                pr1=str(price[0])
                pr2=str(price[1])
                pr2=(pr2[0:2])
                if len(pr1)==2:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==3:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==5:
                    pr1=pr1.split(' ')
                    price=float(pr1[0]+pr1[1]+'.'+pr2)
                else:
                    messagebox.showinfo('Внимание!', 'Есть вопрос с ценой ' + str(self.short_description) + ' на сайте!')
                    print('Есть вопрос с ценой ' + str(self.short_description) + ' на сайте!')  
                cena_s_nds = float(price)
                cena_bez_nds = round(cena_s_nds/1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс Стелберри
    class STELBERRY():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                print('Стучимся на сайт STELBERRY')
                session = requests.Session()
                r = session.get(self.url)
                html = r.text                                                           
                soup = BeautifulSoup(html, 'lxml')
                price =  soup.find('span', itemprop="price").get_text()
                print('Достучались')
                price=price.split(',')
                pr1=str(price[0])
                pr2=str(price[1])
                pr2=(pr2[0:2])
                if len(pr1)==2:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==3:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==5:
                    pr1=pr1.split(' ')
                    price=float(pr1[0]+pr1[1]+'.'+pr2)
                else:
                    messagebox.showinfo('Внимание!', 'Есть вопрос с ценой на сайте!')
                    print('Есть вопрос с ценой на сайте!')  
                cena_s_nds = float(price)
                cena_bez_nds = round(cena_s_nds/1.2,2)
                
                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс WORK
    class WORK():
        def __init__(self, name, price, check, enter):
            self.name = name
            self.price = price
            self.check = check
            self.enter = enter

        def find_price(self):
            if self.check.get() == 0:
                kolvo = 0
            else:
                try:
                    kolvo = int(self.enter.get())
                except:
                    messagebox.showinfo('Внимание!', 'Введите целое значение для ' + self.name + '!')
                    return()
            if kolvo == 0:
                name_of_work.append(self.name)
                kolvo_of_work.append(0)
                price_per_one.append(self.price)
                price_of_work.append(round(kolvo*self.price,2))
            else:
                name_of_work.append(self.name)
                kolvo_of_work.append(kolvo)
                price_per_one.append(self.price)
                price_of_work.append(round(kolvo*self.price,2))
# класс Нетаир
    class NETAIR():
        def __init__(self, enter, vkladka, artikul, description, short_description):
            self.enter = enter
            self.vkladka = vkladka
            self.artikul = artikul
            self.description = description
            self.short_description = short_description
        def find_price(self): 
            if self.enter == 0:
                pass
            else:
                df = Netair_price.parse(self.vkladka)
                df = df[['Unnamed: 3', 'Unnamed: 7']]
                df = df.rename(columns={'Unnamed: 3': 'Line3'})
                df = df.rename(columns={'Unnamed: 7': 'Line7'})
                df = df[df.Line3 == self.artikul]
                df = df[['Line7']]
                cena_s_nds = (df.iat[0,0])
                cena_bez_nds = round(cena_s_nds/1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс Айпиматика
    class IPMATIKA():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                session = requests.Session()
                r = session.get(self.url)
                html = r.text
                soup = BeautifulSoup(html, 'lxml')
                price = soup.find('div', class_="catalog_price_value").get_text()
                price=price.split(',')
                pr1=str(price[0])
                pr2=str(price[1])
                pr1=(pr1[2:])
                pr2=(pr2[0:2])
                if len(pr1)==2:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==3:
                    price=float(pr1+'.'+pr2)
                elif len(pr1)==5:
                    pr1=pr1.split(' ')
                    price=float(pr1[0]+pr1[1]+'.'+pr2)
                else:
                    messagebox.showinfo('Внимание!', 'Есть вопрос с ценой ' + str(self.short_description) + ' на сайте!')
                    print('Есть вопрос с ценой ' + str(self.short_description) + ' на сайте!')      
                cena_s_nds = price
                cena_bez_nds = round(cena_s_nds/1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс WSD
    class WSD():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                session = requests.Session()
                r = session.get(self.url)
                html = r.text
                soup = BeautifulSoup(html, 'lxml')
                price = soup.find('div', class_="bxr-market-item-price bxr-format-price bxr-market-price-without-name").get_text()
                price = price.split('руб')
                try:
                    price = float(price[0])
                except:
                    print('Не получил цену с wsd.by')
                cena_bez_nds = price
                cena_s_nds = round(cena_bez_nds*1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс Crazyservice
    class CRAZY():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                session = requests.Session()
                r = session.get(self.url)
                html = r.text
                soup = BeautifulSoup(html, 'lxml')
                price = soup.find('span', class_="price_value").get_text()
                price = price.replace(',','.')
                try:
                    price = float(price)
                except:
                    print('Не получил цену с crazyservice.by')
                cena_bez_nds = price
                cena_s_nds = round(cena_bez_nds*1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс Solosecurity
    class SOLO():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','accept-encoding':'gzip, deflate, br','accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'no-cache','dnt': '1','pragma': 'no-cache','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
                session = requests.Session()
                session.headers = header
                r = session.get(self.url)
                html = r.text
                soup = BeautifulSoup(html, 'lxml')
                price = soup.find('span', itemprop="price").get_text()
                price = price.split('руб')
                try:
                    price = float(price[0])
                except:
                    print('Не получил цену с solosecurity.by')
                cena_s_nds = price
                cena_bez_nds = round(cena_s_nds/1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)
# класс Activsb
    class ASB():
        def __init__(self, enter, url, description, short_description):
            self.enter = enter
            self.url = url
            self.description = description
            self.short_description = short_description
        def find_price(self):
            if self.enter == 0:
                pass
            else:
                header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','accept-encoding':'gzip, deflate, br','accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'no-cache','dnt': '1','pragma': 'no-cache','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
                session = requests.Session()
                session.headers = header
                r = session.get(self.url)
                html = r.text
                soup = BeautifulSoup(html, 'lxml')
                price = soup.find('span', class_="cena dol").get_text()
                price = price.split('руб')
                price = price[0]
                price = price.replace(',','.')
                try:
                    price = float(price)
                except:
                    print('Не получил цену с activsb.by')
                cena_s_nds = price
                cena_bez_nds = round(cena_s_nds/1.2,2)

                material_list.append(self.description)
                short_name_list.append(self.short_description)
                kolvo_list.append(self.enter)
                cena_s_nds_list.append(cena_s_nds)
                cena_bez_nds_list.append(cena_bez_nds)


# find prices of first page
    if check_utp5e.get():
        try:
            DATASTREAM(int(enter_utp5e.get()), 'TWT-LANMASTER', 'TWT-5EUTP', 
                'Кабель UTP, 4 пары, кат.5e, м.', 'UTP 5e').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-5EUTP', 
                'Кабель UTP, 4 пары, кат.5e, м.', 'UTP 5e').find_price()
    if check_utp5e_lszh.get():
        try:
            DATASTREAM(int(enter_utp5e_lszh.get()), 'TWT-LANMASTER', 'TWT-5EUTP-LSZH', 
                'Кабель UTP, 4 пары, кат.5e, LSZH, м.', 'UTP 5e LSZH').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-5EUTP-LSZH', 
                'Кабель UTP, 4 пары, кат.5e, LSZH, м.', 'UTP 5e LSZH').find_price()
    if check_utp5e_out.get():
        try:
            DATASTREAM(int(enter_utp5e_out.get()), 'TWT-LANMASTER', 'TWT-5EUTP-OUT', 
                'Кабель UTP, 4 пары, кат.5e, для внешней прокладки, м.', 
                'UTP 5e OUT').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-5EUTP-OUT', 
                'Кабель UTP, 4 пары, кат.5e, для внешней прокладки, м.', 
                'UTP 5e OUT').find_price()
    if check_ftp5e.get():
        try:
            DATASTREAM(int(enter_ftp5e.get()), 'TWT-LANMASTER', 'TWT-5EFTP', 
                'Кабель FTP, 4 пары, кат.5e, м.', 'FTP 5e').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-5EFTP', 
                'Кабель FTP, 4 пары, кат.5e, м.', 'FTP 5e').find_price()
    if check_ftp5e_lszh.get():
        try:
            DATASTREAM(int(enter_ftp5e_lszh.get()), 'TWT-LANMASTER', 'TWT-5EFTP-LSZH', 
                'Кабель FTP, 4 пары, кат.5e, LSZH, м.', 'FTP 5e LSZH').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-5EFTP-LSZH', 
                'Кабель FTP, 4 пары, кат.5e, LSZH, м.', 'FTP 5e LSZH').find_price()
    if check_ftp5e_out.get():
        try:
            DATASTREAM(int(enter_ftp5e_out.get()), 'TWT-LANMASTER', 'TWT-5EFTP-OUT', 
                'Кабель FTP, 4 пары, кат.5e, для внешней прокладки, м.', 
                'FTP 5e OUT').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-5EFTP-OUT', 
                'Кабель FTP, 4 пары, кат.5e, для внешней прокладки, м.', 
                'FTP 5e OUT').find_price()
    if check_utp6.get():
        try:
            DATASTREAM(int(enter_utp6.get()), 'TWT-LANMASTER', 'TWT-6UTP-GY', 
                'Кабель UTP, 4 пары, Кат.6, м.', 'UTP 6').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-6UTP-GY', 
                'Кабель UTP, 4 пары, Кат.6, м.', 'UTP 6').find_price()
    if check_utp6_lszh.get():
        try:
            DATASTREAM(int(enter_utp6_lszh.get()), 'TWT-LANMASTER', 'TWT-6UTP-LSZH', 
                'Кабель UTP, 4 пары, Кат.6, LSZH, м.', 'UTP 6 LSZH').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-6UTP-LSZH', 
                'Кабель UTP, 4 пары, Кат.6, LSZH, м.', 'UTP 6 LSZH').find_price()
    if check_ftp6.get():
        try:
            DATASTREAM(int(enter_ftp6.get()), 'TWT-LANMASTER', 'TWT-6FTP-GY', 
                'Кабель FTP, 4 пары, Кат.6, м.', 'FTP 6').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-6FTP-GY', 
                'Кабель FTP, 4 пары, Кат.6, м.', 'FTP 6').find_price()
    if check_ftp6_lszh.get():
        try:
            DATASTREAM(int(enter_ftp6_lszh.get()), 'TWT-LANMASTER', 'TWT-6FTP-LSZH', 
                'Кабель FTP, 4 пары, Кат.6, LSZH, м.', 'FTP 6 LSZH').find_price()
        except:
            DATASTREAM(1, 'TWT-LANMASTER', 'TWT-6FTP-LSZH', 
                'Кабель FTP, 4 пары, Кат.6, LSZH, м.', 'FTP 6 LSZH').find_price()
    if check_rg6.get():
        try:
            ETPROM(int(enter_rg6.get()), 'https://etprom.by/catalog/kabel/rg_rk/12702/', 
                'Кабель телевизионный RG-6 75 ОМ с однопроволочным медным внутренним проводником, м.', 
                'Кабель RG-6').find_price()
        except:
            ETPROM(1, 'https://etprom.by/catalog/kabel/rg_rk/12702/', 
                'Кабель телевизионный RG-6 75 ОМ с однопроволочным медным внутренним проводником, м.', 
                'Кабель RG-6').find_price()
# МАТЕРИАЛЫ: ОПТИЧЕСКИЙ КАБЕЛЬ
    if check_vok2.get():
        try:
            DATASTREAM(int(enter_vok2.get()), 'TWT-LANMASTER', 'LAN-OFC-DI2-S2-LS', 'Кабель оптический, LSZH, 2 волокна, SM, м.', 'Кабель оптический 2-вол.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель оптический 2 жилы"!')
            return()
    if check_vok4.get():
        try:
            DATASTREAM(int(enter_vok4.get()), 'TWT-LANMASTER', 'LAN-OFC-DI4-S2-LS', 'Кабель оптический, LSZH, 4 волокна, SM, м.', 'Кабель оптический 4-вол.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель оптический 4 жилы"!')
            return()
    if check_vok8.get():
        try:
            DATASTREAM(int(enter_vok8.get()), 'TWT-LANMASTER', 'LAN-OFC-DI8-S2-LS', 'Кабель оптический, LSZH, 8 волокон, SM, м.', 'Кабель оптический 8-вол.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель оптический 8 жил"!')
            return()
    if check_vok12.get():
        try:
            DATASTREAM(int(enter_vok12.get()), 'TWT-LANMASTER', 'LAN-OFC-DI12-S2-LS', 'Кабель оптический, LSZH, 12 волокон, SM, м.', 'Кабель оптический 12-вол.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель оптический 12 жил"!')
            return()
    if check_vok16.get():
        try:
            DATASTREAM(int(enter_vok16.get()), 'TWT-LANMASTER', 'LAN-OFC-DI16-S2-LS', 'Кабель оптический, LSZH, 16 волокон, SM, м.', 'Кабель оптический 16-вол.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель оптический 16 жил"!')
            return()
    if check_vok24.get():
        try:
            DATASTREAM(int(enter_vok24.get()), 'TWT-LANMASTER', 'LAN-OFC-DI24-S2-LS', 'Кабель оптический, LSZH, 24 волокна, SM, м.', 'Кабель оптический 24-вол.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель оптический 24 жил"!')
            return()
    if check_vok24.get():
        try:
            DATASTREAM(int(enter_vok24.get()), 'TWT-LANMASTER', 'LAN-OFC-DI24-S2-LS', 'Кабель оптический, LSZH, 24 волокна, SM, м.', 'Кабель оптический 24-вол.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель оптический 24 жилы"!')
            return()
# МАТЕРИАЛЫ: РОЗЕТКИ СЛАБОТОЧНЫЕ
    if check_roz1x.get():
        try:
            DATASTREAM(int(enter_roz1x.get()), 'TWT-LANMASTER', 'TWT-SM1-45-WH', 'Розетка настенная, 1 порт RJ-45 кат.5е, UTP, белая, шт.', 'Розетка 1хRJ45').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Розетка TWT 1хRJ45"!')
            return()
    if check_roz2x.get():
        try:
            DATASTREAM(int(enter_roz2x.get()), 'TWT-LANMASTER', 'TWT-SM2-4545-WH', 'Розетка настенная, 2 порта RJ-45 кат.5е, UTP, белая, шт.', 'Розетка 2хRJ45').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Розетка TWT 2хRJ45"!')
            return()
    if check_roz1x_quteo.get():
        try:
            WSD(int(enter_roz1x_quteo.get()), 'https://wsd.by/catalog/elektroustanovochnoe-oborudovanie/rozetki-i-vyklyuchateli-otkrytogo-montazha-nakladnye/rozetki-i-vyklyuchateli-legrand-otkrytogo-montazha-nakladnye/quteo-nakladnoy-montazh/quteo-belyy-tsvet/rozetki-belyy-quteo-legrand/quteo-rozetka-1khrj-45-5e-utp-belyy/', 'Legrand Quteo Розетка 1хRJ45 5E UTP (белая) Арт.782224, шт.', 'Legrand Quteo 1хRJ45').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Розетка Legrand Quteo 1хRJ45"!')
            return()
    if check_roz2x_quteo.get():
        try:
            WSD(int(enter_roz2x_quteo.get()), 'https://wsd.by/catalog/elektroustanovochnoe-oborudovanie/rozetki-i-vyklyuchateli-otkrytogo-montazha-nakladnye/rozetki-i-vyklyuchateli-legrand-otkrytogo-montazha-nakladnye/quteo-nakladnoy-montazh/quteo-belyy-tsvet/rozetki-belyy-quteo-legrand/quteo-rozetka-2khrj-45-utp-kat-5e-8-kontaktnaya-belyy/', 'Legrand Quteo Розетка 2хRJ45 5E UTP (белая) Арт.782228, шт.', 'Legrand Quteo 2хRJ45').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Розетка Legrand Quteo 2хRJ45"!')
            return()
# МАТЕРИАЛЫ: ПАТЧ-ПАНЕЛИ
    if check_pp12.get():
        try:
            DATASTREAM(int(enter_pp12.get()), 'TWT-LANMASTER', 'TWT-PP12UTP-H', 'Патч-панель настенная, 12 портов, UTP, кат.5e, шт.', 'Патч-панель 12 портов').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-панель 12 портов"!')
            return()
    if check_pp24.get():
        try:
            DATASTREAM(int(enter_pp24.get()), 'TWT-LANMASTER', 'TWT-PP24UTP', 'Патч-панель 24 порта, UTP, кат.5e, 1U, шт.', 'Патч-панель 24 порта').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-панель 24 порта"!')
            return() 
    if check_pp48.get():
        try:
            DATASTREAM(int(enter_pp48.get()), 'TWT-LANMASTER', 'TWT-PP48UTP', 'Патч-панель 48 портов, UTP, кат.5e, 2U, шт.', 'Патч-панель 48 портов').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-панель 48 портов"!')
            return()
# МАТЕРИАЛЫ: КОННЕКТОРЫ
    if check_conn_rj45.get():
        try:
            DATASTREAM(int(enter_conn_rj45.get()), 'TWT-LANMASTER', 'TWT-PL45-8P8C', 'Коннектор RJ-45 UTP 8P8C, универсальный, кат.5е, шт.', 'Коннектор RJ45').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Коннектор RJ45"!')
            return()
    if check_colp_rj45.get():
        try:
            DATASTREAM(int(enter_colp_rj45.get()), 'TWT-LANMASTER', 'TWT-BO-6.0-GY/100', 'Колпачок защитный для кабеля кат.5е, серый, шт.', 'Колпачок RJ45').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Коннектор RJ45"!')
            return()
    if check_ap_008.get():
        try:
            AVANT(int(enter_ap_008.get()), 'Каталог', '5533', 'Разъем питания для телекамер c клемной колодкой, шт.', 'Разъем питания').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Разъем питания"!')
            return()
    if check_f_connector.get():
        try:
            AVANT(int(enter_f_connector.get()), 'Каталог', '3105', 'F коннектор для кабеля 6 мм, шт.', 'F-коннектор').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "F-коннектор"!')
            return()
    if check_f_razjem.get():
        try:
            AVANT(int(enter_f_razjem.get()), 'Каталог', '4597', 'Разъем для коаксиального кабеля под F коннектор, шт.', 'F-разъем').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "F-разъем"!')
            return()
    if check_BNC_vint.get():
        try:
            AVANT(int(enter_BNC_vint.get()), 'Каталог', '5689', 'Разъем для коаксиального кабеля под винтовой зажим, шт.', 'BNC под винт с пружиной').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "BNC под винт с пружиной"!')
            return()
# МАТЕРИАЛЫ: ОПТИЧЕСКОЕ ОБОРУДОВАНИЕ
    if check_opt_kross_16_SC.get():
        try:
            DATASTREAM(int(enter_opt_kross_16_SC.get()), 'TWT-LANMASTER', 'LAN-FOBM-RM-16SC', 'Кросс оптический, 16 портов SC, 19", 1U, шт.', 'Кросс оптический, 16 портов').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кросс оптический, 16 портов"!')
            return()
    if check_opt_kross_24_SC.get():
        try:
            DATASTREAM(int(enter_opt_kross_24_SC.get()), 'TWT-LANMASTER', 'LAN-FOBM-RMS-24SC', 'Кросс оптический, 24 порта SC, 19", 1U, шт.', 'Кросс оптический, 16 портов').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кросс оптический, 24 порта"!')
            return()
    if check_PT_SC_APC_SM.get():
        try:
            DATASTREAM(int(enter_PT_SC_APC_SM.get()), 'TWT-LANMASTER', 'TWT-PIG-SC/SA-1.5', 'Пигтейл SC, APC, одномодовый, 1.5 м, шт.', 'Пигтейл SC APC SM').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Пигтейл SC APC SM"!')
            return()
    if check_PT_SC_UPC_SM.get():
        try:
            DATASTREAM(int(enter_PT_SC_UPC_SM.get()), 'TWT-LANMASTER', 'TWT-PIG-SC/SU-1.5', 'Пигтейл SC, UPC, одномодовый, 1.5 м, шт.', 'Пигтейл SC UPC SM').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Пигтейл SC UPC SM"!')
            return()
    if check_PT_LC_UPC_SM.get():
        try:
            DATASTREAM(int(enter_PT_LC_UPC_SM.get()), 'TWT-LANMASTER', 'TWT-PIG-LC/SU-1.5', 'Пигтейл LC, UPC, одномодовый, 1.5 м, шт.', 'Пигтейл LC UPC SM').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Пигтейл LC UPC SM"!')
            return()
    if check_PT_FC_UPC_SM.get():
        try:
            DATASTREAM(int(enter_PT_FC_UPC_SM.get()), 'TWT-LANMASTER', 'TWT-PIG-FC/SU-1.5', 'Пигтейл FC, UPC, одномодовый, 1.5 м, шт.', 'Пигтейл FC UPC SM').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Пигтейл FC UPC SM"!')
            return()
    if check_PT_ST_UPC_SM.get():
        try:
            DATASTREAM(int(enter_PT_ST_UPC_SM.get()), 'TWT-LANMASTER', 'TWT-PIG-ST/SU-1.5', 'Пигтейл LC, UPC, одномодовый, 1.5 м, шт.', 'Пигтейл LC UPC SM').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Пигтейл LC UPC SM"!')
            return()
    if check_PT_LC_PC_MM.get():
        try:
            DATASTREAM(int(enter_PT_LC_PC_MM.get()), 'TWT-LANMASTER', 'TWT-PIG-LC/OM2-1.5', 'Пигтейл LC, PC, многомодовый, 1.5 м, шт.', 'Пигтейл LC PC MM').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Пигтейл LC PC MM"!')
            return()
    if check_kdzs.get():
        try:
            DATASTREAM(int(enter_kdzs.get()), 'TWT-LANMASTER', 'LAN-SP-1.0x40', 'Трубка для защиты места сварки оптических волокон, КДЗС, шт.', 'КДЗС').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "КДЗС"!')
            return()
    if check_sfp_module.get():
        try:
            DATASTREAM(int(enter_kdzs.get()), 'TWT-LANMASTER', 'LAN-SFP-LX1.25-SM', 'Трансивер SFP, 1 порт 1000BASE-LX, скорость 1Gbps (Gigabit Ethernet) на расстояние до 20 км, для SМ кабеля', 'SFP-модуль').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "SFP-модуль"!')
            return()
# МАТЕРИАЛЫ: ПАТЧ-КОРДЫ
    if check_pk03.get():
        try:
            DATASTREAM(int(enter_pk03.get()), 'TWT-LANMASTER', 'TWT-45-45-0.3-GY', 'Патч-корд UTP кат.5e, 0.3 м, шт.', 'Патч-корд 0.3м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 0.3м"!')
            return()
    if check_pk05.get():
        try:
            DATASTREAM(int(enter_pk05.get()), 'TWT-LANMASTER', 'TWT-45-45-0.5-GY', 'Патч-корд UTP кат.5e, 0.5 м, шт.', 'Патч-корд 0.5м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 0.5м"!')
            return()
    if check_pk10.get():
        try:
            DATASTREAM(int(enter_pk10.get()), 'TWT-LANMASTER', 'TWT-45-45-1.0-GY', 'Патч-корд UTP кат.5e, 1.0 м, шт.', 'Патч-корд 1.0м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 1.0м"!')
            return()
    if check_pk15.get():
        try:
            DATASTREAM(int(enter_pk15.get()), 'TWT-LANMASTER', 'TWT-45-45-1.5-GY', 'Патч-корд UTP кат.5e, 1.5 м, шт.', 'Патч-корд 1.5м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 1.5м"!')
            return()
    if check_pk20.get():
        try:
            DATASTREAM(int(enter_pk20.get()), 'TWT-LANMASTER', 'TWT-45-45-2.0-GY', 'Патч-корд UTP кат.5e, 2.0 м, шт.', 'Патч-корд 2.0м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 2.0м"!')
            return()
    if check_pk30.get():
        try:
            DATASTREAM(int(enter_pk30.get()), 'TWT-LANMASTER', 'TWT-45-45-3.0-GY', 'Патч-корд UTP кат.5e, 3.0 м, шт.', 'Патч-корд 3.0м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 3.0м"!')
            return()
    if check_pk50.get():
        try:
            DATASTREAM(int(enter_pk50.get()), 'TWT-LANMASTER', 'TWT-45-45-5.0-GY', 'Патч-корд UTP кат.5e, 5.0 м, шт.', 'Патч-корд 5.0м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 5.0м"!')
            return()
    if check_pk70.get():
        try:
            DATASTREAM(int(enter_pk70.get()), 'TWT-LANMASTER', 'TWT-45-45-7.0-GY', 'Патч-корд UTP кат.5e, 7.0 м, шт.', 'Патч-корд 7.0м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 7.0м"!')
            return()
    if check_pk100.get():
        try:
            DATASTREAM(int(enter_pk100.get()), 'TWT-LANMASTER', 'TWT-45-45-10-GY', 'Патч-корд UTP кат.5e, 10.0 м, шт.', 'Патч-корд 10.0м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 10.0м"!')
            return()
    if check_pk150.get():
        try:
            DATASTREAM(int(enter_pk150.get()), 'TWT-LANMASTER', 'TWT-45-45-15-GY', 'Патч-корд UTP кат.5e, 15.0 м, шт.', 'Патч-корд 15.0м').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Патч-корд 15.0м"!')
            return()
# МАТЕРИАЛЫ: ДЛЯ ШКАФОВ
    if check_elroz.get():
        try:
            DATASTREAM(int(enter_elroz.get()), 'Шкафы ЦМО', 'БР10-008', 'Блок силовых розеток 19" 8 роз., без шнура, 10A, шт.', 'Блок розеток').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Блок розеток"!')
            return()
    if check_elwire.get():
        try:
            DATASTREAM(int(enter_elwire.get()), 'Шкафы ЦМО', 'ПВС-АП3х0,75-250-27-10-3,0 м', 'Шнур соединительный ПВС 3х0.75-250-27-10, 3.0 м, шт.', 'Шнур питания').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Шнур питания"!')
            return()
    if check_organizer.get():
        try:
            DATASTREAM(int(enter_organizer.get()), 'Шкафы TWT-LANMASTER', 'TWT-ORG/CV-1U', 'Органайзер кабельный 19" c крышкой, 1U, шт.', 'Органайзер').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Органайзер"!')
            return()
    if check_polka_280.get():
        try:
            DATASTREAM(int(enter_polka_280.get()), 'Шкафы ЦМО', 'МС-30', 'Полка фронтальная, глубина 280 мм, 2U, шт.', 'Полка 280мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Полка 280мм"!')
            return()
    if check_ibp.get():
        try:
            DATASTREAM(int(enter_ibp.get()), 'APC', 'BC750-RS', 'Источник бесперебойного питания APC BC750-RS, шт.', 'ИБП APC BC750-RS').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "ИБП APC BC750-RS"!')
            return()
# МАТЕРИАЛЫ: ПРОЧИЕ МАТЕРИАЛЫ
    if check_krp1.get():
        try:
            DATASTREAM(int(enter_krp1.get()), 'Ecoplast', 44007, 'Коробка распределительная 100х100х55, 6 вых., IP55, шт.', 'КРП 100х100').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "КРП 100х100"!')
            return()
    if check_komplekt2_25.get():
        try:
            DATASTREAM(int(enter_komplekt2_25.get()), 'Шкафы ЦМО', 'КМ-2-25', 'Комплект монтажный № 2 (винт, шайба, гайка с защелкой), упаковка 25 шт.', 'Клипсы 25 шт.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Клипсы 25 шт."!')
            return()
    if check_komplekt2_50.get():
        try:
            DATASTREAM(int(enter_komplekt2_50.get()), 'Шкафы ЦМО', 'КМ-2-50', 'Комплект монтажный № 2 (винт, шайба, гайка с защелкой), упаковка 50 шт.', 'Клипсы 50 шт.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Клипсы 50 шт."!')
            return()
    if check_poe_kit.get():
        try:
            DATASTREAM(int(enter_poe_kit.get()), 'TWT-LANMASTER', 'LAN-POE-KIT-2.1', 'Пассивный комплект POE, разъем питания 2.1 мм, шт.', 'Пассивный комплект POE').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Пассивный комплект POE"!')
            return()
# ГОФРА/КОРОБА: КАБЕЛЬ-КАНАЛЫ
    if check_kk1616.get():
        try:
            DATASTREAM(int(enter_kk1616.get()), 'Ecoplast', 77202, 'Кабель-канал ПВХ 16х16, м.', 'Кабель-канал ПВХ 16х16, м.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель-канал 16х16"!')
            return()
    if check_kk2516.get():
        try:
            DATASTREAM(int(enter_kk2516.get()), 'Ecoplast', 77207, 'Кабель-канал ПВХ 25х16, м.', 'Кабель-канал ПВХ 25х16, м.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель-канал 25х16"!')
            return()
    if check_kk2525.get():
        try:
            DATASTREAM(int(enter_kk2525.get()), 'Ecoplast', 77215, 'Кабель-канал ПВХ 25х25, м.', 'Кабель-канал ПВХ 25х25, м.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель-канал 25х25"!')
            return()
    if check_kk4016.get():
        try:
            DATASTREAM(int(enter_kk4016.get()), 'Ecoplast', 77208, 'Кабель-канал ПВХ 40х16, м.', 'Кабель-канал ПВХ 40х16, м.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель-канал 40х16"!')
            return()
    if check_kk4025.get():
        try:
            DATASTREAM(int(enter_kk4025.get()), 'Ecoplast', 77210, 'Кабель-канал ПВХ 40х25, м.', 'Кабель-канал ПВХ 40х25, м.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель-канал 40х25"!')
            return()        
    if check_kk4040.get():
        try:
            DATASTREAM(int(enter_kk4040.get()), 'Ecoplast', 77209, 'Кабель-канал ПВХ 40х40, м.', 'Кабель-канал ПВХ 40х40, м.').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Кабель-канал 40х40"!')
            return()
    if check_kklo75.get():
        try:
            WSD(int(enter_kklo75.get()), 'https://wsd.by/catalog/sistemy-dlya-prokladki-kabelya/kabelnyy-kanal-pvkh-i-aksessuary/napolnye-kabel-kanaly-i-aksessuary/napolnye-kabel-kanaly-kopos/lo-75-ld-kanal-kabelnyy-pvkh-napolnyy-kopos/', 'LO 75 LD Кабельный канал напольный ПВХ. (Темно серый) (KOPOS)', 'Кабель-канал напольный LO75').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Кабель-канал напольный LO75"!')
            return()
# ГОФРА/КОРОБА: ГОФРА\ТРУБЫ
    if check_gofra_16.get():
        try:
            DATASTREAM(int(enter_gofra_16.get()), 'Ecoplast', '10116-100', 'Труба ПВХ гофрир. легкая, диам. 16 мм, м.', 'Гофра д.16 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Гофра д.16 мм"!')
            return()
    if check_gofra_20.get():
        try:
            DATASTREAM(int(enter_gofra_20.get()), 'Ecoplast', '10120-100', 'Труба ПВХ гофрир. легкая, диам. 20 мм, м.', 'Гофра д.20 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Гофра д.20 мм"!')
            return()
    if check_gofra_25.get():
        try:
            DATASTREAM(int(enter_gofra_25.get()), 'Ecoplast', '10125-50', 'Труба ПВХ гофрир. легкая, диам. 25 мм, м.', 'Гофра д.25 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Гофра д.25 мм"!')
            return()
    if check_gofra_32.get():
        try:
            DATASTREAM(int(enter_gofra_32.get()), 'Ecoplast', 10132, 'Труба ПВХ гофрир. легкая, диам. 32 мм, м.', 'Гофра д.32 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Гофра д.32 мм"!')
            return()
    if check_gofra_40.get():
        try:
            DATASTREAM(int(enter_gofra_40.get()), 'Ecoplast', '10140-20', 'Труба ПВХ гофрир. легкая, диам. 40 мм, м.', 'Гофра д.40 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Гофра д.40 мм"!')
            return()
    if check_gofra_50.get():
        try:
            DATASTREAM(int(enter_gofra_50.get()), 'Ecoplast', 10150, 'Труба ПВХ гофрир. легкая, диам. 50 мм, м.', 'Гофра д.50 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Гофра д.50 мм"!')
            return()
    if check_pnd_16.get():
        try:
            DATASTREAM(int(enter_pnd_16.get()), 'Ecoplast', '20116-100', 'Труба ПНД гофрир. легкая, с зондом диам. 16 мм, цвет черный, м.', 'Труба ПНД д.16 мм').find_price()       
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПНД д.16 мм"!')
            return()
    if check_pnd_20.get():
        try:
            DATASTREAM(int(enter_pnd_20.get()), 'Ecoplast', '20120-100', 'Труба ПНД гофрир. легкая, с зондом диам. 20 мм, цвет черный, м.', 'Труба ПНД д.20 мм').find_price()       
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПНД д.20 мм"!')
            return()
    if check_pnd_25.get():
        try:
            DATASTREAM(int(enter_pnd_25.get()), 'Ecoplast', '20125-50', 'Труба ПНД гофрир. легкая, с зондом диам. 25 мм, цвет черный, м.', 'Труба ПНД д.25 мм').find_price()       
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПНД д.25 мм"!')
            return()
    if check_pnd_32.get():
        try:
            DATASTREAM(int(enter_pnd_32.get()), 'Ecoplast', 20132, 'Труба ПНД гофрир. легкая, с зондом диам. 32 мм, цвет черный, м.', 'Труба ПНД д.32 мм').find_price()       
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПНД д.32 мм"!')
            return()
    if check_truba_16.get():
        try:
            DATASTREAM(int(enter_truba_16.get()), 'Ecoplast', 30016, 'Труба ПВХ жесткая легкая диам. 16 мм, м.', 'Труба ПВХ жесткая д.16 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПВХ жесткая д.16 мм"!')
            return()
    if check_truba_20.get():
        try:
            DATASTREAM(int(enter_truba_20.get()), 'Ecoplast', 30020, 'Труба ПВХ жесткая легкая диам. 20 мм, м.', 'Труба ПВХ жесткая д.20 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПВХ жесткая д.20 мм"!')
            return()
    if check_truba_25.get():
        try:
            DATASTREAM(int(enter_truba_25.get()), 'Ecoplast', 30025, 'Труба ПВХ жесткая легкая диам. 25 мм, м.', 'Труба ПВХ жесткая д.25 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПВХ жесткая д.25 мм"!')
            return()
    if check_truba_32.get():
        try:
            DATASTREAM(int(enter_truba_32.get()), 'Ecoplast', 30032, 'Труба ПВХ жесткая легкая диам. 32 мм, м.', 'Труба ПВХ жесткая д.32 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПВХ жесткая д.32 мм"!')
            return()
    if check_truba_40.get():
        try:
            DATASTREAM(int(enter_truba_40.get()), 'Ecoplast', 30040, 'Труба ПВХ жесткая легкая диам. 40 мм, м.', 'Труба ПВХ жесткая д.40 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПВХ жесткая д.40 мм"!')
            return()
    if check_truba_50.get():
        try:
            DATASTREAM(int(enter_truba_50.get()), 'Ecoplast', 30050, 'Труба ПВХ жесткая легкая диам. 50 мм, м.', 'Труба ПВХ жесткая д.50 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПВХ жесткая д.50 мм"!')
            return()
    if check_truba_63.get():
        try:
            DATASTREAM(int(enter_truba_63.get()), 'Ecoplast', 30063, 'Труба ПВХ жесткая легкая диам. 63 мм, м.', 'Труба ПВХ жесткая д.63 мм').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Труба ПВХ жесткая д.63 мм"!')
            return()
# ГОФРА/КОРОБА: АКСЕССУАРЫ ДЛЯ ТРУБ
    if check_klipsa_16.get():
        try:
            DATASTREAM(int(enter_klipsa_16.get()), 'Ecoplast', 41716, 'Держатель (клипса) для труб диам. 16 мм, шт.','Клипса д.16 мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.16 мм"!')
            return()
    if check_klipsa_20.get():
        try:
            DATASTREAM(int(enter_klipsa_20.get()), 'Ecoplast', 41720, 'Держатель (клипса) для труб диам. 20 мм, шт.','Клипса д.20 мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.20 мм"!')
            return()
    if check_klipsa_25.get():
        try:
            DATASTREAM(int(enter_klipsa_25.get()), 'Ecoplast', 41725, 'Держатель (клипса) для труб диам. 25 мм, шт.','Клипса д.25 мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.25 мм"!')
            return()
    if check_klipsa_32.get():
        try:
            DATASTREAM(int(enter_klipsa_32.get()), 'Ecoplast', 41732, 'Держатель (клипса) для труб диам. 32 мм, шт.','Клипса д.32 мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.32 мм"!')
            return()
    if check_klipsa_40.get():
        try:
            DATASTREAM(int(enter_klipsa_40.get()), 'Ecoplast', 41740, 'Держатель (клипса) для труб диам. 40 мм, шт.','Клипса д.40 мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.40 мм"!')
            return() 
    if check_klipsa_50.get():
        try:
            DATASTREAM(int(enter_klipsa_50.get()), 'Ecoplast', 41750, 'Держатель (клипса) для труб диам. 50 мм, шт.','Клипса д.50 мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.50 мм"!')
            return()
    if check_klipsa_16_z.get():
        try:
            DATASTREAM(int(enter_klipsa_16_z.get()), 'Ecoplast', 41616, 'Держатель с защелкой для труб диам. 16 мм, шт.','Клипса д.16 мм с защелкой').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.16 мм"!')
            return()
    if check_klipsa_20_z.get():
        try:
            DATASTREAM(int(enter_klipsa_20_z.get()), 'Ecoplast', 41620, 'Держатель с защелкой для труб диам. 20 мм, шт.','Клипса д.20 мм с защелкой').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.20 мм"!')
            return()
    if check_klipsa_25_z.get():
        try:
            DATASTREAM(int(enter_klipsa_25_z.get()), 'Ecoplast', 41625, 'Держатель с защелкой для труб диам. 25 мм, шт.','Клипса д.25 мм с защелкой').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.25 мм"!')
            return()
    if check_klipsa_32_z.get():
        try:
            DATASTREAM(int(enter_klipsa_32_z.get()), 'Ecoplast', 41632, 'Держатель с защелкой для труб диам. 32 мм, шт.','Клипса д.32 мм с защелкой').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Клипса д.32 мм"!')
            return()
    if check_mufta_16.get():
        try:
            DATASTREAM(int(enter_mufta_16.get()), 'Ecoplast', 42516, 'Муфта соедин. для труб диам. 16 мм, шт.','Муфта соедин. для труб D16мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Муфта соедин. для труб D16мм"!')
            return() 
    if check_mufta_20.get():
        try:
            DATASTREAM(int(enter_mufta_20.get()), 'Ecoplast', 42520, 'Муфта соедин. для труб диам. 20 мм, шт.','Муфта соедин. для труб D20мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Муфта соедин. для труб D20мм"!')
            return() 
    if check_mufta_25.get():
        try:
            DATASTREAM(int(enter_mufta_25.get()), 'Ecoplast', '42525-50', 'Муфта соедин. для труб диам. 25 мм, шт.','Муфта соедин. для труб D25мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Муфта соедин. для труб D25мм"!')
            return() 
    if check_mufta_32.get():
        try:
            DATASTREAM(int(enter_mufta_32.get()), 'Ecoplast', 42532, 'Муфта соедин. для труб диам. 32 мм, шт.','Муфта соедин. для труб D32мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Муфта соедин. для труб D32мм"!')
            return() 
    if check_mufta_40.get():
        try:
            DATASTREAM(int(enter_mufta_40.get()), 'Ecoplast', 42540, 'Муфта соедин. для труб диам. 40 мм, шт.','Муфта соедин. для труб D40мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Муфта соедин. для труб D40мм"!')
            return() 
    if check_mufta_50.get():
        try:
            DATASTREAM(int(enter_mufta_50.get()), 'Ecoplast', 42550, 'Муфта соедин. для труб диам. 50 мм, шт.','Муфта соедин. для труб D50мм').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Муфта соедин. для труб D50мм"!')
            return() 
    if check_povorot_16.get():
        try:
            DATASTREAM(int(enter_povorot_16.get()), 'Ecoplast', 43216, 'Гибкий поворот для труб диам. 16 мм, шт.','Поворот д.16').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Поворот д.16"!')
            return() 
    if check_povorot_20.get():
        try:
            DATASTREAM(int(enter_povorot_20.get()), 'Ecoplast', 43220, 'Гибкий поворот для труб диам. 20 мм, шт.','Поворот д.20').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Поворот д.20"!')
            return() 
    if check_povorot_25.get():
        try:
            DATASTREAM(int(enter_povorot_25.get()), 'Ecoplast', 43225, 'Гибкий поворот для труб диам. 25 мм, шт.','Поворот д.25').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Поворот д.25"!')
            return()            
    if check_povorot_32.get():
        try:
            DATASTREAM(int(enter_povorot_32.get()), 'Ecoplast', 43232, 'Гибкий поворот для труб диам. 32 мм, шт.','Поворот д.32').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Поворот д.32"!')
            return()            
    if check_povorot_40.get():
        try:
            DATASTREAM(int(enter_povorot_40.get()), 'Ecoplast', 43240, 'Гибкий поворот для труб диам. 40 мм, шт.','Поворот д.40').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Поворот д.40"!')
            return()            
# ГОФРА/КОРОБА: ЛОТОК ПЕРФОРИРОВАННЫЙ
    if check_lotok_perf_50_50_3000.get():
        try:
            CRAZY(int(enter_lotok_perf_50_50_3000.get()), 'https://crazyservice.by/catalog/lotok_metallicheskij_perforirovannyj/lotok-perforirovannyy-50kh50kh3000-0-55mm-ekf/', 'Лоток перфорированный 50х50х3000-0,55мм EKF, м.', 'Лоток перфорированный 50х50х3000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Лоток перфорированный 50х50х3000"!')
            return()
    if check_lotok_perf_50_100_3000.get():
        try:
            CRAZY(int(enter_lotok_perf_50_100_3000.get()), 'https://crazyservice.by/catalog/lotok_metallicheskij_perforirovannyj/lotok-perforirovannyy-50kh100kh3000-0-55mm-ekf/', 'Лоток перфорированный 50х100х3000-0,55мм EKF, м.', 'Лоток перфорированный 50х100х3000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Лоток перфорированный 50х100х3000"!')
            return()
    if check_lotok_perf_50_150_3000.get():
        try:
            CRAZY(int(enter_lotok_perf_50_150_3000.get()), 'https://crazyservice.by/catalog/lotok_metallicheskij_perforirovannyj/lotok-perforirovannyy-50kh150kh3000-0-55mm-ekf/', 'Лоток перфорированный 50х150х3000-0,55мм EKF, м.', 'Лоток перфорированный 50х150х3000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Лоток перфорированный 50х150х3000"!')
            return()
    if check_lotok_perf_50_200_3000.get():
        try:
            CRAZY(int(enter_lotok_perf_50_200_3000.get()), 'https://crazyservice.by/catalog/lotok_metallicheskij_perforirovannyj/lotok-perforirovannyy-50kh200kh3000-0-55mm-ekf/', 'Лоток перфорированный 50х200х3000-0,55мм EKF, м.', 'Лоток перфорированный 50х200х3000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Лоток перфорированный 50х200х3000"!')
            return()
# ШКАФЫ: TWT НАСТЕННЫЕ NEXT
    if check_wall_twt_next_6u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_6u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-6U-6x4-BK', 'Шкаф настенный TWT серии Next, 6U 550x450, стеклянная дверь, черный, шт.', 'TWT Next 6U 550x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 6U 550x450"!')
            return()
    if check_wall_twt_next_6u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_6u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-6U-6x6-BK', 'Шкаф настенный TWT серии Next, 6U 550x600, стеклянная дверь, черный, шт.', 'TWT Next 6U 550x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 6U 550x600"!')
            return()
    if check_wall_twt_next_9u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_9u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-9U-6x4-BK', 'Шкаф настенный TWT серии Next, 9U 550x450, стеклянная дверь, черный, шт.', 'TWT Next 9U 550x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 9U 550x450"!')
            return()
    if check_wall_twt_next_9u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_9u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-9U-6x6-BK', 'Шкаф настенный TWT серии Next, 9U 550x600, стеклянная дверь, черный, шт.', 'TWT Next 9U 550x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 9U 550x600"!')
            return()
    if check_wall_twt_next_12u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_12u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-12U-6x4-BK', 'Шкаф настенный TWT серии Next, 12U 550x450, стеклянная дверь, черный, шт.', 'TWT Next 12U 550x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 12U 550x450"!')
            return()
    if check_wall_twt_next_12u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_12u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-12U-6x6-BK', 'Шкаф настенный TWT серии Next, 12U 550x600, стеклянная дверь, черный, шт.', 'TWT Next 12U 550x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 12U 550x600"!')
            return()
    if check_wall_twt_next_15u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_15u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-15U-6x4-BK', 'Шкаф настенный TWT серии Next, 15U 550x450, стеклянная дверь, черный, шт.', 'TWT Next 15U 550x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 15U 550x450"!')
            return()
    if check_wall_twt_next_15u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_next_15u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWNG-15U-6x6-BK', 'Шкаф настенный TWT серии Next, 15U 550x600, стеклянная дверь, черный, шт.', 'TWT Next 15U 550x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Next 15U 550x600"!')
            return()
# ШКАФЫ: TWT НАСТЕННЫЕ PRO
    if check_wall_twt_pro_6u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_6u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-6U-6x4-GY', 'Шкаф настенный TWT серии Pro, 6U 600x450, стеклянная дверь, шт.', 'TWT Pro настенный 6U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 6U 600x450"!')
            return()
    if check_wall_twt_pro_6u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_6u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-6U-6x6-GY', 'Шкаф настенный TWT серии Pro, 6U 600x600, стеклянная дверь, шт.', 'TWT Pro настенный 6U 600x600').find_price()    
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 6U 600x600"!')
            return()
    if check_wall_twt_pro_9u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_9u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-9U-6x4-GY', 'Шкаф настенный TWT серии Pro, 9U 600x450, стеклянная дверь, шт.', 'TWT Pro настенный 9U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 9U 600x450"!')
            return()
    if check_wall_twt_pro_9u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_9u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-9U-6x6-GY', 'Шкаф настенный TWT серии Pro, 9U 600x600, стеклянная дверь, шт.', 'TWT Pro настенный 9U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 9U 600x600"!')
            return()
    if check_wall_twt_pro_12u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_12u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-12U-6x4-GY', 'Шкаф настенный TWT серии Pro, 12U 600x450, стеклянная дверь, шт.', 'TWT Pro настенный 12U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 12U 600x450"!')
            return()
    if check_wall_twt_pro_12u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_12u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-12U-6x6-GY', 'Шкаф настенный TWT серии Pro, 12U 600x600, стеклянная дверь, шт.', 'TWT Pro настенный 12U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 12U 600x600"!')
            return()
    if check_wall_twt_pro_15u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_15u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-15U-6x4-GY', 'Шкаф настенный TWT серии Pro, 15U 600x450, стеклянная дверь, шт.', 'TWT Pro настенный 15U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 15U 600x450"!')
            return()
    if check_wall_twt_pro_15u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_15u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-15U-6x6-GY', 'Шкаф настенный TWT серии Pro, 15U 600x600, стеклянная дверь, шт.', 'TWT Pro настенный 15U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 15U 600x600"!')
            return()
    if check_wall_twt_pro_18u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_18u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-18U-6x4-GY', 'Шкаф настенный TWT серии Pro, 18U 600x450, стеклянная дверь, шт.', 'TWT Pro настенный 18U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 18U 600x450"!')
            return()
    if check_wall_twt_pro_18u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_18u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-18U-6x6-GY', 'Шкаф настенный TWT серии Pro, 18U 600x600, стеклянная дверь, шт.', 'TWT Pro настенный 18U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 18U 600x600"!')
            return()
    if check_wall_twt_pro_22u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_22u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-22U-6x4-GY', 'Шкаф настенный TWT серии Pro, 22U 600x450, стеклянная дверь, шт.', 'TWT Pro настенный 22U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 22U 600x450"!')
            return()
    if check_wall_twt_pro_22u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_22u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-22U-6x6-GY', 'Шкаф настенный TWT серии Pro, 22U 600x600, стеклянная дверь, шт.', 'TWT Pro настенный 22U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 22U 600x600"!')
            return()
    if check_wall_twt_pro_27u_6_4.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_27u_6_4.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-27U-6x4-GY', 'Шкаф настенный TWT серии Pro, 27U 600x450, стеклянная дверь, шт.', 'TWT Pro настенный 27U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 27U 600x450"!')
            return()
    if check_wall_twt_pro_27u_6_6.get():
        try:
            DATASTREAM(int(enter_wall_twt_pro_27u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBWPG-27U-6x6-GY', 'Шкаф настенный TWT серии Pro, 27U 600x600, стеклянная дверь, шт.', 'TWT Pro настенный 27U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный TWT Pro 27U 600x600"!')
            return()
# ШКАФЫ: TWT НАПОЛЬНЫЕ PRO
    if check_floor_twt_pro_18u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_18u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-18U-6x6-G1', 'Шкаф напольный TWT серии Pro, 18U 600x600, стеклянная дверь, шт.', 'TWT Pro 18U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 18U 600x600"!')
            return()
    if check_floor_twt_pro_18u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_18u_6_8.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-18U-6x8-G1', 'Шкаф напольный TWT серии Pro, 18U 600x800, стеклянная дверь, шт.', 'TWT Pro 18U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 18U 600x800"!')
            return()
    if check_floor_twt_pro_18u_6_10.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_18u_6_10.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-18U-6x10-G1', 'Шкаф напольный TWT серии Pro, 18U 600x1000, стеклянная дверь, шт.', 'TWT Pro 18U 600x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 18U 600x1000"!')
            return()
    if check_floor_twt_pro_22u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_22u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-22U-6x6-G1', 'Шкаф напольный TWT серии Pro, 22U 600x600, стеклянная дверь, шт.', 'TWT Pro 22U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 22U 600x600"!')
            return()
    if check_floor_twt_pro_22u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_22u_6_8.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-22U-6x8-G1', 'Шкаф напольный TWT серии Pro, 22U 600x800, стеклянная дверь, шт.', 'TWT Pro 22U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 22U 600x800"!')
            return()
    if check_floor_twt_pro_22u_6_10.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_22u_6_10.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-22U-6x10-G1', 'Шкаф напольный TWT серии Pro, 22U 600x1000, стеклянная дверь, шт.', 'TWT Pro 22U 600x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 22U 600x1000"!')
            return()
    if check_floor_twt_pro_32u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_32u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-32U-6x6-G1', 'Шкаф напольный TWT серии Pro, 32U 600x600, стеклянная дверь, шт.', 'TWT Pro 32U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 32U 600x600"!')
            return()
    if check_floor_twt_pro_32u_6_10.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_32u_6_10.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-32U-6x10-G1', 'Шкаф напольный TWT серии Pro, 32U 600x1000, стеклянная дверь, шт.', 'TWT Pro 32U 600x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 32U 600x1000"!')
            return()
    if check_floor_twt_pro_37u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_37u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-37U-6x6-G1', 'Шкаф напольный TWT серии Pro, 37U 600x600, стеклянная дверь, шт.', 'TWT Pro 37U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 37U 600x600"!')
            return()
    if check_floor_twt_pro_37u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_37u_6_8.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-37U-6x8-G1', 'Шкаф напольный TWT серии Pro, 37U 600x800, стеклянная дверь, шт.', 'TWT Pro 37U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 37U 600x800"!')
            return()
    if check_floor_twt_pro_37u_6_10.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_37u_6_10.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-37U-6x10-G1', 'Шкаф напольный TWT серии Pro, 37U 600x1000, стеклянная дверь, шт.', 'TWT Pro 37U 600x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 37U 600x1000"!')
            return()
    if check_floor_twt_pro_42u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_42u_6_8.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-42U-6x8-G1', 'Шкаф напольный TWT серии Pro, 42U 600x800, стеклянная дверь, шт.', 'TWT Pro 42U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 42U 600x800"!')
            return()
    if check_floor_twt_pro_42u_6_10.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_42u_6_10.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-42U-6x10-G1', 'Шкаф напольный TWT серии Pro, 42U 600x1000, стеклянная дверь, шт.', 'TWT Pro 42U 600x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 42U 600x1000"!')
            return()
    if check_floor_twt_pro_42u_6_12.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_42u_6_12.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-42U-6x12-G1', 'Шкаф напольный TWT серии Pro, 42U 600x1200, стеклянная дверь, шт.', 'TWT Pro 42U 600x1200').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 42U 600x1200"!')
            return()
    if check_floor_twt_pro_42u_8_8.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_42u_8_8.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-42U-8x8-G1', 'Шкаф напольный TWT серии Pro, 42U 800x800, стеклянная дверь, шт.', 'TWT Pro 42U 800x800').find_price()    
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 42U 800x800"!')
            return()
    if check_floor_twt_pro_42u_8_10.get():
        floor_twt_pro_42u_8_10 = 0
        try:
            DATASTREAM(int(enter_floor_twt_pro_42u_8_10.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-42U-8x10-G1', 'Шкаф напольный TWT серии Pro, 42U 800x1000, стеклянная дверь, шт.', 'TWT Pro 42U 800x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 42U 800x1000"!')
            return()
    if check_floor_twt_pro_42u_8_12.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_42u_8_12.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-42U-8x12-G1', 'Шкаф напольный TWT серии Pro, 42U 800x1200, стеклянная дверь, шт.', 'TWT Pro 42U 800x1200').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 42U 800x1200"!')
            return()
    if check_floor_twt_pro_47u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_47u_6_6.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-47U-6x6-G1', 'Шкаф напольный TWT серии Pro, 47U 600x600, стеклянная дверь, шт.', 'TWT Pro 47U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 47U 600x600"!')
            return()
    if check_floor_twt_pro_47u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_47u_6_8.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-47U-6x8-G1', 'Шкаф напольный TWT серии Pro, 47U 600x800, стеклянная дверь, шт.', 'TWT Pro 47U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 47U 600x800"!')
            return()
    if check_floor_twt_pro_47u_6_12.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_47u_6_12.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-47U-6x12-G1', 'Шкаф напольный TWT серии Pro, 47U 600x1200, стеклянная дверь, шт.', 'TWT Pro 47U 600x1200').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 47U 600x1200"!')
            return()
    if check_floor_twt_pro_47u_8_8.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_47u_8_8.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-47U-8x8-G1', 'Шкаф напольный TWT серии Pro, 47U 800x800, стеклянная дверь, шт.', 'TWT Pro 47U 800x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 47U 800x800"!')
            return()
    if check_floor_twt_pro_47u_8_10.get():
        try:
            DATASTREAM(int(enter_floor_twt_pro_47u_8_10.get()), 'Шкафы TWT-LANMASTER', 'TWT-CBB-47U-8x10-G1', 'Шкаф напольный TWT серии Pro, 47U 800x1000, стеклянная дверь, шт.', 'TWT Pro 47U 800x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный TWT Pro 47U 800x1000"!')
            return()
# ШКАФЫ: ЦМО НАСТЕННЫЕ
    if check_wall_cmo_6u_6_480.get():
        try:
            DATASTREAM(int(enter_wall_cmo_6u_6_480.get()), 'Шкафы ЦМО', 'ШРН-6.480', 'Шкаф настенный 6U (600х480) дверь стекло, шт.', 'ЦМО 6U 600x480').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 6U 600x480"!')
            return()
    if check_wall_cmo_6u_6_650.get():
        try:
            DATASTREAM(int(enter_wall_cmo_6u_6_650.get()), 'Шкафы ЦМО', 'ШРН-6.650', 'Шкаф настенный 6U (600х650) дверь стекло, шт.', 'ЦМО 6U 600x650').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 6U 600x650"!')
            return()
    if check_wall_cmo_9u_6_480.get():
        try:
            DATASTREAM(int(enter_wall_cmo_9u_6_480.get()), 'Шкафы ЦМО', 'ШРН-9.480', 'Шкаф настенный 9U (600х480) дверь стекло, шт.', 'ЦМО 9U 600x480').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 9U 600x480"!')
            return()
    if check_wall_cmo_9u_6_650.get():
        try:
            DATASTREAM(int(enter_wall_cmo_9u_6_650.get()), 'Шкафы ЦМО', 'ШРН-9.650', 'Шкаф настенный 9U (600х650) дверь стекло, шт.', 'ЦМО 9U 600x650').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 9U 600x650"!')
            return()
    if check_wall_cmo_12u_6_480.get():
        try:
            DATASTREAM(int(enter_wall_cmo_12u_6_480.get()), 'Шкафы ЦМО', 'ШРН-12.480', 'Шкаф настенный 12U (600х480) дверь стекло, шт.', 'ЦМО 12U 600x480').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 12U 600x480"!')
            return()
    if check_wall_cmo_12u_6_650.get():
        try:
            DATASTREAM(int(enter_wall_cmo_12u_6_650.get()), 'Шкафы ЦМО', 'ШРН-12.650', 'Шкаф настенный 12U (600х650) дверь стекло, шт.', 'ЦМО 12U 600x650').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 12U 600x650"!')
            return()
    if check_wall_cmo_15u_6_480.get():
        try:
            DATASTREAM(int(enter_wall_cmo_15u_6_480.get()), 'Шкафы ЦМО', 'ШРН-15.480', 'Шкаф настенный 15U (600х480) дверь стекло, шт.', 'ЦМО 15U 600x480').find_price()    
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 15U 600x480"!')
            return()
    if check_wall_cmo_15u_6_650.get():
        try:
            DATASTREAM(int(enter_wall_cmo_15u_6_650.get()), 'Шкафы ЦМО', 'ШРН-15.650', 'Шкаф настенный 15U (600х650) дверь стекло, шт.', 'ЦМО 15U 600x650').find_price() 
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф настенный ЦМО 15U 600x650"!')
            return()
# ШКАФЫ: ЦМО НАПОЛЬНЫЕ
    if check_floor_cmo_18u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_cmo_18u_6_6.get()), 'Шкафы ЦМО', 'ШТК-М-18.6.6-1ААА', 'Шкаф напольный 18U (600х600) дверь стекло, шт.', 'ЦМО 18U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 18U 600x600"!')
            return()
    if check_floor_cmo_18u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_cmo_18u_6_8.get()), 'Шкафы ЦМО', 'ШТК-М-18.6.8-1ААА', 'Шкаф напольный 18U (600х800) дверь стекло, шт.', 'ЦМО 18U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 18U 600x800"!')
            return()
    if check_floor_cmo_22u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_cmo_22u_6_6.get()), 'Шкафы ЦМО', 'ШТК-М-22.6.6-1ААА', 'Шкаф напольный 22U (600х600) дверь стекло, шт.', 'ЦМО 22U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 22U 600x600"!')
            return()
    if check_floor_cmo_22u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_cmo_22u_6_8.get()), 'Шкафы ЦМО', 'ШТК-М-22.6.8-1ААА', 'Шкаф напольный 22U (600х800) дверь стекло, шт.', 'ЦМО 22U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 22U 600x800"!')
            return()
    if check_floor_cmo_22u_6_10.get():
        try:
            DATASTREAM(int(enter_floor_cmo_22u_6_10.get()), 'Шкафы ЦМО', 'ШТК-М-22.6.10-1ААА', 'Шкаф напольный 22U (600х1000) дверь стекло, шт.', 'ЦМО 22U 600x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 22U 600x1000"!')
            return()
    if check_floor_cmo_27u_6_6.get():
        try:
            DATASTREAM(int(enter_floor_cmo_27u_6_6.get()), 'Шкафы ЦМО', 'ШТК-М-27.6.6-1ААА', 'Шкаф напольный 27U (600х600) дверь стекло, шт.', 'ЦМО 27U 600x600').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 27U 600x600"!')
            return()
    if check_floor_cmo_27u_6_8.get():
        try:
            DATASTREAM(int(enter_floor_cmo_27u_6_8.get()), 'Шкафы ЦМО', 'ШТК-М-27.6.8-1ААА', 'Шкаф напольный 27U (600х800) дверь стекло, шт.', 'ЦМО 27U 600x800').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 27U 600x800"!')
            return()
    if check_floor_cmo_27u_6_10.get():
        try:
            DATASTREAM(int(enter_floor_cmo_27u_6_10.get()), 'Шкафы ЦМО', 'ШТК-М-27.6.10-1ААА', 'Шкаф напольный 27U (600х1000) дверь стекло, шт.', 'ЦМО 27U 600x1000').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Шкаф напольный ЦМО 27U 600x1000"!')
            return()
# ШКАФЫ: ЩИТЫ МОНТАЖНЫЕ
    if check_smp_00_ip_31.get():
        try:
            ETPROM(int(enter_smp_00_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12094/','Щит с монтажной панелью ЩМП-00 IP31 (270х210х140) EKF PROxima, шт.', 'ЩМП-00 IP31 (270х210х140)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-00 IP31 (270х210х140)"!')
            return()
    if check_smp_01_ip_31.get():
        try:
            ETPROM(int(enter_smp_01_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12095/','Щит с монтажной панелью ЩМП-01 IP31 (410х210х140) EKF PROxima, шт.', 'ЩМП-01 IP31 (410х210х140)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-01 IP31 (410х210х140)"!')
            return()
    if check_smp_02_ip_31.get():
        try:
            ETPROM(int(enter_smp_02_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12096/','Щит с монтажной панелью ЩМП-02 IP31 (250х300х140) EKF PROxima, шт.', 'ЩМП-02 IP31 (250х300х140)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-02 IP31 (250х300х140)"!')
            return()
    if check_smp_03_ip_31.get():
        try:
            ETPROM(int(enter_smp_03_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12214/','Щит с монтажной панелью ЩМП-03 IP31 (350х300х155) EKF PROxima, шт.', 'ЩМП-03 IP31 (350х300х155)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-03 IP31 (350х300х155)"!')
            return()
    if check_smp_04_ip_31.get():
        try:
            ETPROM(int(enter_smp_04_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12097/','Щит с монтажной панелью ЩМП-04 IP31 (400х300х155) EKF PROxima, шт.', 'ЩМП-04 IP31 (400х300х155)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-04 IP31 (400х300х155)"!')
            return()
    if check_smp_05_ip_31.get():
        try:
            ETPROM(int(enter_smp_05_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12098/', 'Щит с монтажной панелью ЩМП-05 IP31 (400х400х155) EKF PROxima, шт.', 'ЩМП-05 IP31 (400х400х155)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-05 IP31 (400х400х155)"!')
            return()
    if check_smp_06_ip_31.get():
        try:
            ETPROM(int(enter_smp_06_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12099/', 'Щит с монтажной панелью ЩМП-06 IP31 (500х400х170) EKF PROxima, шт.', 'ЩМП-06 IP31 (500х400х170)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-06 IP31 (500х400х170)"!')
            return()
    if check_smp_07_ip_31.get():
        try:
            ETPROM(int(enter_smp_07_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12100/', 'Щит с монтажной панелью ЩМП-07 IP31 (700х500х210) EKF PROxima, шт.', 'ЩМП-07 IP31 (700х500х210)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-07 IP31 (700х500х210)"!')
            return() 
    if check_smp_09_ip_31.get():
        try:
            ETPROM(int(enter_smp_09_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12215/', 'Щит с монтажной панелью ЩМП-09 IP31 (600х400х210) EKF PROxima, шт.', 'ЩМП-09 IP31 (600х400х210)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-09 IP31 (600х400х210)"!')
            return()
    if check_smp_11_ip_31.get():
        try:
            ETPROM(int(enter_smp_11_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12423/', 'Щит с монтажной панелью ЩМП-11 IP31 (600х400х400) EKF PROxima, шт.', 'ЩМП-11 IP31 (600х400х400)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-11 IP31 (600х400х400)"!')
            return()
    if check_smp_12_ip_31.get():
        try:
            ETPROM(int(enter_smp_12_ip_31.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12101/', 'Щит с монтажной панелью ЩМП-12 IP31 (600х600х400) EKF PROxima, шт.', 'ЩМП-12 IP31 (600х600х400)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩМП-12 IP31 (600х600х400)"!')
            return()
    if check_srnm_1_ip_54.get():
        try:
            ETPROM(int(enter_srnm_1_ip_54.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12640/', 'Щит с монтажной панелью ЩРНМ-1 IP54 (400х300х220) EKF PROxima, шт.', 'ЩРНМ-1 IP54 (400х300х220)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩРНМ-1 IP54 (400х300х220)"!')
            return()
    if check_srnm_2_ip_54.get():
        try:
            ETPROM(int(enter_srnm_2_ip_54.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12112/', 'Щит с монтажной панелью ЩРНМ-2 IP54 (500х400х220) EKF PROxima, шт.', 'ЩРНМ-2 IP54 (500х400х220)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩРНМ-2 IP54 (500х400х220)"!')
            return()
    if check_srnm_3_ip_54.get():
        try:
            ETPROM(int(enter_srnm_3_ip_54.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12114/', 'Щит с монтажной панелью ЩРНМ-3 IP54 (650х500х220) EKF PROxima, шт.', 'ЩРНМ-3 IP54 (650х500х220)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩРНМ-3 IP54 (650х500х220)"!')
            return()
    if check_srnm_4_ip_54.get():
        try:
            ETPROM(int(enter_srnm_4_ip_54.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12218/', 'Щит с монтажной панелью ЩРНМ-4 IP54 (800х600х250) EKF PROxima, шт.', 'ЩРНМ-4 IP54 (800х600х250)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩРНМ-4 IP54 (800х600х250)"!')
            return()
    if check_srnm_5_ip_54.get():
        try:
            ETPROM(int(enter_srnm_5_ip_54.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/13867/', 'Щит с монтажной панелью ЩРНМ-5 IP54 (1000х650х300) EKF PROxima, шт.', 'ЩРНМ-5 IP54 (1000х650х300)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩРНМ-5 IP54 (1000х650х300)"!')
            return()
    if check_srnm_6_ip_54.get():
        try:
            ETPROM(int(enter_srnm_6_ip_54.get()), 'https://etprom.by/catalog/korpusa_elektroshchitov_i_aksessuary/korpusa_metallicheskie/korpusa_s_montazhnoy_panelyu/12219/', 'Щит с монтажной панелью ЩРНМ-6 IP54 (1200х750х300) EKF PROxima, шт.', 'ЩРНМ-6 IP54 (1200х750х300)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ЩРНМ-6 IP54 (1200х750х300)"!')
            return()
# ШКАФЫ: W&T
    if check_wt_066045.get():
        try:
            ASB(int(enter_wt_066045.get()), 'https://activsb.by/katalog/shkafy-telekommunikacionnye-19/nastennye-shkafy/6u-vysota-368mm/shkaf-19-nastennyj-6u-seryj/chernyj-c066045g/vwt.html','Шкаф 19" настенный 6U серый/черный C066045G/ВWT, шт.', 'W&T 6U 600x450').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "W&T 6U 600x450"!')
            return()
# РЕГИСТРАТОРЫ: HIKVISION
    if check_hik7604niq1.get():
        try:
            AVANT(int(enter_hik7604niq1.get()), 'Каталог', '8077', 'HIKVISION DS-7604NI-Q1, 4-канальный IP-видеорегистратор, 1 жесткий диск до 8TB, питание 12VDC, шт.', 'HIKVISION DS-7604NI-Q1').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7604NI-Q1"!')
            return()
    if check_hik7608niq2.get():
        try:
            AVANT(int(enter_hik7608niq2.get()), 'Каталог', '8252', 'HIKVISION DS-7608NI-Q2, 8-канальный IP-видеорегистратор, 2 жестких диска до 8ТВ, питание 12VDC, шт.', 'HIKVISION DS-7608NI-Q2').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7608NI-Q2"!')
            return()
    if check_hik7616niq2.get():
        try:
            AVANT(int(enter_hik7616niq2.get()), 'Каталог', '8098', 'HIKVISION DS-7616NI-Q2, 16-канальный IP-видеорегистратор, 2 жестких диска до 8ТВ, питание 12VDC, шт.', 'HIKVISION DS-7616NI-Q2').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7616NI-Q2"!')
            return()
    if check_hik7716niq4.get():
        try:
            AVANT(int(enter_hik7716niq4.get()), 'Каталог', '10716', 'HIKVISION DS-7716NI-Q4, 16-канальный IP-видеорегистратор, 4 жестких диска до 6ТВ, питание 100-240VAC, шт.', 'HIKVISION DS-7716NI-Q4').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7716NI-Q4"!')
            return()
    if check_hik7732niq4.get():
        try:
            AVANT(int(enter_hik7732niq4.get()), 'Каталог', '10460', 'HIKVISION DS-7732NI-Q4, 32-канальный IP-видеорегистратор, 4 жестких диска до 6ТВ, питание 100-240VAC, шт.', 'HIKVISION DS-7732NI-Q4').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7732NI-Q4"!')
            return()
    if check_hik7604nik1.get():
        try:
            AVANT(int(enter_hik7604nik1.get()), 'Каталог', '7291', 'HIKVISION DS-7604NI-K1(B), 4-канальный IP-видеорегистратор, 1 жесткий диск, питание 12VDC, шт.', 'HIKVISION DS-7604NI-K1').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7604NI-K1"!')
            return()
    if check_hik7608nik2.get():
        try:
            AVANT(int(enter_hik7608nik2.get()), 'Каталог', '7122', 'HIKVISION DS-7608NI-K2, 8-канальный IP-видеорегистратор, 2 жестких диска, питание 12VDC, шт.', 'HIKVISION DS-7608NI-K2').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7608NI-K2"!')
            return()
    if check_hik7616nik2.get():
        try:
            AVANT(int(enter_hik7616nik2.get()), 'Каталог', '7124', 'HIKVISION DS-7616NI-K2, 16-канальный IP-видеорегистратор, 2 жестких диска, питание 12VDC, шт.', 'HIKVISION DS-7616NI-K2').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7616NI-K2"!')
            return()
    if check_hik_7732ni_k4.get():
        try:
            AVANT(int(enter_hik_7732ni_k4.get()), 'Каталог', '7277', 'HIKVISIONDS-7732NI-K4, 32-канальный IP-видеорегистратор, 4 жестких диска, питание АC100-240В, шт.', 'HIKVISION DS-7732NI-K4').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7732NI-K4"!')
            return()
    if check_hik7604niq1_4p.get():
        try:
            AVANT(int(enter_hik7604niq1_4p.get()), 'Каталог', '8078', 'HIKVISION DS-7604NI-Q1/4P, 4-канальный IP-видеорегистратор (4 канала с поддержкой РоЕ), 1 жесткий диск, питание 12VDC, шт.', 'HIKVISION DS-7604NI-Q1/4P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7604NI-Q1/4P"!')
            return()
    if check_hik7608niq2_8p.get():
        try:
            AVANT(int(enter_hik7608niq2_8p.get()), 'Каталог', '8080', 'HIKVISION DS-7608NI-Q2/8P, 8-канальный IP-видеорегистратор (8 каналов с поддержкой РоЕ), 2 жестких диска, питание 12VDC, шт.', 'HIKVISION DS-7608NI-Q2/8P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7608NI-Q2/8P"!')
            return()
    if check_hik7616niq2_16p.get():
        try:
            AVANT(int(enter_hik7616niq2_16p.get()), 'Каталог', '8178', 'HIKVISION DS-7616NI-Q2/16P, 16-канальный IP-видеорегистратор (16 каналов с поддержкой PoE), 2 жестких диска, питание 12VDC, шт.', 'HIKVISION DS-7616NI-Q2/16P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7616NI-Q2/16P"!')
            return()
    if check_hik7604nik1_4p.get():
        try:
            AVANT(int(enter_hik7604nik1_4p.get()), 'Каталог', '9109', 'HIKVISION DS-7604NI-K1/4P(B), 4-канальный IP-видеорегистратор (4 канала с поддержкой PoE), 1 жесткий диск, питание 48VDC, шт.', 'HIKVISION DS-7604NI-K1/4P(B)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7604NI-K1/4P(B)"!')
            return()
    if check_hik7608nik2_8p.get():
        try:
            AVANT(int(enter_hik7608nik2_8p.get()), 'Каталог', '7123', 'HIKVISION DS-7608NI-K2/8P, 8-канальный IP-видеорегистратор (8 каналов с поддержкой PoE), 2 жестких диска, питание 100-240VAC, шт.', 'HIKVISION DS-7608NI-K2/8P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7608NI-K2/8P"!')
            return()
    if check_hik7616nik2_16p.get():
        try:
            AVANT(int(enter_hik7616nik2_16p.get()), 'Каталог', '6446', 'HIKVISION DS-7616NI-K2/16P, 16-канальный IP-видеорегистратор (16 каналов с поддержкой РоЕ), 2 жестких диска, питание 100-240VAC, шт.', 'HIKVISION DS-7616NI-K2/16P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7616NI-K2/16P"!')
            return()
    if check_hik7116hqhi_k1.get():
        try:
            AVANT(int(enter_hik7116hqhi_k1.get()), 'Каталог', '11057', 'HIKVISION DS-7116HQHI-K1(S), 16-канальный HD-видеорегистратор, 1 жесткий диск, питание 12VDC, шт.', 'HIKVISION DS-7116HQHI-K1(S)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дHIKVISION DS-7116HQHI-K1(S)"!')
            return()
    if check_hikvision_ds_7216hqhi_k2_4audio.get():
        try:
            AVANT(int(enter_hikvision_ds_7216hqhi_k2_4audio.get()), 'Каталог', '9335', 'HIKVISION DS-7216HQHI-K2 4audio, 16-канальный HD-видеорегистратор, 1 жесткий диск до 10TB, питание DC12В, шт.', 'HIKVISION DS-7216HQHI-K2 4audio').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение дDS-7216HQHI-K2 4audio"!')
            return() 
# РЕГИСТРАТОРЫ: HIWATCH
    if check_hiwatch_dsn204.get():
        try:
            AVANT(int(enter_hiwatch_dsn204.get()), 'Каталог', '9323', 'HiWatch DS-N204(B), 4-канальный IP-видеорегистратор, 1 жесткий диск, питание 12VDC, шт.', 'HIWATCH DS-N204').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-N204(B)"!')
            return()
    if check_hiwatch_dsn208.get():
        try:
            AVANT(int(enter_hiwatch_dsn208.get()), 'Каталог', '7361', 'HiWatch DS-N208(B), 8-канальный IP-видеорегистратор, 1 жесткий диск, питание 12VDC, шт.', 'HIWATCH DS-N208').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-N208(B)"!')
            return()
    if check_hiwatch_dsn204p.get():
        try:
            AVANT(int(enter_hiwatch_dsn204p.get()), 'Каталог', '8785', 'HiWatch DS-N204P(B), 4-канальный IP-видеорегистратор (4 канала с поддержкой РоЕ), 1 жесткий диск, питание 48VDC, шт.', 'HIWATCH DS-N204P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-N204P(B)"!')
            return()
    if check_hiwatch_dsn208p.get():
        try:
            AVANT(int(enter_hiwatch_dsn208p.get()), 'Каталог', '8892', 'HiWatch DS-N208P(B), 8-канальный IP-видеорегистратор (8 каналов с поддержкой РоЕ), 1 жесткий диск, питание 48VDC, шт.', 'HIWATCH DS-N208P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-N208P(B)"!')
            return()
# РЕГИСТРАТОРЫ: DAHUA
    if check_dhi_nvr4116hs_4216.get():
        try:
            SFERA(int(enter_dhi_nvr4116hs_4216.get()), 'https://secur.by/katalog/videonablyudenie/ustrojstva-zapisi/videoregistratory-setevye/dhi-nvr4116hs-4ks2.html', 'DAHUA DHI-NVR4116HS-4KS2 Видеорегистратор сетевой, 16 каналов, пропускная способность 80Mbps, Smart H.265+/H.265/Smart H.264+/H.264, поддержка разрешения записи до 8MP, поддержка видеоаналитики камер, шт.', 'DHI-NVR4116HS-4KS2').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DHI-NVR4116HS-4KS2"!')
            return()
# КАМЕРЫ: IP HIKVISION
    if check_hik2cd1023g0.get():
        try:
            AVANT(int(enter_hik2cd1023g0.get()), 'Каталог', '7787', 'HIKVISION DS-2CD1023G0-I, уличная IP-видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1023G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1023G0-I"!')
            return()
    if check_hik2cd1623g0.get():
        try:
            AVANT(int(enter_hik2cd1623g0.get()), 'Каталог', '7792', 'HIKVISION DS-2CD1623G0-I, уличная IP-видеокамера, 2MP, вариофокальный объектив, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1623G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1623G0-I"!')
            return()
    if check_hik2cd1123g0.get():
        try:
            AVANT(int(enter_hik2cd1123g0.get()), 'Каталог', '7789', 'HIKVISION DS-2CD1123G0-I, антивандальная уличная/внутренняя IP-видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1123G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1123G0-I"!')
            return()
    if check_hik2cd2121g0_is.get():
        try:
            AVANT(int(enter_hik2cd2121g0_is.get()), 'Каталог', '8473', 'HIKVISION DS-2CD2121G0-IS, антивандальная уличная/внутренняя IP-видеокамера, 2MP, разрешение 1920x1080, канал звука (подключение внешнего микрофона), дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD2121G0-IS').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD2121G0-IS"!')
            return()
    if check_hik2cd1723g0.get():
        try:
            AVANT(int(enter_hik2cd1723g0.get()), 'Каталог', '7795', 'HIKVISION DS-2CD1723G0-I, антивандальная уличная/внутренняя IP-видеокамера, вариофокальный объектив, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1723G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1723G0-I"!')
            return()
    if check_hik2cd2420fi.get():
        try:
            AVANT(int(enter_hik2cd2420fi.get()), 'Каталог', '6100', 'HIKVISION DS-2CD2420F-I, внутренняя IP-видеокамера, встроенный микрофон, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD2420F-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD2420F-I"!')
            return()
    if check_hik2cd1043g0.get():
        try:
            AVANT(int(enter_hik2cd1043g0.get()), 'Каталог', '7785', 'HIKVISION DS-2CD1043G0-I, уличная IP-видеокамера, 4MP, разрешение 2560x1440, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1043G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1043G0-I"!')
            return()
    if check_hik2cd1643g0.get():
        try:
            AVANT(int(enter_hik2cd1643g0.get()), 'Каталог', '7790', 'HIKVISION DS-2CD1643G0-I, уличная IP-видеокамера, 4MP, вариофокальный объектив, разрешение 2560x1440, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1643G0-I').find_price()
            
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1643G0-I"!')
            return()
    if check_hik2cd1143g0.get():
        try:
            AVANT(int(enter_hik2cd1143g0.get()), 'Каталог', '7991', 'HIKVISION DS-2CD1143G0-I, антивандальная уличная/внутренняя IP-видеокамера, 4MP, разрешение 2560x1440, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1143G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1143G0-I"!')
            return()
    if check_hik2cd1743g0.get():
        try:
            AVANT(int(enter_hik2cd1743g0.get()), 'Каталог', '7880', 'HIKVISION DS-2CD1743G0-I, антивандальная уличная/внутренняя IP-видеокамера, вариофокальный объектив, 4MP, разрешение 2560x1440, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD1743G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD1743G0-I"!')
            return()
    if check_hik2cd2643g0_izs.get():
        try:
            AVANT(int(enter_hik2cd2643g0_izs.get()), 'Каталог', '9816', 'HIKVISION DS-2CD2643G1-IZS, уличная IP-видеокамера, вариофокальный объектив, 4MP, разрешение 2560x1440, дальность ИК подсветки до 50м, шт.', 'HIKVISION DS-2CD2643G1-IZS').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD2643G1-IZS"!')
            return()  
    if check_hik2cd2123g0_i.get():
        try:
            AVANT(int(enter_hik2cd2123g0_i.get()), 'Каталог', '8292', 'HIKVISION DS-2CD2123G0-I, антивандальная IP-видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD2123G0-I').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD2123G0-I"!')
            return()
    if check_hik2cd2123g0_iu.get():
        try:
            AVANT(int(enter_hik2cd2123g0_iu.get()), 'Каталог', '10434', 'HIKVISION DS-2CD2123G0-IU, антивандальная IP-видеокамера, 2MP, разрешение 1920x1080, канал звука (встроенный микрофон), дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CD2123G0-IU').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD2123G0-IU"!')
            return()
    if check_hik2cd2721g0_is.get():
        try:
            AVANT(int(enter_hik2cd2721g0_is.get()), 'Каталог', '8685', 'HIKVISION DS-2CD2721G0-IS, антивандальная уличная/внутренняя IP видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, канал звука (подключение внешнего микрофона), шт.', 'HIKVISION DS-2CD2721G0-IS').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CD2721G0-IS"!')
            return()  
# КАМЕРЫ: HD HIKVISION
    if check_hik2ce76d3t_itmf.get():
        try:
            AVANT(int(enter_hik2ce76d3t_itmf.get()), 'Каталог', '11073', 'HIKVISION DS-2CE76D3T-ITMF, уличная HD-видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIKVISION DS-2CE76D3T-ITMF').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CE76D3T-ITMF"!')
            return()
    if check_hik2ce19d3t_it3zf.get():
        try:
            AVANT(int(enter_hik2ce19d3t_it3zf.get()), 'Каталог', '11072', 'HIKVISION DS-2CE19D3T-IT3ZF, уличная HD-видеокамера, 2MP, моторизованный вариофокальный объектив, разрешение 1920x1080, дальность ИК подсветки до 70м, шт.', 'HIKVISION DS-2CE19D3T-IT3ZF').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CE19D3T-IT3ZF"!')
            return()
    if check_hikvision_ds_2ce16d3t_it3f.get():
        try:
            AVANT(int(enter_hikvision_ds_2ce16d3t_it3f.get()), 'Каталог', '11274', 'HIKVISION DS-2CE16D3T-IT3F 2,8мм, уличная HD-видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 50м, шт.', 'HIKVISION DS-2CE16D3T-IT3F').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIKVISION DS-2CE16D3T-IT3F"!')
            return()
# КАМЕРЫ: IP HIWATCH
    if check_hiwatch_dsi200.get():
        try:
            AVANT(int(enter_hiwatch_dsi200.get()), 'Каталог', '7140', 'HiWatch DS-I200 (В), уличная IP-видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIWATCH DS-I200').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-I200 (В)"!')
            return()
    if check_hiwatch_dsi206.get():
        try:
            AVANT(int(enter_hiwatch_dsi206.get()), 'Каталог', '7153', 'HiWatch DS-I206, уличная IP-видеокамера, вариофокальный объектив, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIWATCH DS-I206').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-I206"!')
            return()
    if check_hiwatch_dsi202.get():
        try:
            AVANT(int(enter_hiwatch_dsi202.get()), 'Каталог', '7112', 'HiWatch DS-I202, антивандальная уличная IP-видеокамера, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIWATCH DS-I202').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-I202"!')
            return()
    if check_hiwatch_dsi214.get():
        try:
            AVANT(int(enter_hiwatch_dsi214.get()), 'Каталог', '8084', 'HiWatch DS-I214, внутренняя IP-видеокамера, встроенный микрофон, 2MP, разрешение 1920x1080, дальность ИК подсветки до 30м, шт.', 'HIWATCH DS-I214').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-I214"!')
            return()
    if check_hiwatch_dsi400.get():
        try:
            AVANT(int(enter_hiwatch_dsi400.get()), 'Каталог', '8089', 'HiWatch DS-I400, уличная IP-видеокамера, 4MP, разрешение 2560x1440, дальность ИК подсветки до 30м, шт.', 'HIWATCH DS-I400').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-I400"!')
            return()
    if check_hiwatch_dsi456.get():
        try:
            AVANT(int(enter_hiwatch_dsi456.get()), 'Каталог', '8162', 'HiWatch DS-I456, уличная IP-видеокамера, вариофокальный объектив, 4MP, разрешение 2560x1440, дальность ИК подсветки до 30м, шт.', 'HIWATCH DS-I456').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-I456"!')
            return()
# КАМЕРЫ: HD HIWATCH
    if check_hiwatch_ds_t203.get():
        try:
            AVANT(int(enter_hiwatch_ds_t203.get()), 'Каталог', '6906', 'HiWatch DS-T203, цветная купольная 2-мегапиксельная видеокамера, разрешение 1920x1080, дальность ИК подсветки до 20м, шт.', 'HIWATCH DS-T203').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HIWATCH DS-T203"!')
            return()
# КАМЕРЫ: DAHUA
    if check_ez_ipc_b1b40p_0360b.get():
        try:
            SFERA(int(enter_ez_ipc_b1b40p_0360b.get()), 'https://secur.by/katalog/videonablyudenie/videokamery/setevye-ip/cilindricheskie/ez-ipc-b1b40p-0360b.html', 'DAHUA EZ-IPC-B1B40P-0360B Сетевая камера цилиндрическая, 4MP (2688x1520/20fps), 1/3" CMOS, день/ночь (механический ИК-фильтр), объектив f3.6mm/F2.0, угол обзора 81°, шт.', 'EZ-IPC-B1B40P-0360B').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "EZ-IPC-B1B40P-0360B"!')
            return()
# ДЛЯ ВИДЕО: ЖЕСТКИЕ ДИСКИ
    if check_hdd_1.get():
        try:
            AVANT(int(enter_hdd_1.get()), 'HDD,Мониторы и т.п.', '8344', 'Жесткий диск 1Tb WD Purple для видеонаблюдения WD10PURZ | SATA 3.0 | 64 MB | 5400 rpm | 3,5", шт.', 'HDD WD 1 TB').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HDD WD 1 TB"!')
            return()
    if check_hdd_2.get():
        try:
            AVANT(int(enter_hdd_2.get()), 'HDD,Мониторы и т.п.', '8619', 'Жесткий диск 2Tb WD Purple для видеонаблюдения WD20PURZ | SATA 3.0 | 64 MB | 5400 rpm | 3,5", шт.', 'HDD WD 1 TB').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HDD WD 2 TB"!')
            return()
    if check_hdd_4.get():
        try:
            AVANT(int(enter_hdd_4.get()), 'HDD,Мониторы и т.п.', '7967', 'Жесткий диск 4Tb WD Purple для видеонаблюдения WD40PURZ | SATA 3.0 | 64 MB | 5400 rpm | 3,5", шт.', 'HDD WD 1 TB').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HDD WD 4 TB"!')
            return()
    if check_hdd_6.get():
        try:
            AVANT(int(enter_hdd_6.get()), 'HDD,Мониторы и т.п.', '6134', 'Жесткий диск 6Tb WD Purple для видеонаблюдения WD60PURZ | SATA 3.0 | 64 MB | 5400 rpm | 3,5", шт.', 'HDD WD 1 TB').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HDD WD 6 TB"!')
            return()
    if check_hdd_8.get():
        try:
            AVANT(int(enter_hdd_8.get()), 'HDD,Мониторы и т.п.', '10824', 'Жесткий диск 8Tb WD Purple для видеонаблюдения WD82PURZ | SATA 3.0 | 256 MB | 7200 rpm | 3,5", шт.', 'HDD WD 1 TB').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HDD WD 8 TB"!')
            return()
    if check_hdd_10.get():
        try:
            AVANT(int(enter_hdd_10.get()), 'HDD,Мониторы и т.п.', '11754', 'Жесткий диск 10Tb WD Purple для видеонаблюдения WD102PURZ | SATA 3.0 | 256 MB | 7200 rpm | 3,5", шт.', 'HDD WD 1 TB').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HDD WD 10 TB"!')
            return()
    if check_hdd_12.get():
        try:
            AVANT(int(enter_hdd_12.get()), 'HDD,Мониторы и т.п.', '10146', 'Жесткий диск 12Tb WD Purple для видеонаблюдения WD121PURZ | SATA 3.0 | 256 MB | 7200 rpm | 3,5", шт.', 'HDD WD 1 TB').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "HDD WD 10 TB"!')
            return()
# ДЛЯ ВИДЕО: КРОНШТЕЙНЫ
    if check_DS_1260ZJ.get():
        try:
            AVANT(int(enter_DS_1260ZJ.get()), 'Каталог', '5178', 'DS-1260ZJ Монтажная коробка для цилиндрических камер. Алюминиевый сплав, белый, Ф88.5мм, шт.', 'Кронштейн DS-1260ZJ').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Кронштейн DS-1260ZJ"!')
            return()
    if check_DS_1280ZJ_S.get():
        try:
            AVANT(int(enter_DS_1280ZJ_S.get()), 'Каталог', '6357', 'DS-1280ZJ-S Монтажная коробка для цилиндрических камер усиленная. Алюминиевый сплав, белый, Ф137x53.4x164.8mm, шт.', 'Кронштейн DS-1280ZJ-S').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Кронштейн DS-1280ZJ-S"!')
            return()
    if check_DS_1280ZJ_DM18.get():
        try:
            AVANT(int(enter_DS_1280ZJ_DM18.get()), 'Каталог', '5405', 'DS-1280ZJ-DM18 Монтажная коробка для купольных камер. Алюминиевый сплав, белый, Ф101 мм,, шт.', 'Кронштейн DS-1280ZJ-DM18').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Кронштейн DS-1280ZJ-DM18"!')
            return()
    if check_DH_PFA152_E.get():
        try:
            SFERA(int(enter_DH_PFA152_E.get()), 'https://secur.by/katalog/videonablyudenie/kozhuhi-kronshtejny/dh-pfa152-e.html', 'DAHUA DH-PFA152-E Кронштейн для установки PTZ-камер, купольных и цилиндрических камер на столб, корпус алюминий, максимальная нагрузка 3kg, обжимаемый диаметр 80-150mm, шт.', 'DH-PFA152-E').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DH-PFA152-E"!')
            return()
    if check_DH_PFA134.get():
        try:
            SFERA(int(enter_DH_PFA134.get()), 'https://secur.by/katalog/videonablyudenie/kozhuhi-kronshtejny/dh-pfa134.html', 'DAHUA DH-PFA134 Монтажная коробка для установки цилиндрических (HAC-HFW, IPC-HFW) камер, корпус алюминий, максимальная нагрузка 1kg, шт.', 'DH-PFA134').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DH-PFA134"!')
            return()
# ДЛЯ ВИДЕО: МОНИТОРЫ
    if check_AOC_E2270SWN.get():
        try:
            AVANT(int(enter_AOC_E2270SWN.get()), 'HDD,Мониторы и т.п.', '5740', 'AOC E2270SWN 21.5" ЖК монитор Black TN LCD, Wide, 1920x1080, D-Sub, 5 мс, 200 кд/м2, 600:1 (20M:1 DCR), 90°/65°, шт.', 'AOC E2270SWN').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "AOC E2270SWN"!')
            return()
# ДЛЯ ВИДЕО: ПРИЕМО-ПЕРЕДАТЧИКИ
    if check_DH_PFM800_E.get():
        try:
            SFERA(int(enter_DH_PFM800_E.get()), 'https://secur.by/katalog/videonablyudenie/priemoperedatchiki-i-ustrojstva-zashhity/dh-pfm800-e.html', 'DAHUA DH-PFM800-E Приемопередатчик видеосигнала HDCVI/AHD/TVI/CVBS по витой паре пассивный одноканальный (комплект 2шт), поддерживаемое разрешение 720P/1080P, расстояние передачи 720P-400m, 1080P-250m, встроенная грозозащита, защита от низкочастотных помех, самозажимные клеммы, корпус пластик, -10...+55°C, (L)180х(W)19х(H)16mm, шт.', 'DH-PFM800-E').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DH-PFM800-E"!')
            return()
# БЛОКИ ПИТАНИЯ: ББП
    if check_bbp20_1.get():
        try:
            SFERA(int(enter_bbp20_1.get()), 'https://secur.by/katalog/istochniki-pitaniya/besperebojnye-bloki-pitaniya/bbp-20.html', 'Блок бесперебойного питания, Iном=2.0А, Iмакс=2.5А, Uвых=12VDC, АКБ 1х7.0А/h, шт.', 'ББП-20').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ББП-20"!')
            return()
    if check_bbp40_1.get():
        try:
            SFERA(int(enter_bbp40_1.get()), 'https://secur.by/katalog/istochniki-pitaniya/besperebojnye-bloki-pitaniya/bbp-40.html', 'Блок бесперебойного питания, Iном=4.0А, Iмакс=4.5А, Uвых=12VDC, АКБ 1х7.0А/h, шт.', 'ББП-40').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ББП-40"!')
            return()
    if check_bbp60_1.get():
        try:
            SFERA(int(enter_bbp60_1.get()), 'https://secur.by/katalog/istochniki-pitaniya/besperebojnye-bloki-pitaniya/bbp-60.html', 'Блок бесперебойного питания, Iном=6.0А, Iмакс=6.5А, Uвых=12VDC, АКБ 1х7.0А/h, шт.', 'ББП-60').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ББП-60"!')
            return()
    if check_bbp60_2.get():
        try:
            SFERA(int(enter_bbp60_2.get()), 'https://secur.by/katalog/istochniki-pitaniya/besperebojnye-bloki-pitaniya/bbp-60-isp.2.html', 'Блок бесперебойного питания, Iном=6.0А, Iмакс=6.5А, Uвых=12VDC, АКБ 1х17.0А/h, шт.', 'ББП-60 исп.2').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ББП-60 исп.2"!')
            return()
# БЛОКИ ПИТАНИЯ: АККУМУЛЯТОРЫ
    if check_akk7.get():
        try:
            SFERA(int(enter_akk7.get()), 'https://secur.by/katalog/istochniki-pitaniya/akkumulyatory/7.0-12v1.html', 'Аккумулятор, 12V, 7.0Ah, шт.', 'Аккумулятор 7 А/ч').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Аккумулятор 7 А/ч"!')
            return()
    if check_akk18.get():
        try:
            SFERA(int(enter_akk18.get()), 'https://secur.by/katalog/istochniki-pitaniya/akkumulyatory/18.0-12v1.html', 'Аккумулятор, 12V, 18Ah, шт.', 'Аккумулятор 18 А/ч').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Аккумулятор 18 А/ч"!')
            return()
# БЛОКИ ПИТАНИЯ: БЛОКИ ПИТАНИЯ
    if check_blok_pitania_1a.get():
        try:
            SFERA(int(enter_blok_pitania_1a.get()), 'https://secur.by/katalog/istochniki-pitaniya/bloki-pitaniya/at-1210.html', 'Блок стабилизированного питания, Iном=1.0А, Iмакс=1.5А, Uвых=12VDC, шт.', 'Блок питания 1А').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Блок питания 1А"!')
            return()
# БЛОКИ ПИТАНИЯ: ИБП
    if check_UT1500E.get():
        try:
            SFERA(int(enter_UT1500E.get()), 'https://secur.by/katalog/istochniki-pitaniya/besperebojnye-istochniki-pitaniya/cyberpower-ut1500e.html', 'CyberPower UT1500E Источник бесперебойного питания 1500VA/900W, line-interactive, AVR, защита телефонной линии RJ11/RJ45, USB, 4 розетки C13/C14 + 2 розетки C13 с заземлением, cтупенчатая аппроксимация синусоиды, холодный старт, совместимость с генераторами, аккумулятор 2x12V/7.5Ah, 0...+40°С, (L)193x(W)335x(H)247mm, 9.1kg, шт.', 'CyberPower UT1500E').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "CyberPower UT1500E"!')
            return()
# СКУД: КОНТРОЛЛЕРЫ
    if check_sigur_e500u.get():
        try:
            SOLO(int(enter_sigur_e500u.get()), 'https://solosecurity.by/sigur-skyd/setevye-kontrollery/setevoj-kontroller-sigur-e500u.html','Сетевой контроллер Sigur E500U, шт.', 'Sigur E500U').find_price() 
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Sigur E500U"!')
            return()
# СКУД: ЗАМКИ\ЗАЩЕЛКИ
    if check_ml194k_be.get():
        try:
            AVANT_SKD(int(enter_ml194k_be.get()), 'Accordtec', 'ML-194K (Б/Э)', 'ML-194K (Б/Э) Замок электромагнитный, 12 V DC, 0.64 A, усилие не менее 500 кг, Габариты: 270x75x45. Вес 5,6 кг. Темп.диапазон -30°С…+50°С. Размер отсека блока электроники 36x66x36мм. Уголок для крепления в комплекте.', 'Замок ML-194K (Б/Э)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ML-194K (Б/Э)"!')
            return()
    if check_jis_1711.get():
        try:
            SFERA(int(enter_jis_1711.get()), 'https://secur.by/katalog/kontrol-i-upravlenie-dostupom/elektrozamki-i-zashhelki/elektromehanicheskie-zashhelki/1711_elektrozaschelka.html', 'Jis 1711 Электрозащелка нормально-открытого типа (NO), регулируемая запорная планка, 12VDC/3.25W', 'Jis 1711').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Jis 1711"!')
            return()
# СКУД: КНОПКИ
    if check_AA_UD808G2.get():
        try:
            SFERA(int(enter_AA_UD808G2.get()), 'https://secur.by/katalog/kontrol-i-upravlenie-dostupom/knopki_vyhoda/aa-ud808g2.html', 'Устройство разблокировки двери с восстанавливаемой вставкой, 2 группы НО/НЗ контактов, защитная прозрачная крышка, коммутируемый ток 3А, 12/24VDC(AC)', 'Устройство разблокировки').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Устройство разблокировки"!')
            return()
    if check_AT_H805A.get():
        try:
            AVANT_SKD(int(enter_AT_H805A.get()), 'Accordtec', 'AT-H805A  ', 'AT-H805A Кнопка выхода металическая накладная. Габариты 82*32*25. Тип контактов НО.','Кнопка выхода AT-H805A').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "AT-H805A"!')
            return()
# СКУД: ПЛАНКИ
    if check_jis_904G.get():
        try:
            SFERA(int(enter_jis_904G.get()), 'https://secur.by/katalog/kontrol-i-upravlenie-dostupom/elektrozamki-i-zashhelki/elektromehanicheskie-zashhelki/904g.html', 'Jis 904G Планка универсальная, длинная, для электрозащелок 17хх серии, левая/правая установка, корпус сталь, (L)25х(W)250х(H)2.5mm, внутр. (L)12х(W)102mm, цвет серый, шт.', 'Планка Jis 904G').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Jis 904G"!')
            return()
# СКУД: КАРТЫ ДОСТУПА
    if check_SL_05_EM.get():
        try:
            AVANT_SKD(int(enter_SL_05_EM.get()), 'Системы доступа, брелки, карты', 'Карта Clamshell SL-05 EM', 'Карта EM - marine 1.6 мм c прорезью, шт.','Clamshell SL-05 EM').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Clamshell SL-05 EM"!')
            return()
    if check_SL_05_MF.get():
        try:
            AVANT_SKD(int(enter_SL_05_MF.get()), 'Системы доступа, брелки, карты', 'Карта Clamshell SL-05 MF', 'Карта Mifare 1.6 мм c прорезью, шт.','Clamshell SL-05 MF').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Clamshell SL-05 MF"!')
            return()
    if check_SL_06_EM.get():
        try:
            AVANT_SKD(int(enter_SL_06_EM.get()), 'Системы доступа, брелки, карты', 'Карта PVC SL-06 EM', 'Карта EM - marine 0.8 мм тонкая под печать, шт.','PVC SL-06 EM').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PVC SL-06 EM"!')
            return()
    if check_SL_06_MF.get():
        try:
            AVANT_SKD(int(enter_SL_06_MF.get()), 'Системы доступа, брелки, карты', 'Карта PVC SL-06 MF', 'Карта Mifare 0.8 мм тонкая под печать, шт.','PVC SL-06 MF').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PVC SL-06 MF"!')
            return()
    if check_SL_06_EM_MF.get():
        try:
            AVANT_SKD(int(enter_SL_06_EM_MF.get()), 'Системы доступа, брелки, карты', 'Карта PVC SL-06 EM+MF', 'Двухдиапазонная карта (ЕМ + Mifare) 0.8 мм тонкая под печать, шт.','PVC SL-06 EM+MF').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PVC SL-06 EM+MF"!')
            return()
    if check_SL_01_EM_BW.get():
        try:
            AVANT_SKD(int(enter_SL_01_EM_BW.get()), 'Системы доступа, брелки, карты', 'Брелок SL-01 EM BW', 'Брелок EM - marine, шт.', 'SL-01 EM BW').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "SL-01 EM BW"!')
            return()
    if check_SL_03_MF.get():
        try:
            AVANT_SKD(int(enter_SL_03_MF.get()), 'Системы доступа, брелки, карты', 'Брелок SL-03 MF', 'Брелок Mifare, шт.', 'SL-03 MF').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "SL-03 MF"!')
            return()
# PERCo: КОНТРОЛЛЕРЫ
    if check_perco_ctl_042.get():
        try:
            SOB(int(enter_perco_ctl_042.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=84&ID=3304','PERCo-CT/L04.2 Контроллер турникета под два выносных считывателя с интерфейсом RS-485, выходной протокол Ethernet, память на 50 000 карт, ёмкость памяти событий - до 135 000, напряжение питания 12V DC, 6Вт, +1°С…+40°С, габаритные размеры 205х235х58мм', 'PERCo-CT/L04.2').find_price() 
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-CT/L04.2"!')
            return()
    if check_perco_cr012.get():
        try:
            SOB(int(enter_perco_cr012.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=84&ID=25358','PERCo-CR01.2 Контроллер регистрации, выходной протокол Ethernet, память на 50 000 карт, ёмкость памяти - до 140 000, до 5000 пользователей, напряжение питания 12V DC, 3Вт, +1°С…+40°С, габаритные размеры 190х140х23мм', 'PERCo-CR01.2').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-CR01.2"!')
            return()            
# PERCo: СЧИТЫВАТЕЛИ
    if check_perco_ir031b.get():
        try:
            SOB(int(enter_perco_ir031b.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=101&ID=3366','PERCo-IR03.1B Считыватель бесконтактных карт HID, EM-Marin с интерфейсом RS-485, дальность считывания карт - 10см, брелоков - 4см, максимальное расстояние до контроллера 50м, напряжение питания 12V DC, 1Вт, -40°С…+40°С, цвет бежевый, габаритные размеры 145х50х20мм', 'PERCo-IR03.1B').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-IR03.1B"!')
            return()            
    if check_perco_ir031d.get():
        try:
            SOB(int(enter_perco_ir031d.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=101&ID=3367','PERCo-IR03.1D Считыватель бесконтактных карт HID, EM-Marin с интерфейсом RS-485, дальность считывания карт - 10см, брелоков - 4см, максимальное расстояние до контроллера 50м, напряжение питания 12V DC, 1Вт, -40°С…+40°С, цвет темно-серый, габаритные размеры 145х50х20мм', 'PERCo-IR03.1D').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-IR03.1D"!')
            return()            
    if check_perco_ir04.get():
        try:
            SOB(int(enter_perco_ir04.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=101&ID=3368','PERCo-IR04 Считыватель бесконтактных карт HID, EM-Marin с интерфейсом RS-485, дальность считывания карт - 10см, брелоков - 4см, максимальное расстояние до контроллера 40м, напряжение питания 12V DC, 2Вт, +1°С…+50°С, габаритные размеры 145х50х20мм', 'PERCo-IR04').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-IR04"!')
            return()            
    if check_perco_ir041.get():
        try:
            SOB(int(enter_perco_ir041.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=101&ID=25359','PERCo-IR04.1 Считыватель бесконтактных карт HID, EM-Marin с интерфейсом RS-485, дальность считывания карт - 10см, брелоков - 4см, максимальное расстояние до контроллера 40м, напряжение питания 12V DC, 2Вт, +1°С…+50°С, габаритные размеры 145х50х20мм', 'PERCo-IR04.1').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-IR04.1"!')
            return()            
    if check_perco_ir07.get():
        try:
            SOB(int(enter_perco_ir07.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=101&ID=3369','PERCo-IR07 Считыватель бесконтактных карт HID, EM-Marin с интерфейсом RS-485, дальность считывания карт - 10см, брелоков - 4см, максимальное расстояние до контроллера 40м, напряжение питания 12V DC, 2Вт, +1°С…+50°С, габаритные размеры 145х50х20мм', 'PERCo-IR07').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-IR07"!')
            return()
# PERCo: ПО
    if check_perco_sl02.get():
        try:
            SOB(int(enter_perco_sl02.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7720','PERCo-SL02 Локальное ПО с видеоидентификацией является однопользовательским модулем и предназначен для организации контроля доступа по принципу разрешено/запрещено через одну точку прохода с возможностью видеоидентификации. Возможности: ввод данных о сотрудниках (ФИО), выдача карт доступа, назначение прав доступа (разрешение/запрет), установка и изменение режимов доступа, просмотр списка событий, связанных с конкретным сотрудником за определенный период времени, конфигурация аппаратуры, регистрация событий в файле базы данных с возможностью экспорта данных в файл (например, Excel)', 'PERCo-SL02').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SL02"!')
            return()
    if check_perco_sm01.get():
        try:
            SOB(int(enter_perco_sm01.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3269','PERCo-SM01 Сетевой модуль «Администратор» предназначен для организации рабочего места администратора системы безопасности. Необходим для описания параметров функционирования устройств и программного обеспечения, описания параметров функционирования подсистемы пожарной сигнализации, описания параметров функционирования подсистемы видеонаблюдения, задания реакции системы безопасности и программного обеспечения на зарегистрированные события, ведение списка операторов', 'PERCo-SM01').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM01"!')
            return()
    if check_perco_sm02.get():
        try:
            SOB(int(enter_perco_sm02.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3270','PERCo-SM02 Сетевой модуль «Персонал» предназначен для организации рабочего места сотрудника отдела кадров, позволяет сократить объем рутинной работы и повышает эффективность работы. В отличие от раздела Сотрудники, входящего в состав Базового ПО, раздел данного модуля позволяет: вводить фотографии сотрудников предприятия, заполнять расширенный список учетных данных в текстовом и графическом виде', 'PERCo-SM02').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM02"!')
            return()
    if check_perco_sm03.get():
        try:
            SOB(int(enter_perco_sm03.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3271','PERCo-SM03 Сетевой модуль «Бюро пропусков» используется для выдачи и изъятия карт доступа сотрудникам предприятия и посетителям, разграничения доступа в помещения по времени, назначения сотрудникам прав на постановку/снятие помещений на/с охраны', 'PERCo-SM03').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM03"!')
            return()
    if check_perco_sm04.get():
        try:
            SOB(int(enter_perco_sm04.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3272','PERCo-SM04 Сетевой модуль «Управление доступом» предназначен для создания справочников графиков (временные зоны, недельные графики, скользящие посуточные и скользящие понедельные графики, задание праздников) доступа по времени, для разграничения доступа по времени сотрудников и посетителей', 'PERCo-SM04').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM04"!')
            return()
    if check_perco_sm05.get():
        try:
            SOB(int(enter_perco_sm05.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3273','PERCo-SM05 Сетевой модуль «Дисциплинарные отчеты» позволяет автоматизировать формирование отчетов о времени присутствия сотрудников на рабочем месте и местонахождения сотрудников на определенный момент времени. Предназначен для контроля руководителями подразделений трудовой дисциплины сотруднико', 'PERCo-SM05').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM05"!')
            return()
    if check_perco_sm07.get():
        try:
            SOB(int(enter_perco_sm07.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3274','PERCo-SM07 Сетевой модуль «Учет рабочего времени» обеспечивает автоматизацию учета рабочего времени на предприятии с возможностью сформировать табель учета рабочего времени по стандартным формам Т12 и Т13. Интеллектуальный алгоритм учета поддерживает многосменные и скользящие графики работы, обеспечивает корректный учет рабочего времени при различных видах трудового распорядка', 'PERCo-SM07').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM07"!')
            return()
    if check_perco_sm08.get():
        try:
            SOB(int(enter_perco_sm08.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3275','PERCo-SM08 Сетевой модуль «Мониторинг» устанавливается на рабочее место сотрудника службы безопасности и предназначен для отображения информации о состоянии объекта и оперативного управления расположенными на нем устройствами, а также для построения графического плана СКД', 'PERCo-SM08').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM08"!')
            return()
    if check_perco_sm09.get():
        try:
            SOB(int(enter_perco_sm09.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3276','PERCo-SM09 Сетевой модуль «Видеоидентификация» устанавливается на рабочее место сотрудника службы охраны и позволяет производить идентификацию владельца карты доступа, сравнивая личность проходящего сотрудника или изображение с видеокамеры и его фото, хранящееся в базе данных системы. Позволяет одновременно контролировать до 4-х точек прохода и 4-х камер видеонаблюдения. Для возможности работы модуля с видеокамерами требуется установка модуля PERCo-SM01 «Администратор»', 'PERCo-SM09').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM09"!')
            return()
    if check_perco_sm10.get():
        try:
            SOB(int(enter_perco_sm10.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3277','PERCo-SM10 Сетевой модуль «Прием посетителей» предназначен для организации приема посетителей, позволяет руководителям и лицам, ведущим прием, дистанционно управлять доступом в свой кабинет', 'PERCo-SM10').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM10"!')
            return()
    if check_perco_sm12.get():
        try:
            SOB(int(enter_perco_sm12.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3278','PERCo-SM12 Программный модуль «Видеонаблюдение» устанавливается на рабочем месте сотрудника службы безопасности и предназначен для отображения видеоинформации, получаемой с видеокамер, управления видеокамерами, записи видеоинформации и ее воспроизведения', 'PERCo-SM12').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM12"!')
            return()
    if check_perco_sm13.get():
        try:
            SOB(int(enter_perco_sm13.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3279','PERCo-SM13 Сетевой модуль «Центральный пост» устанавливается на рабочее место сотрудника службы безопасности и позволяет вести централизованное наблюдения за состоянием объекта. Отображение информации о состоянии объектов на графических планах предприятия и в табличном виде, отображение изображения с камер видеонаблюдения, управление устройствами, расположенными на графическом плане предприятия, контроль доступа в режиме верификации, при возникновении тревожной ситуации автоматическое отображение информации с камер видеонаблюдения и мнемосхемы помещения, где произошло тревожное событие, с указанием точного места возникновения тревоги', 'PERCo-SM13').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM13"!')
            return()
    if check_perco_sm14.get():
        try:
            SOB(int(enter_perco_sm14.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3280','PERCo-SM14 Сетевой модуль «Дизайнер пропусков» используется для подготовки шаблонов и печати пропусков сотрудникам и посетителям предприятия, позволяет автоматизировать работу по оформлению постоянных и временных пропусков, оформить карты доступа в виде пропусков с фотографией и другими данными сотрудника или гостя', 'PERCo-SM14').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM14"!')
            return()
    if check_perco_sm15.get():
        try:
            SOB(int(enter_perco_sm15.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3281','PERCo-SM15 Как элемент системы видеонаблюдения, модуль «Прозрачное здание» позволяет руководителям использовать видеоинформацию для контроля выполнения сотрудниками производственных задач на рабочих местах, создавая «эффект присутствия» и дает возможность вывода информации с видеокамер на мониторы, установленные в местах общего доступа, способствуя повышению самодисциплины сотрудников', 'PERCo-SM15').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM15"!')
            return()
    if check_perco_sm16.get():
        try:
            SOB(int(enter_perco_sm16.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7722','PERCo-SM16 Модуль PERCo-SM16 «Кафе» предназначен для организации безналичного расчета оплаты питания сотрудников предприятий, имеющих в своей структуре подразделения служебного питания (кафе, буфеты, столовые и т.п.). Модуль «Кафе» позволяет учитывать различные схемы льгот и компенсаций питания сотрудников', 'PERCo-SM16').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM16"!')
            return()
    if check_perco_sm17.get():
        try:
            SOB(int(enter_perco_sm17.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7723','PERCo-SM17 Сетевой модуль ПО PERCo-SM17 «АТП» предназначен для организации работы автотранспортной проходной, автоматизации контроля доступа на территорию предприятия служебных транспортных средств (ТС) и личных ТС сотрудников и посетителей. Модуль ПО «АТП» позволяет формировать отчеты о проездах ТС, и вести учет времени нахождения ТС на территории предприятия и за его пределами.', 'PERCo-SM17').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM17"!')
            return()
    if check_perco_sm18.get():
        try:
            SOB(int(enter_perco_sm18.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7775','PERCo-SM18 «Модуль интеграции с системой пожарной и охранной безопасности «Орион» PERCo-SM18 позволяет отслеживать состояния и настраивать параметры подключенных устройств ИСО «Орион», получать регистрируемые ими события и подавать команды управления непосредственно в интерфейсе S-20.', 'PERCo-SM18').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM18"!')
            return()
    if check_perco_sm19.get():
        try:
            SOB(int(enter_perco_sm19.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=25574',"PERCo-SM19 Модуль 'Интеграция с 1С:Предприятие' для интеграции PERCo-S20 c 1C:Предприятие v.8 и выше", 'PERCo-SM19').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM19"!')
            return()
    if check_perco_sm20.get():
        try:
            SOB(int(enter_perco_sm20.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=25575',"PERCo-SM20 Модуль 'Интеграция с видеоподсистемой 'Trassir'", 'PERCo-SM20').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SM20"!')
            return()
    if check_perco_sn01.get():
        try:
            SOB(int(enter_perco_sn01.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=3268',"PERCo-SN01 Базовое ПО является сетевым программным обеспечением системы S-20 и предназначено для: конфигурации аппаратуры, оперативного управления устройствами, ведения списка сотрудников, выдачи карт доступа, разграничение доступа в помещения по принципу «свой/чужой», регистрации событий в файле базы данных с возможностью экспорта данных в файл Excel. PERCo-SN01 является необходимым элементом для установки других программных модулей", 'PERCo-SN01').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SN01"!')
            return()
    if check_perco_sp09.get():
        try:
            SOB(int(enter_perco_sp09.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7776', 'PERCo-SP09 Комплект программного обеспечения «Дисциплина + УРВ» (Базовое ПО, "Дисциплинарные отчеты", “УРВ") Минимально необходимый комплект для работы терминала LICON', 'PERCo-SP09').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP09"!')
            return()
    if check_perco_sp10.get():
        try:
            SOB(int(enter_perco_sp10.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7724', 'PERCo-SP10 Комплект программного обеспечения «Контроль доступа + ОПС» (Базовое ПО, «Бюро пропусков», «Управление доступом», «Персонал», «Мониторинг»)', 'PERCo-SP10').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP10"!')
            return()
    if check_perco_sp11.get():
        try:
            SOB(int(enter_perco_sp11.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7725', 'PERCo-SP11 Комплект программного обеспечения «Контроль доступа + ОПС + Фотоидентификация» (Базовое ПО, «Бюро пропусков», «Управление доступом», «Персонал», «Мониторинг», «Видеоидентификация»)', 'PERCo-SP11').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP11"!')
            return()
    if check_perco_sp12.get():
        try:
            SOB(int(enter_perco_sp12.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7726', 'PERCo-SP12 Комплект программного обеспечения «Контроль доступа + ОПС + Дисциплина» (Базовое ПО, «Бюро пропусков», «Управление доступом», «Персонал», «Мониторинг», «Дисциплинарные отчеты»)', 'PERCo-SP12').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP12"!')
            return()
    if check_perco_sp13.get():
        try:
            SOB(int(enter_perco_sp13.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7727', 'PERCo-SP13 Комплект программного обеспечения «Контроль доступа + ОПС + Дисциплина + УРВ» (Базовое ПО, «Бюро пропусков», «Управление доступом», «Персонал», «Мониторинг», «Дисциплинарные отчеты», «УРВ»)', 'PERCo-SP13').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP13"!')
            return()
    if check_perco_sp14.get():
        try:
            SOB(int(enter_perco_sp14.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7728', 'PERCo-SP14 Комплект программного обеспечения «Усиленный контроль доступа с видеоидентификацией + ОПС + Дисциплина» (Базовое ПО, «Администратор», «Бюро пропусков», «Управление доступом», «Персонал», «Мониторинг», «Дисциплинарные отчеты», «Видеоидентификация»)', 'PERCo-SP14').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP14"!')
            return()
    if check_perco_sp15.get():
        try:
            SOB(int(enter_perco_sp15.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7729', 'PERCo-SP15 Комплект программного обеспечения «Усиленный контроль доступа с видеоидентификацией + ОПС + Дисциплина + УРВ»', 'PERCo-SP15').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP15"!')
            return()
    if check_perco_sp16.get():
        try:
            SOB(int(enter_perco_sp16.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7730', 'PERCo-SP16 Комплект программного обеспечения «Усиленный контроль доступа с видеоидентификацией + ОПС + Видео + Дисциплина + УРВ» (Базовое ПО, «Администратор», «Бюро пропусков», «Управление доступом», «Персонал», «Мониторинг», Дисциплинарные отчеты», «УРВ», «Видеоидентификация», «Видеонаблюдение», «Прозрачное здание»)', 'PERCo-SP16').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP16"!')
            return()
    if check_perco_sp17.get():
        try:
            SOB(int(enter_perco_sp17.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=86&ID=7731', 'PERCo-SP17 Комплект программного обеспечения «Усиленный контроль доступа с видеоидентификацией + ОПС + Видео + Дисциплина + Центральный пост охраны» (Базовое ПО, «Администратор», «Бюро пропусков», «Управление доступом», «Персонал», «Мониторинг», «Дисциплинарные отчеты», «Видеоидентификация», «Видеонаблюдение», «Центральный пост»)', 'PERCo-SP17').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "PERCo-SP17"!')
            return()
# MATRIX: КОНТРОЛЛЕРЫ
    if check_matrix_ii_net.get():
        try:
            AVANT_SKD(int(enter_matrix_ii_net.get()), 'Системы доступа, брелки, карты', 'Считыватель Matrix-II NET', 'Matrix II NET Сетевой контроллер со встроенным считывателем, Напряжение питания: 8-18V DC, Ток потребления: 45 mA, Количество подключаемых считывателей: 1шт. Тип (протокол) подключаемых считывателей: Dallas Touch Memory, Выходы МДП транзистор: 1 шт. Ток коммутации: 5А. Количество ключей/карт (max): 2024шт. Количество запоминаемых событий (max):2048шт.', 'Matrix-II Net').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Matrix-II Net"!')
            return()  
    if check_matrix_ii.get():
        try:
            AVANT_SKD(int(enter_matrix_ii.get()), 'Системы доступа, брелки, карты', 'Считыватель Matrix-II серый', 'Matrix II Считыватель проксимити-карт стандарта EM-Marine, офисный вариант, индентификатор EM Marine, Ангстрем-125 кГц,звуковая и световая индикация, дальность чтения: 6-8 cm, выход-Dallas 1990A, Wiegand 26, напряжение питания: 8 - 18 В постоянного тока, 85x44x18', 'Matrix-II').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Matrix-II"!')
            return()
    if check_z397_web.get():
        try:
            SOB(int(enter_z397_web.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=57&CID=100&ID=7788','IronLogic Z-397 Web конвертер для доступа к устройствам, управляемым по шине RS-485 (422), через локальную сеть или Web-сервисы. Устройство подсоединяется к локальной сети или сети Интернет и к шине RS-485. Работа с Z-397 ведется по протоколу TCP/IP.', 'Z-397 (мод. WEB)').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Z-397 (мод. WEB)"!')
            return()
# MATRIX: GUARD SAAS КОМПЛЕКТ
    if check_guard_saas_2_50.get():
        try:
            SOB(int(enter_guard_saas_2_50.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7801', 'Guard Saas-2/50 Web ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-2, человек-50, комплектность: Z-397 Web с лицензией GuardSaaS - 2/50, совместимо с конверторами/контроллерами: Z-5R Net, Z-5RNet 8000, Matrix-II Net, Guard Net.', 'Guard Saas-2/50 Web').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-2/50 Web"!')
            return()
    if check_guard_saas_2_100.get():
        try:
            SOB(int(enter_guard_saas_2_100.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7803', 'Guard Saas-2/100 Web ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-2, человек-100, комплектность: Z-397 Web с лицензией GuardSaaS - 2/100, совместимо с конверторами/контроллерами: Z-5R Net, Z-5RNet 8000, Matrix-II Net, Guard Net.', 'Guard Saas-2/100 Web').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-2/100 Web"!')
            return()
    if check_guard_saas_2_250.get():
        try:
            SOB(int(enter_guard_saas_2_250.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7802', 'Guard Saas-2/250 Web ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-2, человек-250, комплектность: Z-397 Web с лицензией GuardSaaS - 2/250, совместимо с конверторами/контроллерами: Z-5R Net, Z-5RNet 8000, Matrix-II Net, Guard Net.', 'Guard Saas-2/250 Web').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-2/250 Web"!')
            return()
    if check_guard_saas_5_100.get():
        try:
            SOB(int(enter_guard_saas_5_100.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7804', 'Guard Saas-5/100 Web ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-5, человек-100, комплектность: Z-397 Web с лицензией GuardSaaS - 5/100, совместимо с конверторами/контроллерами: Z-5R Net, Z-5RNet 8000, Matrix-II Net, Guard Net.', 'Guard Saas-5/100 Web').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-5/100 Web"!')
            return()
    if check_guard_saas_10_250.get():
        try:
            SOB(int(enter_guard_saas_10_250.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7805', 'Guard Saas-10/250 Web ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-10, человек-250, комплектность: Z-397 Web с лицензией GuardSaaS - 10/250, совместимо с конверторами/контроллерами: Z-5R Net, Z-5RNet 8000, Matrix-II Net, Guard Net.', 'Guard Saas-10/250 Web').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-10/250 Web"!')
            return()
# MATRIX: GUARD SAAS ЛИЦЕНЗИЯ
    if check_guard_saas_2_50_l.get():
        try:
            SOB(int(enter_guard_saas_2_50_l.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7807', 'Guard Saas-2/50L ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-2, человек-50, совместимо с конвертором Z-397 Web.', 'Guard Saas-2/50L').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-2/50L"!')
            return()
    if check_guard_saas_2_100_l.get():
        try:
            SOB(int(enter_guard_saas_2_100_l.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7808', 'Guard Saas-2/100L ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-2, человек-100, совместимо с конвертором Z-397 Web.', 'Guard Saas-2/100L').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-2/100L"!')
            return()
    if check_guard_saas_2_250_l.get():
        try:
            SOB(int(enter_guard_saas_2_250_l.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7809', 'Guard Saas-2/250L ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-2, человек-250, совместимо с конвертором Z-397 Web.', 'Guard Saas-2/250L').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-2/250L"!')
            return()
    if check_guard_saas_5_100_l.get():
        try:
            SOB(int(enter_guard_saas_5_100_l.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7810', 'Guard Saas-5/100L ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-5, человек-100, совместимо с конвертором Z-397 Web.', 'Guard Saas-5/100"').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-5/100L"!')
            return()
    if check_guard_saas_10_250_l.get():
        try:
            SOB(int(enter_guard_saas_10_250_l.get()), 'http://www.sob.by/time_control_price_t.php?CAT_ID=51&CID=378&ID=7811', 'Guard Saas-10/250L ПО для учета рабочего времени. Подключение конвертора-Ethernet, ПК не требуется, количество точек прохода-10, человек-250, совместимо с конвертором Z-397 Web.', 'Guard Saas-10/250L').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Guard Saas-10/250L"!')
            return()
# КОММУТАТОРЫ: D-LINK FAST ETHERNET
    if check_des_1005c.get():
        try:
            SOB(int(enter_des_1005c.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53850', 'D-Link DES-1005C Неуправляемый коммутатор с 5 портами 10/100Base-TX и функцией энергосбережения, шт.', 'DES-1005C').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1005C"!')
            return()
    if check_des_1005d.get():
        try:
            SOB(int(enter_des_1005d.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53851', 'D-Link DES-1005D Неуправляемый коммутатор с 5 портами 10/100Base-TX, шт.', 'DES-1005D').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1005D/O2B"!')
            return()
    if check_des_1005p.get():
        try:
            SOB(int(enter_des_1005p.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53852', 'D-Link DES-1005P Неуправляемый коммутатор с 5 портами 10/100Base-TX, функцией энергосбережения и поддержкой QoS (4 порта с поддержкой PoE 802.3af/802.3at (30 Вт), PoE-бюджет 60 Вт), шт.', 'DES-1005P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1005P/B1A"!')
            return()
    if check_des_1008c.get():
        try:
            SOB(int(enter_des_1008c.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53853', 'D-Link DES-1008C Неуправляемый коммутатор с 8 портами 10/100Base-TX и функцией энергосбережения, шт.', 'DES-1008C').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1008C/A1B"!')
            return()
    if check_des_1008d.get():
        try:
            SOB(int(enter_des_1008d.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53854', 'D-Link DES-1008D Неуправляемый коммутатор с 8 портами 10/100Base-TX, шт.', 'DES-1008D').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1008D/L2B"!')
            return()
    if check_des_1008p.get():
        try:
            SOB(int(enter_des_1008p.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4335&ID=55059', 'D-Link DES-1008P Коммутатор D-Link DES-1008P, 8-Port 10/100 Switch (4 порта с поддержкой PoE), шт.', 'DES-1008P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1008P/C1A"!')
            return()
    if check_des_1008pp.get():
        try:
            SOB(int(enter_des_1008pp.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53855', 'D-Link DES-1008P+ Неуправляемый коммутатор с 8 портами 10/100Base-TX с поддержкой PoE 802.3af/802.3at (30 Вт), PoE-бюджет 140 Вт, шт.', 'DES-1008P+').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1008P+/A1A"!')
            return()
    if check_des_1016d.get():
        try:
            SOB(int(enter_des_1016d.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53867', 'D-Link DES-1016D Неуправляемый коммутатор с 16 портами 10/100Base-TX, функцией энергосбережения и поддержкой QoS, шт.', 'DES-1016D').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1016D/H1A"!')
            return()
    if check_des_1018p.get():
        try:
            SOB(int(enter_des_1018p.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53869', 'D-Link DES-1018P Неуправляемый коммутатор с 16 портами 10/100Base-TX, 2 комбо-портами 100/1000Base-T/SFP и функцией энергосбережения (8 портов с поддержкой PoE 802.3af (15,4 Вт), PoE-бюджет 80 Вт), шт.', 'DES-1018P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1018P/A2A"!')
            return()
    if check_des_1018mp.get():
        try:
            SOB(int(enter_des_1018mp.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53868', 'D-Link DES-1018MP Неуправляемый коммутатор с 16 портами 10/100Base-TX, 2 комбо-портами 100/1000Base-T/SFP и функцией энергосбережения (16 портов с поддержкой PoE 802.3af (15,4 Вт), PoE-бюджет 246,4 Вт), шт.', 'DES-1018MP').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DES-1018MP/A1A"!')
            return()
# КОММУТАТОРЫ: D-LINK GIGABIT ETHERNET
    if check_dgs_1005a.get():
        try:
            SOB(int(enter_dgs_1005a.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53858', 'D-Link DGS-1005A Неуправляемый коммутатор с 5 портами 10/100/1000Base-T, функцией энергосбережения и поддержкой QoS, шт.', 'DGS-1005A').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1005A/E1A"!')
            return()
    if check_dgs_1005d.get():
        try:
            SOB(int(enter_dgs_1005d.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53859', 'D-Link DGS-1005D Неуправляемый коммутатор с 5 портами 10/100/1000Base-T и функцией энергосбережения, шт.', 'DGS-1005D').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1005D/I3A"!')
            return()
    if check_dgs_1005d.get():
        try:
            SOB(int(enter_dgs_1005d.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53860', 'D-Link DGS-1005P Неуправляемый коммутатор с 5 портами 10/100/1000Base-T, функцией энергосбережения и поддержкой QoS (4 порта с поддержкой PoE 802.3af/802.3at (30 Вт), PoE-бюджет 60 Вт), шт.', 'DGS-1005P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1005P/A1A"!')
            return()
    if check_dgs_1008a.get():
        try:
            SOB(int(enter_dgs_1008a.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53861', 'D-Link DGS-1008A Неуправляемый коммутатор с 8 портами 10/100/1000Base-T и функцией энергосбережения, шт.', 'DGS-1008A').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1008A/E1A"!')
            return()
    if check_dgs_1008d.get():
        try:
            SOB(int(enter_dgs_1008d.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53862', 'D-Link DGS-1008D Неуправляемый коммутатор с 8 портами 10/100/1000Base-T, функцией энергосбережения и поддержкой QoS, шт.', 'DGS-1008D').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1008D/J3A"!')
            return()
    if check_dgs_1008p.get():
        try:
            SOB(int(enter_dgs_1008p.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53863', 'D-Link DGS-1008P Неуправляемый коммутатор с 8 портами 10/100/1000Base-T, функцией энергосбережения и поддержкой QoS (4 порта с поддержкой PoE 802.3af/802.3at (30 Вт), PoE-бюджет 68 Вт), шт.', 'DGS-1008P').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1008P/D1A"!')
            return()
    if check_dgs_1008mp.get():
        try:
            SOB(int(enter_dgs_1008mp.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53873', 'D-Link DGS-1008MP Неуправляемый коммутатор с 8 портами 10/100/1000Base-T с поддержкой PoE 802.3af/802.3at (30 Вт, PoE-бюджет 140 Вт) и функцией энергосбережения, шт.', 'DGS-1008MP').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1008MP/A2A"!')
            return()
    if check_dgs_1010mp.get():
        try:
            SOB(int(enter_dgs_1010mp.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53874', 'D-Link DGS-1010MP Неуправляемый коммутатор с 9 портами 10/100/1000Base-T, 1 портом 1000Base-X SFP, функцией энергосбережения и поддержкой QoS (8 портов с поддержкой PoE 802.3af/802.3at (30 Вт), PoE-бюджет 125 Вт), шт.', 'DGS-1010MP').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1010MP/A1A"!')
            return()
    if check_dgs_1016c.get():
        try:
            SOB(int(enter_dgs_1016c.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53875', 'D-Link DGS-1016C Неуправляемый коммутатор с 16 портами 10/100/1000Base-T, функцией энергосбережения и поддержкой QoS, шт.', 'DGS-1016C').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1016C/B1A"!')
            return()
    if check_dgs_1024c.get():
        try:
            SOB(int(enter_dgs_1024c.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53876', 'D-Link DGS-1024C Неуправляемый коммутатор с 24 портами 10/100/1000Base-T, функцией энергосбережения и поддержкой QoS, шт.', 'DGS-1024C').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1024C/B1A"!')
            return()
    if check_dgs_1026mp.get():
        try:
            SOB(int(enter_dgs_1026mp.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53877', 'D-Link DGS-1026MP Неуправляемый коммутатор с 24 портами 10/100/1000Base-T, 2 комбо-портами 100/1000Base-T/SFP и функцией энергосбережения (24 порта с поддержкой PoE 802.3af/at (30 Вт), PoE-бюджет 370 Вт), шт.', 'DGS-1026MP').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1026MP/A1A"!')
            return()
    if check_dgs_1026x.get():
        try:
            SOB(int(enter_dgs_1026x.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53878', 'D-Link DGS-1026X Неуправляемый коммутатор с 24 портами 10/100/1000Base-T, 2 портами 10GBase-X SFP+, функцией энергосбережения и поддержкой QoS, шт.', 'DGS-1026X').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1026X/A1A"!')
            return()
    if check_dgs_1052x.get():
        try:
            SOB(int(enter_dgs_1052x.get()), 'http://www.sob.by/lvs_price_t.php?CAT_ID=809&CID=4306&ID=53879', 'D-Link DGS-1052X Неуправляемый коммутатор с 48 портами 10/100/1000Base-T, 4 портами 10GBase-X SFP+ и функцией энергосбережения, шт.', 'DGS-1052X').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DGS-1052X"!')
            return()
# КОММУТАТОРЫ: ТОЧКИ ДОСТУПА
    if check_MikroTik_RBwAP2nD.get():
        try:
            NETAIR(int(enter_MikroTik_RBwAP2nD.get()), 'Прайс', 'RBwAP2nD', 'MikroTik wAP беспроводной маршрутизатор, шт.', 'MikroTik RBwAP2nD').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "MikroTik RBwAP2nD"!')
            return()
    if check_MikroTik_RBcAP2nD.get():
        try:
            NETAIR(int(enter_MikroTik_RBcAP2nD.get()), 'Прайс', 'RBcAP2nD', 'MikroTik cAP-2nD беспроводной маршрутизатор, шт.', 'MikroTik RBwAP2nD').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "MikroTik RBwAP2nD"!')
            return()
    if check_MikroTik_RBcAPGi_5acD2nD.get():
        try:
            NETAIR(int(enter_MikroTik_RBcAPGi_5acD2nD.get()), 'Прайс', 'RBcAPGi-5acD2nD', 'MikroTik cAP ac беспроводной маршрутизатор, шт.', 'MikroTik RBcAPGi-5acD2nD').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "MikroTik RBcAPGi-5acD2nD"!')
            return()
    if check_MikroTik_SXT_2.get():
        try:
            NETAIR(int(enter_MikroTik_SXT_2.get()), 'Прайс', 'RBSXTG-2HnD', 'MikroTik SXT 2 беспроводной маршрутизатор внешнего исполнения, шт.', 'MikroTik RBSXTG-2HnD').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "MikroTik RBSXTG-2HnD"!')
            return()
    if check_MikroTik_QMP.get():
        try:
            NETAIR(int(enter_MikroTik_QMP.get()), 'Прайс', 'QMP', 'MikroTik quickMOUNT pro, кронштейн для точки доступа, шт.', 'MikroTik QMP').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "MikroTik QMP"!')
            return()
# КОММУТАТОРЫ: МАРШРУТИЗАТОРЫ
    if check_MikroTik_RB951Ui_2HnD.get():
        try:
            NETAIR(int(enter_MikroTik_RB951Ui_2HnD.get()), 'Прайс', 'RB951Ui-2HnD', 'MikroTik RB951Ui-2HnD беспроводной маршрутизатор, шт.', 'MikroTik RB951Ui-2HnD').find_price()
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "MikroTik RB951Ui-2HnD"!')
            return()
# КОМУУТАТОРЫ: WI-TEK
    if check_WI_PS210G_O.get():
        try:
            SFERA(int(enter_WI_PS210G_O.get()), 'https://secur.by/katalog/setevoe-oborudovanie/kommutatory/wi-tek/wi-ps210g-o.html', 'Wi-Tek WI-PS210G-O Сетевой коммутатор неуправляемый уличный, 11 портов (6x10/100 Base-TX PoE, 2x1000 Base-TX PoE, 2x1000 Base-TX Up-link, 1xSFP), 2xPoE IEEE802.3bt (60W), 6xPoE IEEE802.3af/at (30W), бюджет PoE 120W, защита PoE от перенапряжения до 6kV, пропускная способность 11.2Gbps, выход 5VDC, Watchdog (детекция зависшего оборудования и перезагрузка питания PoE), 110-240VAC, грозозащита до 10kV, IP65, -30...+70°C, возможность установки на стену/столб (крепление в комплекте), (L)310x(W)260x(H)100mm, шт.', 'WI-PS210G-O').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "WI-PS210G-O"!')
            return()
# ЭЛЕКТРИКА: ВВГ
    if check_vvg_ng_ls_2_15.get():
        try:
            ETPROM(int(enter_vvg_ng_ls_2_15.get()), 'https://etprom.by/catalog/kabel/vvgng_ls/14667/', 'Кабель ВВГнг-LS 2х1.5, м.', 'ВВГнг-LS 2х1,5').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ВВГнг-LS 2х1,5"!')
            return()
    if check_vvg_ng_ls_2_25.get():
        try:
            ETPROM(int(enter_vvg_ng_ls_2_25.get()), 'https://etprom.by/catalog/kabel/vvgng_ls/17249/', 'Кабель ВВГнг-LS 2х2.5, м.', 'ВВГнг-LS 2х2,5').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ВВГнг-LS 2х2,5"!')
            return()
    if check_vvg_ng_ls_3_15.get():
        try:
            ETPROM(int(enter_vvg_ng_ls_3_15.get()), 'https://etprom.by/catalog/kabel/vvgng_ls/13528/', 'Кабель ВВГнг-LS 3х1.5, м.', 'ВВГнг-LS 3х1,5').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ВВГнг-LS 3х1,5"!')
            return()
    if check_vvg_ng_ls_3_25.get():
        try:
            ETPROM(int(enter_vvg_ng_ls_3_25.get()), 'https://etprom.by/catalog/kabel/vvgng_ls/14891/', 'Кабель ВВГнг-LS 3х2.5, м.', 'ВВГнг-LS 3х2,5').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ВВГнг-LS 3х2,5"!')
            return()
    if check_vvg_ng_ls_3_40.get():
        try:
            ETPROM(int(enter_vvg_ng_ls_3_40.get()), 'https://etprom.by/catalog/kabel/vvgng_ls/14673/', 'Кабель ВВГнг-LS 3х4, м.', 'ВВГнг-LS 3х4').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ВВГнг-LS 3х4"!')
            return()
    if check_vvg_ng_ls_3_60.get():
        try:
            ETPROM(int(enter_vvg_ng_ls_3_60.get()), 'https://etprom.by/catalog/kabel/vvgng_ls/14669/', 'Кабель ВВГнг-LS 3х6, м.', 'ВВГнг-LS 3х6').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ВВГнг-LS 3х6"!')
            return()
    if check_vvg_ng_ls_5_60.get():
        try:
            ETPROM(int(enter_vvg_ng_ls_5_60.get()), 'https://etprom.by/catalog/kabel/vvgng_ls/17405/', 'Кабель ВВГнг-LS 5х6, м.', 'ВВГнг-LS 5х6').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ВВГнг-LS 5х6"!')
            return()
# ЭЛЕКТРИКА: ШВВП
    if check_svvp_2_05.get():
        try:
            ETPROM(int(enter_svvp_2_05.get()), 'https://etprom.by/catalog/provod/shvvp/13407/', 'Провод ШВВП 2х0.5, м.', 'ШВВП 2х0,5').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ШВВП 2х0,5"!')
            return()
    if check_svvp_2_075.get():
        try:
            ETPROM(int(enter_svvp_2_075.get()), 'https://etprom.by/catalog/provod/shvvp/13480/', 'Провод ШВВП 2х0.75, м.', 'ШВВП 2х0,75').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ШВВП 2х0,75"!')
            return()
# ЭЛЕКТРИКА: АВВГ
    if check_avvg_2_10.get():
        try:
            ETPROM(int(enter_avvg_2_10.get()), 'https://etprom.by/catalog/kabel/avvg/14910/', 'Кабель АВВГ 2х10, м.', 'АВВГ 2х10').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "АВВГ 2х10"!')
            return()
    if check_avvg_2_16.get():
        try:
            ETPROM(int(enter_avvg_2_16.get()), 'https://etprom.by/catalog/kabel/avvg/13502/', 'Кабель АВВГ 2х16, м.', 'АВВГ 2х16').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "АВВГ 2х16"!')
            return()
# ЭЛЕКТРИКА: ПВС
    if check_pvs_2_15.get():
        try:
            ETPROM(int(enter_pvs_2_15.get()), 'https://etprom.by/catalog/provod/pvs/16545/', 'Провод ПВС 2х1.5, м.', 'ПВС 2х1.5').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ПВС 2х1.5"!')
            return()
# ЗВУК: МИКРОФОНЫ ДЛЯ ВИДЕО
    if check_stelberry_m70hd.get():
        try:
            STELBERRY(int(enter_stelberry_m70hd.get()), 'https://stelberry.by/series-m/m-70hd', 'Микрофон STELBERRY M-70HD, шт.', 'STELBERRY M-70HD').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "STELBERRY M-70HD"!')
            return()
    if check_stelberry_m80hd.get():
        try:
            STELBERRY(int(enter_stelberry_m80hd.get()), 'https://stelberry.by/series-m/m-80hd', 'Микрофон STELBERRY M-80HD, шт.', 'STELBERRY M-80HD').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "STELBERRY M-80HD"!')
            return()
    if check_stelberry_m90hd.get():
        try:
            STELBERRY(int(enter_stelberry_m90hd.get()), 'https://stelberry.by/series-m/m-90hd', 'Микрофон STELBERRY M-90HD, шт.', 'STELBERRY M-90HD').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "STELBERRY M-90HD"!')
            return()    
    if check_stelberry_mx225.get():
        try:
            STELBERRY(int(enter_stelberry_mx225.get()), 'https://stelberry.by/series-mx/mx-225', 'РоЕ-сплиттер STELBERRY MX-225, шт.', 'STELBERRY MX-225').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "STELBERRY MX-225"!')
            return()
# ЗВУК: МУЗЫКАЛЬНЫЕ УСИЛИТЕЛИ
    if check_ROXTON_AA_60M.get():
        try:
            SFERA(int(enter_ROXTON_AA_60M.get()), 'https://secur.by/katalog/sistemy-opoveshheniya-i-muzykalnoj-translyacii/translyacionnye-usiliteli/muzykalnye-usiliteli/roxton-aa-60m.html', 'ROXTON AA-60M Музыкальный усилитель, мощность 60W, частотный диапазон 150Hz-15kHz, сигнал/шум >60dB, коэф. искажений <0.5%, проигрыватель MP3/WMA, поддержка USB/SD накопителей, линейные аудиовходы 2xRCA и 1xTRS6.35, микрофонные аудиовходы 3xTRS6.35, аудиовыход 100V/70V/8Ом/4Ом, 230VАC/160W, 0...+40°C, (L)290х(W)270х(H)90mm', 'ROXTON AA-60M').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ROXTON AA-60M"!')
            return()
# ЗВУК: ГРОМКОГОВОРИТЕЛИ
    if check_ROXTON_PA_620T.get():
        try:
            SFERA(int(enter_ROXTON_PA_620T.get()), 'https://secur.by/katalog/sistemy-opoveshheniya-i-muzykalnoj-translyacii/translyacionnye-gromkogovoriteli/potolochnye-gromkogovoriteli/roxton-pa-620t.html', 'ROXTON PA-620T Потолочный громкоговоритель 6/3/1.5W, 91dB, 90-18000Hz, врезной, винтовые зажимы, корпус пластик, металлическая сетка, IP-41, (D)230х(H)80mm, цвет белый', 'ROXTON PA-620T').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ROXTON PA-620T"!')
            return()
# ЗВУК: МИКРОФОНЫ
    if check_ROXTON_RM_03.get():
        try:
            SFERA(int(enter_ROXTON_RM_03.get()), 'https://secur.by/katalog/sistemy-opoveshheniya-i-muzykalnoj-translyacii/mikrofony-i-mikrofonnye-konsoli/roxton-rm-03.html', 'ROXTON RM-03 Микрофон настольный, электретный, сигнал привлечения внимания, 3-pin XLRF, гибкий штатив, 60-18000Hz, шнур XLR-JACK 5m, питание 220VАC/50Гц или 1.5VDC(2xAA), корпус пластик, цвет черный', 'ROXTON RM-03').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "ROXTON RM-03"!')
            return()
# ДОМОФОНИЯ: ВЫЗЫВНЫЕ ПАНЕЛИ
    if check_HIKVISION_DS_KV6113_PE1.get():
        try:
            AVANT_SKD(int(enter_HIKVISION_DS_KV6113_PE1.get()), 'IP-домофоны Hikvision', 'DS-KV6113-PE1', 'HIKVISION DS-KV6113-PE1 Вызывная панель одноабонентская. Цветная камера CMOS 2MP HD, пластиковая, 1-канальный доступ к внутренней станции,Стандартный PoE / 12 В постоянного тока, модуль чтения карт Mifare;10M / 100M Самонастраивающийся Ethernet, 4-канальный тревожный вход, 1 реле для управления замком двери; IP65, 2 встроеных индикатора.-40 °C to +53 °C.138х65х27мм.', 'DS-KV6113-PE1').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DS-KV6113-PE1"!')
            return()  
    if check_Fanvil_i16.get():
        try:
            IPMATIKA(int(enter_Fanvil_i16.get()), "https://ipmatika.by/products/s-knopkoy-vyzova/Fanvil%20i16/", 'Fanvil i16 Видеодомофон с поддержкой SIP и PoE, шт.', 'Fanvil i16').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "Fanvil i16"!')
            return()
# ДОМОФОНИЯ: МОНИТОРЫ ДОМОФОНА
    if check_HIKVISION_DS_KH6320_TE1.get():
        try:
            AVANT_SKD(int(enter_HIKVISION_DS_KH6320_TE1.get()), 'IP-домофоны Hikvision', 'DS-KH6320-TE1', 'HIKVISION DS-KH6320-TE1 Монитор домофонной системы  с сенсорным экраном 7 дюймов,TFT LCD, разрешение дисплея: 1024 * 600. 10/100 Мбит / с Ethernet, стандартное PoE / 12 В пост. Поддержка стандартного SIP протокола. TF карта, максимум 32G. 8-канальный вход тревоги. Размер 200 х140х15.1 мм', 'DS-KH6320-TE1').find_price()
        except:
            messagebox.showinfo('Внимание!', 'Введите целое значение для "DS-KH6320-TE1"!')
            return()
# ПРОЧИЕ МАТЕРИАЛЫ
    if check_dop_material.get():
        try:
            material_list.append("Прочие материалы (стяжки, дюбель-гвозди, саморезы, изолента и т.д.)")
            short_name_list.append("Прочие материалы")
            kolvo_list.append(enter_dop_material.get())
            cena_s_nds_list.append(18.00)
            cena_bez_nds_list.append(18.00/1.2)
        except:
            messagebox.showerror('Внимание!', 'Введите целое значение для "Дополнительные материалы"!')
            return()

# РАБОТЫ
    wrk = WORK('Скрытая прокладка кабеля',                                      0.98,   check_work1, enter_work1).find_price()
    wrk = WORK('Открытая прокладка кабеля',                                     2.38,   check_work2, enter_work2).find_price()
    wrk = WORK('Установка кабель-канала шириной менее 60мм',                    4.32,   check_work3, enter_work3).find_price()
    wrk = WORK('Установка кабель-канала шириной более 60мм',                    4.75,   check_work4, enter_work4).find_price()
    wrk = WORK('Установка аксессуаров для кабель-каналов',                      1.30,   check_work5, enter_work5).find_price()
    wrk = WORK('Открытие/закрытие установленного кабель-канала',                1.30,   check_work6, enter_work6).find_price()
    wrk = WORK('Снятие установленного кабель-канала',                           1.73,   check_work7, enter_work7).find_price()
    wrk = WORK('Установка трубы гофрированной',                                 3.46,   check_work8, enter_work8).find_price()
    wrk = WORK('Сверление отверстия',                                           12.96,  check_work9, enter_work9).find_price()
    wrk = WORK('Установка подрозетника в стену',                                3.24,   check_work10, enter_work10).find_price()
    wrk = WORK('Установка стяжек на потолки и стены из твердых материалов',     3.89,   check_work11, enter_work11).find_price()
    wrk = WORK('Сборка и установка шкафа телекоммуникационного напольного',     108.00, check_work12, enter_work12).find_price()
    wrk = WORK('Сборка и установка шкафа телекоммуникационного настенного',     75.60,  check_work13, enter_work13).find_price()
    wrk = WORK('Установка оборудования в шкаф',                                 12.00,  check_work14, enter_work14).find_price()
    wrk = WORK('Установка оборудования на стену',                               15.12,  check_work15, enter_work15).find_price()
    wrk = WORK('Расключение розетки',                                           8.21,   check_work16, enter_work16).find_price()
    wrk = WORK('Обжим коннектора',                                              2.38,   check_work17, enter_work17).find_price()
    wrk = WORK('Кроссирование патч-панели',                                     4.22,   check_work18, enter_work18).find_price()
    wrk = WORK('Кроссирование плинтов KRONE, рапределительной коробки',         1.30,   check_work19, enter_work19).find_price()
    wrk = WORK('Тестирование и маркировка порта линк-тестером',                 2.16,   check_work20, enter_work20).find_price()
    wrk = WORK('Прокладка ВОК для внутр. прокладки',                            1.73,   check_work21, enter_work21).find_price()
    wrk = WORK('Прокладка бронированного ВОК',                                  2.38,   check_work22, enter_work22).find_price()
    wrk = WORK('Оконцевание ВОК',                                               32.40,  check_work23, enter_work23).find_price()
    wrk = WORK('Тестирование волоконно-оптического кабеля',                     12.96,  check_work24, enter_work24).find_price()
    wrk = WORK('Сборка-разборка фальшпотолков или полов',                       5.18,   check_work25, enter_work25).find_price()
    wrk = WORK('Прочие дополнительные сетевые работы',                          80.00,  check_work26, enter_work26).find_price()
    wrk = WORK('Транспортные расходы',                                          00.50,  check_work27, enter_work27).find_price()

# РЕЗУЛЬТАТ
    result = Tk()
    result.geometry('600x400+200+100')
    result.title("Result")  

    frame1 = LabelFrame(result, text='ОБОРУДОВАНИЕ/МАТЕРИАЛЫ', padx=5, pady=5, fg='red')
    frame1.grid(row=0, column=0, sticky=NW)

    lbl = Label(frame1, text='Номер')
    lbl.grid(row=1, column=0, sticky=W)
    lbl = Label(frame1, text='Наименование')
    lbl.grid(row=1, column=1, sticky=W)
    lbl = Label(frame1, text='Цена без НДС')
    lbl.grid(row=1, column=2)
    lbl = Label(frame1, text='Цена c НДС')
    lbl.grid(row=1, column=3)

    num = 1
    row_num = 2
    col_num = 0
    for kolvo in kolvo_list:
        lbl = Label(frame1, text=num)
        lbl.grid(row=row_num, column=col_num)
        num += 1
        row_num += 1
    row_num = 2
    col_num = 1
    for material in short_name_list:
        lbl = Label(frame1, text=str(material))
        lbl.grid(row=row_num, column=col_num, sticky=W)
        row_num += 1        
    row_num = 2
    col_num = 2
    for cena in cena_bez_nds_list:
        lbl = Label(frame1, text = str("%.2f" % cena), relief=RIDGE, fg='red')
        lbl.grid(row=row_num, column=col_num)
        row_num += 1
    row_num = 2
    col_num = 3
    for cena in cena_s_nds_list:
        lbl = Label(frame1, text = str("%.2f" % cena), relief=RIDGE, fg='red')
        lbl.grid(row=row_num, column=col_num)
        row_num += 1

    frame2 = LabelFrame(result, text='РАБОТЫ', padx=5, pady=5, fg='red')
    frame2.grid(row=0, column=2, sticky=NW)

    lbl = Label(frame2, text='Номер')
    lbl.grid(row=1, column=0, sticky=W)
    lbl = Label(frame2, text='Наименование')
    lbl.grid(row=1, column=1, sticky=W)
    lbl = Label(frame2, text='Количество')
    lbl.grid(row=1, column=2)
    lbl = Label(frame2, text='Цена за единицу')
    lbl.grid(row=1, column=3)
    lbl = Label(frame2, text='Цена за все')
    lbl.grid(row=1, column=4)

    num = 1
    row_num = 2
    col_num = 0
    for material in name_of_work:
        lbl = Label(frame2, text=num)
        lbl.grid(row=row_num, column=col_num)
        num += 1
        row_num += 1
    row_num = 2
    col_num = 1
    for material in name_of_work:
        lbl = Label(frame2, text=str(material))
        lbl.grid(row=row_num, column=col_num, sticky=W)
        row_num += 1        
    row_num = 2
    col_num = 2
    for cena in kolvo_of_work:
        lbl = Label(frame2, text = str("%.2f" % cena), relief=RIDGE, fg='red')
        lbl.grid(row=row_num, column=col_num)
        row_num += 1
    row_num = 2
    col_num = 3
    for cena in price_per_one:
        lbl = Label(frame2, text = str("%.2f" % cena), relief=RIDGE, fg='red')
        lbl.grid(row=row_num, column=col_num)
        row_num += 1    
    row_num = 2
    col_num = 4
    stoimost_raboty = 0
    for cena in price_of_work:
        lbl = Label(frame2, text = str("%.2f" % cena), relief=RIDGE, fg='red')
        lbl.grid(row=row_num, column=col_num)
        stoimost_raboty += cena
        row_num += 1  

    frame3 = LabelFrame(result, text='ИТОГИ РАСЧЕТА', padx=5, pady=5, fg='red')
    frame3.grid(row=0, column=22, sticky=NW)

    lbl = Label(frame3, text='Стоимость работ без НДС')
    lbl.grid(row=2, column=0, sticky=W)
    lbl = Label(frame3, text = str("%.2f" % stoimost_raboty), relief=RIDGE, fg='red')
    lbl.grid(row=2, column=1, sticky=E)

    lbl = Label(frame3, text='Наименование объекта').grid(row=3, column=0, sticky=W)
    name_of_file = Entry(frame3, width=30)
    name_of_file.grid(row=3, column=1, sticky=W)

    btn = Button(frame3, text='Сохранить в Excel', command=make_doc)
    btn.grid(row=30, column=0, sticky=W)

    description_of_work = 'Монтажные работы:'
    if text_1.get():
        description_of_work = description_of_work + ' прокладка кабеля,'
    if text_2.get():
        description_of_work = description_of_work + ' установка кабель-канала,'
    if text_3.get():
        description_of_work = description_of_work + ' установка трубы гофрированной,'
    if text_14.get():
        description_of_work = description_of_work + ' монтаж сетевых розеток,'
    if text_4.get():
        description_of_work = description_of_work + ' сборка и установка шкафа телекоммуникационного,'
    if text_6.get():
        description_of_work = description_of_work + ' кроссирование патч-панелей,'
    if text_7.get():
        description_of_work = description_of_work + ' прокладка ВОК,'
    if text_8.get():
        description_of_work = description_of_work + ' сварка ВОК,'
    if text_9.get():
        description_of_work = description_of_work + ' установка сетевого оборудования,'
    if text_13.get():
        description_of_work = description_of_work + ' установка видеокамер,'        
    if text_10.get():
        description_of_work = description_of_work + ' пуско-наладочные работы,'
    if text_11.get():
        description_of_work = description_of_work + ' транспортные расходы,'
    if text_12.get():
        description_of_work = description_of_work + ' прочие дополнительные сетевые работы,'

    description_of_work = description_of_work[:-1]

    datastream_price.close()
    avant_video_price.close()
    avant_skd_price.close()
    netair_price.close()
    result.mainloop()



# create program window
root = Tk()
root.attributes('-zoomed',True)
root.title('First Number')
root.iconphoto(True, PhotoImage(file='/home/' + str(os.environ.get( "USERNAME" )) + 
            '/Documents/Logo/logo_fn.png'))

# create menu
main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label = 'Datastream Price', command = download_datastream)
file_menu.add_command(label = 'Avant Video Price', command = download_avant_video)
file_menu.add_command(label = 'Avant Skd Price', command = download_avant_skd)
file_menu.add_command(label = 'Netair Price', command = download_netair)
file_menu.add_separator()
file_menu.add_command(label = 'Delete all prices', command = delete_prices)

main_menu.add_cascade(label = 'PRICES', menu = file_menu)
main_menu.add_command(label = 'SKS', command = get_input)
main_menu.add_command(label = 'EXIT', command = close_program)

root.config(menu = main_menu)


# create tabs
# создание вкладок
tab = ttk.Notebook(root)

tab1 = ttk.Frame(tab)
tab.add(tab1, text='МАТЕРИАЛЫ')
tab.pack(fill='both', expand=True)

tab2 = ttk.Frame(tab)
tab.add(tab2, text='ГОФРА/КОРОБА')
tab.pack(fill='both', expand=True)

tab3 = ttk.Frame(tab)
tab.add(tab3, text='ШКАФЫ')
tab.pack(fill='both', expand=True)

tab4 = ttk.Frame(tab)
tab.add(tab4, text='ВИДЕОРЕГИСТРАТОРЫ')
tab.pack(fill='both', expand=True)

tab5 = ttk.Frame(tab)
tab.add(tab5, text='ВИДЕОКАМЕРЫ')
tab.pack(fill='both', expand=True)

tab6 = ttk.Frame(tab)
tab.add(tab6, text='ДЛЯ ВИДЕО')
tab.pack(fill='both', expand=True)

tab7 = ttk.Frame(tab)
tab.add(tab7, text='БЛОКИ ПИТАНИЯ')
tab.pack(fill='both', expand=True)

tab8 = ttk.Frame(tab)
tab.add(tab8, text='СКУД')
tab.pack(fill='both', expand=True)

tab9 = ttk.Frame(tab)
tab.add(tab9, text='ПО СКУД')
tab.pack(fill='both', expand=True)

tab11 = ttk.Frame(tab)
tab.add(tab11, text='КОММУТАТОРЫ')
tab.pack(fill='both', expand=True)

tab12 = ttk.Frame(tab)
tab.add(tab12, text='ЭЛЕКТРИКА')
tab.pack(fill='both', expand=True)

tab13 = ttk.Frame(tab)
tab.add(tab13, text='ЗВУК')
tab.pack(fill='both', expand=True)

tab14 = ttk.Frame(tab)
tab.add(tab14, text='ДОМОФОНИЯ')
tab.pack(fill='both', expand=True)

tab100 = ttk.Frame(tab)
tab.add(tab100, text='РАБОТЫ')
tab.pack(fill='both', expand=True)

# переменные
cnt = 0             # счетчик количества позиций
width_of_entry = 3  # ширина поля ввода

frame_1_1 = LabelFrame(tab1, text='UTP/FTP/COAX', padx=5, pady=5, fg='red')
frame_1_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_utp5e = BooleanVar()
Checkbutton(frame_1_1, text='UTP 5E                              ', variable=check_utp5e).grid(row=temp_row, column=temp_col1, sticky=W)
enter_utp5e = Entry(frame_1_1, width=width_of_entry)
enter_utp5e.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_utp5e_lszh = BooleanVar()
Checkbutton(frame_1_1, text='UTP 5E LSZH', variable=check_utp5e_lszh).grid(row=temp_row, column=temp_col1, sticky=W)
enter_utp5e_lszh = Entry(frame_1_1, width=width_of_entry)
enter_utp5e_lszh.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_utp5e_out = BooleanVar()
Checkbutton(frame_1_1, text='UTP 5E OUT', variable=check_utp5e_out).grid(row=temp_row, column=temp_col1, sticky=W)
enter_utp5e_out = Entry(frame_1_1, width=width_of_entry)
enter_utp5e_out.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_ftp5e = BooleanVar()
Checkbutton(frame_1_1, text='FTP 5E', variable=check_ftp5e).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ftp5e = Entry(frame_1_1, width=width_of_entry)
enter_ftp5e.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_ftp5e_lszh = BooleanVar()
Checkbutton(frame_1_1, text='FTP 5E LSZH', variable=check_ftp5e_lszh).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ftp5e_lszh = Entry(frame_1_1, width=width_of_entry)
enter_ftp5e_lszh.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_ftp5e_out = BooleanVar()
Checkbutton(frame_1_1, text='FTP 5E OUT', variable=check_ftp5e_out).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ftp5e_out = Entry(frame_1_1, width=width_of_entry)
enter_ftp5e_out.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_utp6 = BooleanVar()
Checkbutton(frame_1_1, text='UTP 6', variable=check_utp6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_utp6 = Entry(frame_1_1, width=width_of_entry)
enter_utp6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_utp6_lszh = BooleanVar()
Checkbutton(frame_1_1, text='UTP 6 LSZH', variable=check_utp6_lszh).grid(row=temp_row, column=temp_col1, sticky=W)
enter_utp6_lszh = Entry(frame_1_1, width=width_of_entry)
enter_utp6_lszh.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_ftp6 = BooleanVar()
Checkbutton(frame_1_1, text='FTP 6', variable=check_ftp6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ftp6 = Entry(frame_1_1, width=width_of_entry)
enter_ftp6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_ftp6_lszh = BooleanVar()
Checkbutton(frame_1_1, text='FTP 6 LSZH', variable=check_ftp6_lszh).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ftp6_lszh = Entry(frame_1_1, width=width_of_entry)
enter_ftp6_lszh.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_rg6 = BooleanVar()
Checkbutton(frame_1_1, text='Кабель RG-6', variable=check_rg6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_rg6 = Entry(frame_1_1, width=width_of_entry)
enter_rg6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_1_2 = LabelFrame(tab1, text='ОПТИЧЕСКИЙ КАБЕЛЬ', padx=5, pady=5, fg='red')
frame_1_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_vok2 = BooleanVar()
Checkbutton(frame_1_2, text='ВОК 2 жилы', variable=check_vok2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vok2 = Entry(frame_1_2, width=width_of_entry)
enter_vok2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_vok4 = BooleanVar()
Checkbutton(frame_1_2, text='ВОК 4 жилы', variable=check_vok4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vok4 = Entry(frame_1_2, width=width_of_entry)
enter_vok4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_vok8 = BooleanVar()
Checkbutton(frame_1_2, text='ВОК 8 жил', variable=check_vok8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vok8 = Entry(frame_1_2, width=width_of_entry)
enter_vok8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_vok12 = BooleanVar()
Checkbutton(frame_1_2, text='ВОК 12 жил', variable=check_vok12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vok12 = Entry(frame_1_2, width=width_of_entry)
enter_vok12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_vok16 = BooleanVar()
Checkbutton(frame_1_2, text='ВОК 16 жил', variable=check_vok16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vok16 = Entry(frame_1_2, width=width_of_entry)
enter_vok16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_vok24 = BooleanVar()
Checkbutton(frame_1_2, text='ВОК 24 жилы', variable=check_vok24).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vok24 = Entry(frame_1_2, width=width_of_entry)
enter_vok24.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_1_6 = LabelFrame(tab1, text='ОПТИЧЕСКОЕ ОБОРУДОВАНИЕ', padx=5, pady=5, fg='red')
frame_1_6.grid(row=0, column=20, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_opt_kross_16_SC = BooleanVar()
Checkbutton(frame_1_6, text='Кросс оптический 16', variable=check_opt_kross_16_SC).grid(row=temp_row, column=temp_col1, sticky=W)
enter_opt_kross_16_SC = Entry(frame_1_6, width=width_of_entry)
enter_opt_kross_16_SC.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_opt_kross_24_SC = BooleanVar()
Checkbutton(frame_1_6, text='Кросс оптический 24', variable=check_opt_kross_24_SC).grid(row=temp_row, column=temp_col1, sticky=W)
enter_opt_kross_24_SC = Entry(frame_1_6, width=width_of_entry)
enter_opt_kross_24_SC.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_PT_SC_APC_SM = BooleanVar()
Checkbutton(frame_1_6, text='Пигтейл SC APC SM', variable=check_PT_SC_APC_SM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_PT_SC_APC_SM = Entry(frame_1_6, width=width_of_entry)
enter_PT_SC_APC_SM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_PT_SC_UPC_SM = BooleanVar()
Checkbutton(frame_1_6, text='Пигтейл SC UPC SM', variable=check_PT_SC_UPC_SM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_PT_SC_UPC_SM = Entry(frame_1_6, width=width_of_entry)
enter_PT_SC_UPC_SM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_PT_LC_UPC_SM = BooleanVar()
Checkbutton(frame_1_6, text='Пигтейл LC UPC SM', variable=check_PT_LC_UPC_SM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_PT_LC_UPC_SM = Entry(frame_1_6, width=width_of_entry)
enter_PT_LC_UPC_SM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_PT_FC_UPC_SM = BooleanVar()
Checkbutton(frame_1_6, text='Пигтейл FC UPC SM', variable=check_PT_FC_UPC_SM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_PT_FC_UPC_SM = Entry(frame_1_6, width=width_of_entry)
enter_PT_FC_UPC_SM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_PT_ST_UPC_SM = BooleanVar()
Checkbutton(frame_1_6, text='Пигтейл ST UPC SM', variable=check_PT_ST_UPC_SM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_PT_ST_UPC_SM = Entry(frame_1_6, width=width_of_entry)
enter_PT_ST_UPC_SM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_PT_LC_PC_MM = BooleanVar()
Checkbutton(frame_1_6, text='Пигтейл LC PC MM', variable=check_PT_LC_PC_MM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_PT_LC_PC_MM = Entry(frame_1_6, width=width_of_entry)
enter_PT_LC_PC_MM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_kdzs = BooleanVar()
Checkbutton(frame_1_6, text='КДЗС', variable=check_kdzs).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kdzs = Entry(frame_1_6, width=width_of_entry)
enter_kdzs.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_sfp_module = BooleanVar()
Checkbutton(frame_1_6, text='SFP-модуль', variable=check_sfp_module).grid(row=temp_row, column=temp_col1, sticky=W)
enter_sfp_module = Entry(frame_1_6, width=width_of_entry)
enter_sfp_module.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_1_3 = LabelFrame(tab1, text='РОЗЕТКИ', padx=5, pady=5, fg='red')
frame_1_3.grid(row=0, column=30, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_roz1x = BooleanVar()
Checkbutton(frame_1_3, text='TWT 1хRJ45', variable=check_roz1x).grid(row=temp_row, column=temp_col1, sticky=W)
enter_roz1x = Entry(frame_1_3, width=width_of_entry)
enter_roz1x.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_roz2x = BooleanVar()
Checkbutton(frame_1_3, text='TWT 2хRJ45', variable=check_roz2x).grid(row=temp_row, column=temp_col1, sticky=W)
enter_roz2x = Entry(frame_1_3, width=width_of_entry)
enter_roz2x.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_roz1x_quteo = BooleanVar()
Checkbutton(frame_1_3, text='Legrand Quteo 1хRJ45', variable=check_roz1x_quteo).grid(row=temp_row, column=temp_col1, sticky=W)
enter_roz1x_quteo = Entry(frame_1_3, width=width_of_entry)
enter_roz1x_quteo.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_roz2x_quteo = BooleanVar()
Checkbutton(frame_1_3, text='Legrand Quteo 2хRJ45', variable=check_roz2x_quteo).grid(row=temp_row, column=temp_col1, sticky=W)
enter_roz2x_quteo = Entry(frame_1_3, width=width_of_entry)
enter_roz2x_quteo.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_1_4 = LabelFrame(tab1, text='ПАТЧ-ПАНЕЛИ', padx=5, pady=5, fg='red')
frame_1_4.grid(row=0, column=40, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_pp12 = BooleanVar()
Checkbutton(frame_1_4, text='Патч-панель 12 портов', variable=check_pp12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pp12 = Entry(frame_1_4, width=width_of_entry)
enter_pp12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pp24 = BooleanVar()
Checkbutton(frame_1_4, text='Патч-панель 24 порта', variable=check_pp24).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pp24 = Entry(frame_1_4, width=width_of_entry)
enter_pp24.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pp48 = BooleanVar()
Checkbutton(frame_1_4, text='Патч-панель 48 портов', variable=check_pp48).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pp48 = Entry(frame_1_4, width=width_of_entry)
enter_pp48.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_1_5 = LabelFrame(tab1, text='КОННЕКТОРЫ', padx=5, pady=5, fg='red')
frame_1_5.grid(row=0, column=50, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_conn_rj45 = BooleanVar()
Checkbutton(frame_1_5, text='Коннектор RJ45', variable=check_conn_rj45).grid(row=temp_row, column=temp_col1, sticky=W)
enter_conn_rj45 = Entry(frame_1_5, width=width_of_entry)
enter_conn_rj45.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_colp_rj45 = BooleanVar()
Checkbutton(frame_1_5, text='Колпачок RJ45', variable=check_colp_rj45).grid(row=temp_row, column=temp_col1, sticky=W)
enter_colp_rj45 = Entry(frame_1_5, width=width_of_entry)
enter_colp_rj45.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_ap_008 = BooleanVar()
Checkbutton(frame_1_5, text='Разъем питания', variable=check_ap_008).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ap_008 = Entry(frame_1_5, width=width_of_entry)
enter_ap_008.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_f_connector = BooleanVar()
Checkbutton(frame_1_5, text='F коннектор', variable=check_f_connector).grid(row=temp_row, column=temp_col1, sticky=W)
enter_f_connector = Entry(frame_1_5, width=width_of_entry)
enter_f_connector.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_f_razjem = BooleanVar()
Checkbutton(frame_1_5, text='Разъем BNC под F', variable=check_f_razjem).grid(row=temp_row, column=temp_col1, sticky=W)
enter_f_razjem = Entry(frame_1_5, width=width_of_entry)
enter_f_razjem.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_BNC_vint = BooleanVar()
Checkbutton(frame_1_5, text='Разъем BNC под винт', variable=check_BNC_vint).grid(row=temp_row, column=temp_col1, sticky=W)
enter_BNC_vint = Entry(frame_1_5, width=width_of_entry)
enter_BNC_vint.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_1_7 = LabelFrame(tab1, text='ПАТЧ-КОРДЫ', padx=5, pady=5, fg='red')
frame_1_7.grid(row=0, column=60, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_pk03 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 0.3м', variable=check_pk03).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk03 = Entry(frame_1_7, width=width_of_entry)
enter_pk03.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk05 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 0.5м', variable=check_pk05).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk05 = Entry(frame_1_7, width=width_of_entry)
enter_pk05.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk10 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 1.0м', variable=check_pk10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk10 = Entry(frame_1_7, width=width_of_entry)
enter_pk10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk15 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 1.5м', variable=check_pk15).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk15 = Entry(frame_1_7, width=width_of_entry)
enter_pk15.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk20 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 2.0м', variable=check_pk20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk20 = Entry(frame_1_7, width=width_of_entry)
enter_pk20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk30 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 3.0м', variable=check_pk30).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk30 = Entry(frame_1_7, width=width_of_entry)
enter_pk30.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk50 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 5.0м', variable=check_pk50).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk50 = Entry(frame_1_7, width=width_of_entry)
enter_pk50.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk70 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 7.0м', variable=check_pk70).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk70 = Entry(frame_1_7, width=width_of_entry)
enter_pk70.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk100 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 10.0м', variable=check_pk100).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk100 = Entry(frame_1_7, width=width_of_entry)
enter_pk100.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_pk150 = BooleanVar()
Checkbutton(frame_1_7, text='Патч-корд 15.0м', variable=check_pk150).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pk150 = Entry(frame_1_7, width=width_of_entry)
enter_pk150.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_1_8 = LabelFrame(tab1, text='ДЛЯ ШКАФОВ', padx=5, pady=5, fg='red')
frame_1_8.grid(row=0, column=70, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_elroz = BooleanVar()
Checkbutton(frame_1_8, text='Блок розеток', variable=check_elroz).grid(row=temp_row, column=temp_col1, sticky=W)
enter_elroz = Entry(frame_1_8, width=width_of_entry)
enter_elroz.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_elwire = BooleanVar()
Checkbutton(frame_1_8, text='Шнур питания', variable=check_elwire).grid(row=temp_row, column=temp_col1, sticky=W)
enter_elwire = Entry(frame_1_8, width=width_of_entry)
enter_elwire.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_organizer = BooleanVar()
Checkbutton(frame_1_8, text='Органайзер', variable=check_organizer).grid(row=temp_row, column=temp_col1, sticky=W)
enter_organizer = Entry(frame_1_8, width=width_of_entry)
enter_organizer.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_polka_280 = BooleanVar()
Checkbutton(frame_1_8, text='Полка 280мм', variable=check_polka_280).grid(row=temp_row, column=temp_col1, sticky=W)
enter_polka_280 = Entry(frame_1_8, width=width_of_entry)
enter_polka_280.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_ibp = BooleanVar()
Checkbutton(frame_1_8, text='ИБП', variable=check_ibp).grid(row=4, column=0, sticky=W)
enter_ibp = Entry(frame_1_8, width=width_of_entry)
enter_ibp.grid(row=4, column=1, sticky=W)
cnt += 1
temp_row += 1

frame_1_9 = LabelFrame(tab1, text='ПРОЧИЕ МАТЕРИАЛЫ', padx=5, pady=5, fg='red')
frame_1_9.grid(row=1, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_krp1 = BooleanVar()
Checkbutton(frame_1_9, text='КРП 100х100', variable=check_krp1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_krp1 = Entry(frame_1_9, width=width_of_entry)
enter_krp1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_komplekt2_25 = BooleanVar()
Checkbutton(frame_1_9, text='Клипсы для ТКШ 25 шт', variable=check_komplekt2_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_komplekt2_25 = Entry(frame_1_9, width=width_of_entry)
enter_komplekt2_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_komplekt2_50 = BooleanVar()
Checkbutton(frame_1_9, text='Клипсы для ТКШ 50 шт', variable=check_komplekt2_50).grid(row=temp_row, column=temp_col1, sticky=W)
enter_komplekt2_50 = Entry(frame_1_9, width=width_of_entry)
enter_komplekt2_50.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_poe_kit = BooleanVar()
Checkbutton(frame_1_9, text='PoE-инжектор', variable=check_poe_kit).grid(row=temp_row, column=temp_col1, sticky=W)
enter_poe_kit = Entry(frame_1_9, width=width_of_entry)
enter_poe_kit.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_dop_material = BooleanVar()
Checkbutton(frame_1_9, text='Прочие материалы', variable=check_dop_material).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dop_material = Entry(frame_1_9, width=width_of_entry)
enter_dop_material.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_2_1 = LabelFrame(tab2, text='КАБЕЛЬ-КАНАЛ', padx=5, pady=5, fg='red')
frame_2_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_kk1616 = BooleanVar()
Checkbutton(frame_2_1, text='Кабель-канал 16х16', variable=check_kk1616).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kk1616 = Entry(frame_2_1, width=width_of_entry)
enter_kk1616.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_kk2516 = BooleanVar()
Checkbutton(frame_2_1, text='Кабель-канал 25х16', variable=check_kk2516).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kk2516 = Entry(frame_2_1, width=width_of_entry)
enter_kk2516.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_kk2525 = BooleanVar()
Checkbutton(frame_2_1, text='Кабель-канал 25х25', variable=check_kk2525).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kk2525 = Entry(frame_2_1, width=width_of_entry)
enter_kk2525.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_kk4016 = BooleanVar()
Checkbutton(frame_2_1, text='Кабель-канал 40х16', variable=check_kk4016).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kk4016 = Entry(frame_2_1, width=width_of_entry)
enter_kk4016.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_kk4025 = BooleanVar()
Checkbutton(frame_2_1, text='Кабель-канал 40х25', variable=check_kk4025).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kk4025 = Entry(frame_2_1, width=width_of_entry)
enter_kk4025.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_kk4040 = BooleanVar()
Checkbutton(frame_2_1, text='Кабель-канал 40х40', variable=check_kk4040).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kk4040 = Entry(frame_2_1, width=width_of_entry)
enter_kk4040.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_kklo75 = BooleanVar()
Checkbutton(frame_2_1, text='Кабель-канал LO75', variable=check_kklo75).grid(row=temp_row, column=temp_col1, sticky=W)
enter_kklo75 = Entry(frame_2_1, width=width_of_entry)
enter_kklo75.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_2_2 = LabelFrame(tab2, text='ТРУБА ПВХ, ПНД', padx=5, pady=5, fg='red')
frame_2_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_gofra_16 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра д.16', variable=check_gofra_16, anchor=W).grid(row=temp_row, column=temp_col1, sticky=W)
enter_gofra_16 = Entry(frame_2_2, width=width_of_entry)
enter_gofra_16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_gofra_20 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра д.20', variable=check_gofra_20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_gofra_20 = Entry(frame_2_2, width=width_of_entry)
enter_gofra_20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_gofra_25 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра д.25', variable=check_gofra_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_gofra_25 = Entry(frame_2_2, width=width_of_entry)
enter_gofra_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_gofra_32 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра д.32', variable=check_gofra_32).grid(row=temp_row, column=temp_col1, sticky=W)
enter_gofra_32 = Entry(frame_2_2, width=width_of_entry)
enter_gofra_32.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_gofra_40 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра д.40', variable=check_gofra_40).grid(row=temp_row, column=temp_col1, sticky=W)
enter_gofra_40 = Entry(frame_2_2, width=width_of_entry)
enter_gofra_40.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_gofra_50 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра д.50', variable=check_gofra_50).grid(row=temp_row, column=temp_col1, sticky=W)
enter_gofra_50 = Entry(frame_2_2, width=width_of_entry)
enter_gofra_50.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_pnd_16 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра ПНД д.16', variable=check_pnd_16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pnd_16 = Entry(frame_2_2, width=width_of_entry)
enter_pnd_16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_pnd_20 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра ПНД д.20', variable=check_pnd_20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pnd_20 = Entry(frame_2_2, width=width_of_entry)
enter_pnd_20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_pnd_25 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра ПНД д.25', variable=check_pnd_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pnd_25 = Entry(frame_2_2, width=width_of_entry)
enter_pnd_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_pnd_32 = BooleanVar()
Checkbutton(frame_2_2, text='Гофра ПНД д.32', variable=check_pnd_32).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pnd_32 = Entry(frame_2_2, width=width_of_entry)
enter_pnd_32.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_truba_16 = BooleanVar()
Checkbutton(frame_2_2, text='Труба ПВХ жесткая 16', variable=check_truba_16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_truba_16 = Entry(frame_2_2, width=width_of_entry)
enter_truba_16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_truba_20 = BooleanVar()
Checkbutton(frame_2_2, text='Труба ПВХ жесткая 20', variable=check_truba_20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_truba_20 = Entry(frame_2_2, width=width_of_entry)
enter_truba_20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_truba_25 = BooleanVar()
Checkbutton(frame_2_2, text='Труба ПВХ жесткая 25', variable=check_truba_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_truba_25 = Entry(frame_2_2, width=width_of_entry)
enter_truba_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_truba_32 = BooleanVar()
Checkbutton(frame_2_2, text='Труба ПВХ жесткая 32', variable=check_truba_32).grid(row=temp_row, column=temp_col1, sticky=W)
enter_truba_32 = Entry(frame_2_2, width=width_of_entry)
enter_truba_32.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_truba_40 = BooleanVar()
Checkbutton(frame_2_2, text='Труба ПВХ жесткая 40', variable=check_truba_40).grid(row=temp_row, column=temp_col1, sticky=W)
enter_truba_40 = Entry(frame_2_2, width=width_of_entry)
enter_truba_40.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_truba_50 = BooleanVar()
Checkbutton(frame_2_2, text='Труба ПВХ жесткая 50', variable=check_truba_50).grid(row=temp_row, column=temp_col1, sticky=W)
enter_truba_50 = Entry(frame_2_2, width=width_of_entry)
enter_truba_50.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                            
check_truba_63 = BooleanVar()
Checkbutton(frame_2_2, text='Труба ПВХ жесткая 63', variable=check_truba_63).grid(row=temp_row, column=temp_col1, sticky=W)
enter_truba_63 = Entry(frame_2_2, width=width_of_entry)
enter_truba_63.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                       

frame_2_3 = LabelFrame(tab2, text='АКСЕССУАРЫ ДЛЯ ТРУБ', padx=5, pady=5, fg='red')
frame_2_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_klipsa_16 = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 16', variable=check_klipsa_16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_16 = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
temp_row += 1
check_klipsa_20 = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 20', variable=check_klipsa_20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_20 = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_25 = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 25', variable=check_klipsa_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_25 = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_32 = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 32', variable=check_klipsa_32).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_32 = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_32.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_40 = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 40', variable=check_klipsa_40).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_40 = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_40.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_50 = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 50', variable=check_klipsa_50).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_50 = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_50.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_16_z = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 16 (замок)', variable=check_klipsa_16_z).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_16_z = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_16_z.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_20_z = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 20 (замок)', variable=check_klipsa_20_z).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_20_z = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_20_z.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_25_z = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 25 (замок)', variable=check_klipsa_25_z).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_25_z = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_25_z.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_klipsa_32_z = BooleanVar()
Checkbutton(frame_2_3, text='Клипса 32 (замок)', variable=check_klipsa_32_z).grid(row=temp_row, column=temp_col1, sticky=W)
enter_klipsa_32_z = Entry(frame_2_3, width=width_of_entry)
enter_klipsa_32_z.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_mufta_16 = BooleanVar()
Checkbutton(frame_2_3, text='Муфта 16', variable=check_mufta_16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_mufta_16 = Entry(frame_2_3, width=width_of_entry)
enter_mufta_16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_mufta_20 = BooleanVar()
Checkbutton(frame_2_3, text='Муфта 20', variable=check_mufta_20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_mufta_20 = Entry(frame_2_3, width=width_of_entry)
enter_mufta_20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_mufta_25 = BooleanVar()
Checkbutton(frame_2_3, text='Муфта 25', variable=check_mufta_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_mufta_25 = Entry(frame_2_3, width=width_of_entry)
enter_mufta_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_mufta_32 = BooleanVar()
Checkbutton(frame_2_3, text='Муфта 32', variable=check_mufta_32).grid(row=temp_row, column=temp_col1, sticky=W)
enter_mufta_32 = Entry(frame_2_3, width=width_of_entry)
enter_mufta_32.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_mufta_40 = BooleanVar()
Checkbutton(frame_2_3, text='Муфта 40', variable=check_mufta_40).grid(row=temp_row, column=temp_col1, sticky=W)
enter_mufta_40 = Entry(frame_2_3, width=width_of_entry)
enter_mufta_40.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_mufta_50 = BooleanVar()
Checkbutton(frame_2_3, text='Муфта 50', variable=check_mufta_50).grid(row=temp_row, column=temp_col1, sticky=W)
enter_mufta_50 = Entry(frame_2_3, width=width_of_entry)
enter_mufta_50.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_povorot_16 = BooleanVar()
Checkbutton(frame_2_3, text='Гибкий поворот 16', variable=check_povorot_16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_povorot_16 = Entry(frame_2_3, width=width_of_entry)
enter_povorot_16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_povorot_20 = BooleanVar()
Checkbutton(frame_2_3, text='Гибкий поворот 20', variable=check_povorot_20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_povorot_20 = Entry(frame_2_3, width=width_of_entry)
enter_povorot_20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_povorot_25 = BooleanVar()
Checkbutton(frame_2_3, text='Гибкий поворот 25', variable=check_povorot_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_povorot_25 = Entry(frame_2_3, width=width_of_entry)
enter_povorot_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_povorot_32 = BooleanVar()
Checkbutton(frame_2_3, text='Гибкий поворот 32', variable=check_povorot_32).grid(row=temp_row, column=temp_col1, sticky=W)
enter_povorot_32 = Entry(frame_2_3, width=width_of_entry)
enter_povorot_32.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_povorot_40 = BooleanVar()
Checkbutton(frame_2_3, text='Гибкий поворот 40', variable=check_povorot_40).grid(row=temp_row, column=temp_col1, sticky=W)
enter_povorot_40 = Entry(frame_2_3, width=width_of_entry)
enter_povorot_40.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_2_4 = LabelFrame(tab2, text='ЛОТОК ПЕРФОРИРОВАННЫЙ', padx=5, pady=5, fg='red')
frame_2_4.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_lotok_perf_50_50_3000 = BooleanVar()
Checkbutton(frame_2_4, text='Лоток перфорированный 50х50х3000', variable=check_lotok_perf_50_50_3000).grid(row=temp_row, column=temp_col1, sticky=W)
enter_lotok_perf_50_50_3000 = Entry(frame_2_4, width=width_of_entry)
enter_lotok_perf_50_50_3000.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_lotok_perf_50_100_3000 = BooleanVar()
Checkbutton(frame_2_4, text='Лоток перфорированный 50х100х3000', variable=check_lotok_perf_50_100_3000).grid(row=temp_row, column=temp_col1, sticky=W)
enter_lotok_perf_50_100_3000 = Entry(frame_2_4, width=width_of_entry)
enter_lotok_perf_50_100_3000.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_lotok_perf_50_150_3000 = BooleanVar()
Checkbutton(frame_2_4, text='Лоток перфорированный 50х150х3000', variable=check_lotok_perf_50_150_3000).grid(row=temp_row, column=temp_col1, sticky=W)
enter_lotok_perf_50_150_3000 = Entry(frame_2_4, width=width_of_entry)
enter_lotok_perf_50_150_3000.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_lotok_perf_50_200_3000 = BooleanVar()
Checkbutton(frame_2_4, text='Лоток перфорированный 50х200х3000', variable=check_lotok_perf_50_200_3000).grid(row=temp_row, column=temp_col1, sticky=W)
enter_lotok_perf_50_200_3000 = Entry(frame_2_4, width=width_of_entry)
enter_lotok_perf_50_200_3000.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_1 = LabelFrame(tab3, text='TWT NEXT WALL', padx=5, pady=5, fg='red')
frame_3_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_wall_twt_next_6u_6_4 = BooleanVar()
Checkbutton(frame_3_1, text='6U 550x450', variable=check_wall_twt_next_6u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_6u_6_4 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_6u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_next_6u_6_6 = BooleanVar()
Checkbutton(frame_3_1, text='6U 550x600', variable=check_wall_twt_next_6u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_6u_6_6 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_6u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_next_9u_6_4 = BooleanVar()
Checkbutton(frame_3_1, text='9U 550x450', variable=check_wall_twt_next_9u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_9u_6_4 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_9u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_next_9u_6_6 = BooleanVar()
Checkbutton(frame_3_1, text='9U 550x600', variable=check_wall_twt_next_9u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_9u_6_6 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_9u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_next_12u_6_4 = BooleanVar()
Checkbutton(frame_3_1, text='12U 550x450', variable=check_wall_twt_next_12u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_12u_6_4 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_12u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_next_12u_6_6 = BooleanVar()
Checkbutton(frame_3_1, text='12U 550x600', variable=check_wall_twt_next_12u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_12u_6_6 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_12u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_next_15u_6_4 = BooleanVar()
Checkbutton(frame_3_1, text='15U 550x450', variable=check_wall_twt_next_15u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_15u_6_4 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_15u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_next_15u_6_6 = BooleanVar()
Checkbutton(frame_3_1, text='15U 550x600', variable=check_wall_twt_next_15u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_next_15u_6_6 = Entry(frame_3_1, width=width_of_entry)
enter_wall_twt_next_15u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_2 = LabelFrame(tab3, text='TWT PRO WALL', padx=5, pady=5, fg='red')
frame_3_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_wall_twt_pro_6u_6_4 = BooleanVar()
Checkbutton(frame_3_2, text='6U 600x450', variable=check_wall_twt_pro_6u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_6u_6_4 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_6u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_6u_6_6 = BooleanVar()
Checkbutton(frame_3_2, text='6U 600x600', variable=check_wall_twt_pro_6u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_6u_6_6 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_6u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_9u_6_4 = BooleanVar()
Checkbutton(frame_3_2, text='9U 600x450', variable=check_wall_twt_pro_9u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_9u_6_4 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_9u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_9u_6_6 = BooleanVar()
Checkbutton(frame_3_2, text='9U 600x600', variable=check_wall_twt_pro_9u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_9u_6_6 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_9u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_12u_6_4 = BooleanVar()
Checkbutton(frame_3_2, text='12U 600x450', variable=check_wall_twt_pro_12u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_12u_6_4 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_12u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_12u_6_6 = BooleanVar()
Checkbutton(frame_3_2, text='12U 600x600', variable=check_wall_twt_pro_12u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_12u_6_6 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_12u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_15u_6_4 = BooleanVar()
Checkbutton(frame_3_2, text='15U 600x450', variable=check_wall_twt_pro_15u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_15u_6_4 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_15u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_15u_6_6 = BooleanVar()
Checkbutton(frame_3_2, text='15U 600x600', variable=check_wall_twt_pro_15u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_15u_6_6 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_15u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_18u_6_4 = BooleanVar()
Checkbutton(frame_3_2, text='18U 600x450', variable=check_wall_twt_pro_18u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_18u_6_4 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_18u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_18u_6_6 = BooleanVar()
Checkbutton(frame_3_2, text='18U 600x600', variable=check_wall_twt_pro_18u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_18u_6_6 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_18u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_22u_6_4 = BooleanVar()
Checkbutton(frame_3_2, text='22U 600x450', variable=check_wall_twt_pro_22u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_22u_6_4 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_22u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_22u_6_6 = BooleanVar()
Checkbutton(frame_3_2, text='22U 600x600', variable=check_wall_twt_pro_22u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_22u_6_6 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_22u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_27u_6_4 = BooleanVar()
Checkbutton(frame_3_2, text='27U 600x450', variable=check_wall_twt_pro_27u_6_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_27u_6_4 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_27u_6_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_twt_pro_27u_6_6 = BooleanVar()
Checkbutton(frame_3_2, text='27U 600x600', variable=check_wall_twt_pro_27u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_twt_pro_27u_6_6 = Entry(frame_3_2, width=width_of_entry)
enter_wall_twt_pro_27u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_3 = LabelFrame(tab3, text='TWT PRO FLOOR', padx=5, pady=5, fg='red')
frame_3_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_floor_twt_pro_18u_6_6 = BooleanVar()
Checkbutton(frame_3_3, text='18U 600x600', variable=check_floor_twt_pro_18u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_18u_6_6 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_18u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_18u_6_8 = BooleanVar()
Checkbutton(frame_3_3, text='18U 600x800', variable=check_floor_twt_pro_18u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_18u_6_8 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_18u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_18u_6_10 = BooleanVar()
Checkbutton(frame_3_3, text='18U 600x1000', variable=check_floor_twt_pro_18u_6_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_18u_6_10 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_18u_6_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_22u_6_6 = BooleanVar()
Checkbutton(frame_3_3, text='22U 600x600', variable=check_floor_twt_pro_22u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_22u_6_6 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_22u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_22u_6_8 = BooleanVar()
Checkbutton(frame_3_3, text='22U 600x800', variable=check_floor_twt_pro_22u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_22u_6_8 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_22u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_22u_6_10 = BooleanVar()
Checkbutton(frame_3_3, text='22U 600x1000', variable=check_floor_twt_pro_22u_6_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_22u_6_10 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_22u_6_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_32u_6_6 = BooleanVar()
Checkbutton(frame_3_3, text='32U 600x600', variable=check_floor_twt_pro_32u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_32u_6_6 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_32u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_32u_6_10 = BooleanVar()
Checkbutton(frame_3_3, text='32U 600x1000', variable=check_floor_twt_pro_32u_6_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_32u_6_10 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_32u_6_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_37u_6_6 = BooleanVar()
Checkbutton(frame_3_3, text='37U 600x600', variable=check_floor_twt_pro_37u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_37u_6_6 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_37u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_37u_6_8 = BooleanVar()
Checkbutton(frame_3_3, text='37U 600x800', variable=check_floor_twt_pro_37u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_37u_6_8 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_37u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_37u_6_10 = BooleanVar()
Checkbutton(frame_3_3, text='37U 600x1000', variable=check_floor_twt_pro_37u_6_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_37u_6_10 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_37u_6_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_42u_6_8 = BooleanVar()
Checkbutton(frame_3_3, text='42U 600x800', variable=check_floor_twt_pro_42u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_42u_6_8 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_42u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_42u_6_10 = BooleanVar()
Checkbutton(frame_3_3, text='42U 600x1000', variable=check_floor_twt_pro_42u_6_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_42u_6_10 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_42u_6_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_42u_6_12 = BooleanVar()
Checkbutton(frame_3_3, text='42U 600x1200', variable=check_floor_twt_pro_42u_6_12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_42u_6_12 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_42u_6_12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_42u_8_8 = BooleanVar()
Checkbutton(frame_3_3, text='42U 800x800', variable=check_floor_twt_pro_42u_8_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_42u_8_8 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_42u_8_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_42u_8_10 = BooleanVar()
Checkbutton(frame_3_3, text='42U 800x1000', variable=check_floor_twt_pro_42u_8_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_42u_8_10 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_42u_8_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_42u_8_12 = BooleanVar()
Checkbutton(frame_3_3, text='42U 800x1200', variable=check_floor_twt_pro_42u_8_12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_42u_8_12 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_42u_8_12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_47u_6_6 = BooleanVar()
Checkbutton(frame_3_3, text='47U 600x600', variable=check_floor_twt_pro_47u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_47u_6_6 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_47u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_47u_6_8 = BooleanVar()
Checkbutton(frame_3_3, text='47U 600x800', variable=check_floor_twt_pro_47u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_47u_6_8 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_47u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_47u_6_12 = BooleanVar()
Checkbutton(frame_3_3, text='47U 600x1200', variable=check_floor_twt_pro_47u_6_12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_47u_6_12 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_47u_6_12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_47u_8_8 = BooleanVar()
Checkbutton(frame_3_3, text='47U 800x800', variable=check_floor_twt_pro_47u_8_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_47u_8_8 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_47u_8_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_twt_pro_47u_8_10 = BooleanVar()
Checkbutton(frame_3_3, text='47U 800x1000', variable=check_floor_twt_pro_47u_8_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_twt_pro_47u_8_10 = Entry(frame_3_3, width=width_of_entry)
enter_floor_twt_pro_47u_8_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_4 = LabelFrame(tab3, text='ЦМО WALL', padx=5, pady=5, fg='red')
frame_3_4.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_wall_cmo_6u_6_480 = BooleanVar()
Checkbutton(frame_3_4, text='6U 600x480', variable=check_wall_cmo_6u_6_480).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_6u_6_480 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_6u_6_480.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_cmo_6u_6_650 = BooleanVar()
Checkbutton(frame_3_4, text='6U 600x650', variable=check_wall_cmo_6u_6_650).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_6u_6_650 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_6u_6_650.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_cmo_9u_6_480 = BooleanVar()
Checkbutton(frame_3_4, text='9U 600x480', variable=check_wall_cmo_9u_6_480).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_9u_6_480 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_9u_6_480.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_cmo_9u_6_650 = BooleanVar()
Checkbutton(frame_3_4, text='9U 600x650', variable=check_wall_cmo_9u_6_650).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_9u_6_650 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_9u_6_650.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_cmo_12u_6_480 = BooleanVar()
Checkbutton(frame_3_4, text='12U 600x480', variable=check_wall_cmo_12u_6_480).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_12u_6_480 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_12u_6_480.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_cmo_12u_6_650 = BooleanVar()
Checkbutton(frame_3_4, text='12U 600x650', variable=check_wall_cmo_12u_6_650).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_12u_6_650 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_12u_6_650.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_cmo_15u_6_480 = BooleanVar()
Checkbutton(frame_3_4, text='15U 600x480', variable=check_wall_cmo_15u_6_480).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_15u_6_480 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_15u_6_480.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_wall_cmo_15u_6_650 = BooleanVar()
Checkbutton(frame_3_4, text='15U 600x650', variable=check_wall_cmo_15u_6_650).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wall_cmo_15u_6_650 = Entry(frame_3_4, width=width_of_entry)
enter_wall_cmo_15u_6_650.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_5 = LabelFrame(tab3, text='ЦМО FLOOR', padx=5, pady=5, fg='red')
frame_3_5.grid(row=0, column=4, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_floor_cmo_18u_6_6 = BooleanVar()
Checkbutton(frame_3_5, text='18U 600x600', variable=check_floor_cmo_18u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_18u_6_6 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_18u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_cmo_18u_6_8 = BooleanVar()
Checkbutton(frame_3_5, text='18U 600x800', variable=check_floor_cmo_18u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_18u_6_8 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_18u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_cmo_22u_6_6 = BooleanVar()
Checkbutton(frame_3_5, text='22U 600x600', variable=check_floor_cmo_22u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_22u_6_6 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_22u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_cmo_22u_6_8 = BooleanVar()
Checkbutton(frame_3_5, text='22U 600x800', variable=check_floor_cmo_22u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_22u_6_8 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_22u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_cmo_22u_6_10 = BooleanVar()
Checkbutton(frame_3_5, text='22U 600x1000', variable=check_floor_cmo_22u_6_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_22u_6_10 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_22u_6_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_cmo_27u_6_6 = BooleanVar()
Checkbutton(frame_3_5, text='27U 600x600', variable=check_floor_cmo_27u_6_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_27u_6_6 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_27u_6_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_cmo_27u_6_8 = BooleanVar()
Checkbutton(frame_3_5, text='27U 600x800', variable=check_floor_cmo_27u_6_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_27u_6_8 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_27u_6_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_floor_cmo_27u_6_10 = BooleanVar()
Checkbutton(frame_3_5, text='27U 600x1000', variable=check_floor_cmo_27u_6_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_floor_cmo_27u_6_10 = Entry(frame_3_5, width=width_of_entry)
enter_floor_cmo_27u_6_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_6 = LabelFrame(tab3, text='ЩИТЫ ЭЛЕКТРИЧЕСКИЕ IP31', padx=5, pady=5, fg='red')
frame_3_6.grid(row=0, column=5, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_smp_00_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-00 IP31 (270х210х140)', variable=check_smp_00_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_00_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_00_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_01_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-01 IP31 (410х210х140)', variable=check_smp_01_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_01_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_01_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_02_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-02 IP31 (250х300х140)', variable=check_smp_02_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_02_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_02_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_03_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-03 IP31 (350х300х155)', variable=check_smp_03_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_03_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_03_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_04_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-04 IP31 (400х300х155)', variable=check_smp_04_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_04_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_04_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_05_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-05 IP31 (400х400х155)', variable=check_smp_05_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_05_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_05_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_06_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-06 IP31 (500х400х170)', variable=check_smp_06_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_06_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_06_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_07_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-07 IP31 (700х500х210)', variable=check_smp_07_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_07_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_07_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_09_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-09 IP31 (600х400х210)', variable=check_smp_09_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_09_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_09_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_11_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-11 IP31 (600х400х400)', variable=check_smp_11_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_11_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_11_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_smp_12_ip_31 = BooleanVar()
Checkbutton(frame_3_6, text='ЩМП-12 IP31 (600х600х400)', variable=check_smp_12_ip_31).grid(row=temp_row, column=temp_col1, sticky=W)
enter_smp_12_ip_31 = Entry(frame_3_6, width=width_of_entry)
enter_smp_12_ip_31.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_7 = LabelFrame(tab3, text='ЩИТЫ ЭЛЕКТРИЧЕСКИЕ IP54', padx=5, pady=5, fg='red')
frame_3_7.grid(row=0, column=6, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_srnm_1_ip_54 = BooleanVar()
Checkbutton(frame_3_7, text='ЩРНМ-1 IP54 (400х300х220)', variable=check_srnm_1_ip_54).grid(row=temp_row, column=temp_col1, sticky=W)
enter_srnm_1_ip_54 = Entry(frame_3_7, width=width_of_entry)
enter_srnm_1_ip_54.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_srnm_2_ip_54 = BooleanVar()
Checkbutton(frame_3_7, text='ЩРНМ-2 IP54 (500х400х220)', variable=check_srnm_2_ip_54).grid(row=temp_row, column=temp_col1, sticky=W)
enter_srnm_2_ip_54 = Entry(frame_3_7, width=width_of_entry)
enter_srnm_2_ip_54.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_srnm_3_ip_54 = BooleanVar()
Checkbutton(frame_3_7, text='ЩРНМ-3 IP54 (650х500х220)', variable=check_srnm_3_ip_54).grid(row=temp_row, column=temp_col1, sticky=W)
enter_srnm_3_ip_54 = Entry(frame_3_7, width=width_of_entry)
enter_srnm_3_ip_54.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_srnm_4_ip_54 = BooleanVar()
Checkbutton(frame_3_7, text='ЩРНМ-4 IP54 (800х600х250)', variable=check_srnm_4_ip_54).grid(row=temp_row, column=temp_col1, sticky=W)
enter_srnm_4_ip_54 = Entry(frame_3_7, width=width_of_entry)
enter_srnm_4_ip_54.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_srnm_5_ip_54 = BooleanVar()
Checkbutton(frame_3_7, text='ЩРНМ-5 IP54 (1000х650х300)', variable=check_srnm_5_ip_54).grid(row=temp_row, column=temp_col1, sticky=W)
enter_srnm_5_ip_54 = Entry(frame_3_7, width=width_of_entry)
enter_srnm_5_ip_54.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_srnm_6_ip_54 = BooleanVar()
Checkbutton(frame_3_7, text='ЩРНМ-6 IP54 (1200х750х300)', variable=check_srnm_6_ip_54).grid(row=temp_row, column=temp_col1, sticky=W)
enter_srnm_6_ip_54 = Entry(frame_3_7, width=width_of_entry)
enter_srnm_6_ip_54.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_3_8 = LabelFrame(tab3, text='W&T WALL', padx=5, pady=5, fg='red')
frame_3_8.grid(row=0, column=7, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_wt_066045 = BooleanVar()
Checkbutton(frame_3_8, text='W&T 6U 600x450', variable=check_wt_066045).grid(row=temp_row, column=temp_col1, sticky=W)
enter_wt_066045 = Entry(frame_3_8, width=width_of_entry)
enter_wt_066045.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_4_1 = LabelFrame(tab4, text='HIKVISION IP БЕЗ РОЕ', padx=5, pady=5, fg='red')
frame_4_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hik7604niq1 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7604NI-Q1', variable=check_hik7604niq1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7604niq1 = Entry(frame_4_1, width=width_of_entry)
enter_hik7604niq1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7608niq2 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7608NI-Q2', variable=check_hik7608niq2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7608niq2 = Entry(frame_4_1, width=width_of_entry)
enter_hik7608niq2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7616niq2 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7616NI-Q2', variable=check_hik7616niq2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7616niq2 = Entry(frame_4_1, width=width_of_entry)
enter_hik7616niq2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7716niq4 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7716NI-Q4', variable=check_hik7716niq4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7716niq4 = Entry(frame_4_1, width=width_of_entry)
enter_hik7716niq4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7732niq4 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7732NI-Q4', variable=check_hik7732niq4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7732niq4 = Entry(frame_4_1, width=width_of_entry)
enter_hik7732niq4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7604nik1 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7604NI-K1', variable=check_hik7604nik1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7604nik1 = Entry(frame_4_1, width=width_of_entry)
enter_hik7604nik1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7608nik2 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7608NI-K2', variable=check_hik7608nik2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7608nik2 = Entry(frame_4_1, width=width_of_entry)
enter_hik7608nik2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7616nik2 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7616NI-K2', variable=check_hik7616nik2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7616nik2 = Entry(frame_4_1, width=width_of_entry)
enter_hik7616nik2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik_7732ni_k4 = BooleanVar()
Checkbutton(frame_4_1, text='DS-7732NI-K4', variable=check_hik_7732ni_k4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik_7732ni_k4 = Entry(frame_4_1, width=width_of_entry)
enter_hik_7732ni_k4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 

frame_4_2 = LabelFrame(tab4, text='HIKVISION IP C РОЕ', padx=5, pady=5, fg='red')
frame_4_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hik7604niq1_4p = BooleanVar()
Checkbutton(frame_4_2, text='DS-7604NI-Q1/4P', variable=check_hik7604niq1_4p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7604niq1_4p = Entry(frame_4_2, width=width_of_entry)
enter_hik7604niq1_4p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7608niq2_8p = BooleanVar()
Checkbutton(frame_4_2, text='DS-7608NI-Q2/8P', variable=check_hik7608niq2_8p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7608niq2_8p = Entry(frame_4_2, width=width_of_entry)
enter_hik7608niq2_8p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7616niq2_16p = BooleanVar()
Checkbutton(frame_4_2, text='DS-7616NI-Q2/16P', variable=check_hik7616niq2_16p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7616niq2_16p = Entry(frame_4_2, width=width_of_entry)
enter_hik7616niq2_16p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7604nik1_4p = BooleanVar()
Checkbutton(frame_4_2, text='DS-7604NI-K1/4P', variable=check_hik7604nik1_4p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7604nik1_4p = Entry(frame_4_2, width=width_of_entry)
enter_hik7604nik1_4p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7608nik2_8p = BooleanVar()
Checkbutton(frame_4_2, text='DS-7608NI-K2/8P', variable=check_hik7608nik2_8p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7608nik2_8p = Entry(frame_4_2, width=width_of_entry)
enter_hik7608nik2_8p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik7616nik2_16p = BooleanVar()
Checkbutton(frame_4_2, text='DS-7616NI-K2/16P', variable=check_hik7616nik2_16p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7616nik2_16p = Entry(frame_4_2, width=width_of_entry)
enter_hik7616nik2_16p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_4_3 = LabelFrame(tab4, text='HIKVISION HD/АНАЛОГОВЫЕ', padx=5, pady=5, fg='red')
frame_4_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hik7116hqhi_k1 = BooleanVar()
Checkbutton(frame_4_3, text='DS-7116HQHI-K1', variable=check_hik7116hqhi_k1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik7116hqhi_k1 = Entry(frame_4_3, width=width_of_entry)
enter_hik7116hqhi_k1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hikvision_ds_7216hqhi_k2_4audio = BooleanVar()
Checkbutton(frame_4_3, text='DS-7216HQHI-K2', variable=check_hikvision_ds_7216hqhi_k2_4audio).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hikvision_ds_7216hqhi_k2_4audio = Entry(frame_4_3, width=width_of_entry)
enter_hikvision_ds_7216hqhi_k2_4audio.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_4_4 = LabelFrame(tab4, text='HIWATCH IP', padx=5, pady=5, fg='red')
frame_4_4.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hiwatch_dsn204 = BooleanVar()
Checkbutton(frame_4_4, text='DS-N204', variable=check_hiwatch_dsn204).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsn204 = Entry(frame_4_4, width=width_of_entry)
enter_hiwatch_dsn204.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_hiwatch_dsn208 = BooleanVar()
Checkbutton(frame_4_4, text='DS-N208', variable=check_hiwatch_dsn208).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsn208 = Entry(frame_4_4, width=width_of_entry)
enter_hiwatch_dsn208.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_hiwatch_dsn204p = BooleanVar()
Checkbutton(frame_4_4, text='DS-N204P', variable=check_hiwatch_dsn204p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsn204p = Entry(frame_4_4, width=width_of_entry)
enter_hiwatch_dsn204p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_hiwatch_dsn208p = BooleanVar()
Checkbutton(frame_4_4, text='DS-N208P', variable=check_hiwatch_dsn208p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsn208p = Entry(frame_4_4, width=width_of_entry)
enter_hiwatch_dsn208p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_4_5 = LabelFrame(tab4, text='DAHUA', padx=5, pady=5, fg='red')
frame_4_5.grid(row=0, column=30, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_dhi_nvr4116hs_4216 = BooleanVar()
Checkbutton(frame_4_5, text='DHI-NVR4116HS-4KS2', variable=check_dhi_nvr4116hs_4216).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dhi_nvr4116hs_4216 = Entry(frame_4_5, width=width_of_entry)
enter_dhi_nvr4116hs_4216.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_5_1 = LabelFrame(tab5, text='IP-камеры HIKVISION', padx=5, pady=5, fg='red')
frame_5_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hik2cd1023g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1023G0-I', variable=check_hik2cd1023g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1023g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1023g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd1043g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1043G0-I', variable=check_hik2cd1043g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1043g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1043g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd1623g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1623G0-I', variable=check_hik2cd1623g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1623g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1623g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd1643g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1643G0-I', variable=check_hik2cd1643g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1643g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1643g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd1123g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1123G0-I', variable=check_hik2cd1123g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1123g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1123g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd1143g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1143G0-I', variable=check_hik2cd1143g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1143g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1143g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd2121g0_is = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD2121G0-IS', variable=check_hik2cd2121g0_is).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd2121g0_is = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd2121g0_is.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd1723g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1723G0-I', variable=check_hik2cd1723g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1723g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1723g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd1743g0 = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD1743G0-I', variable=check_hik2cd1743g0).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd1743g0 = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd1743g0.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd2420fi = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD2420F-I', variable=check_hik2cd2420fi).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd2420fi = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd2420fi.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd2643g0_izs = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD2643G1-IZS', variable=check_hik2cd2643g0_izs).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd2643g0_izs = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd2643g0_izs.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd2123g0_i = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD2123G0-I', variable=check_hik2cd2123g0_i).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd2123g0_i = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd2123g0_i.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd2123g0_iu = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD2123G0-IU', variable=check_hik2cd2123g0_iu).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd2123g0_iu = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd2123g0_iu.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2cd2721g0_is = BooleanVar()
Checkbutton(frame_5_1, text='DS-2CD2721G0-IS', variable=check_hik2cd2721g0_is).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2cd2721g0_is = Entry(frame_5_1, width=width_of_entry)
enter_hik2cd2721g0_is.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_5_2 = LabelFrame(tab5, text='HD-камеры HIKVISION', padx=5, pady=5, fg='red')
frame_5_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hik2ce76d3t_itmf = BooleanVar()
Checkbutton(frame_5_2, text='DS-2CE76D3T-ITMF', variable=check_hik2ce76d3t_itmf).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2ce76d3t_itmf = Entry(frame_5_2, width=width_of_entry)
enter_hik2ce76d3t_itmf.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hik2ce19d3t_it3zf = BooleanVar()
Checkbutton(frame_5_2, text='DS-2CE19D3T-IT3ZF', variable=check_hik2ce19d3t_it3zf).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hik2ce19d3t_it3zf = Entry(frame_5_2, width=width_of_entry)
enter_hik2ce19d3t_it3zf.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hikvision_ds_2ce16d3t_it3f = BooleanVar()
Checkbutton(frame_5_2, text='DS-2CE16D3T-IT3F', variable=check_hikvision_ds_2ce16d3t_it3f).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hikvision_ds_2ce16d3t_it3f = Entry(frame_5_2, width=width_of_entry)
enter_hikvision_ds_2ce16d3t_it3f.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_5_3 = LabelFrame(tab5, text='IP-камеры HIWATCH', padx=5, pady=5, fg='red')
frame_5_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hiwatch_dsi200 = BooleanVar()
Checkbutton(frame_5_3, text='DS-I200', variable=check_hiwatch_dsi200).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsi200 = Entry(frame_5_3, width=width_of_entry)
enter_hiwatch_dsi200.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hiwatch_dsi400 = BooleanVar()
Checkbutton(frame_5_3, text='DS-I400', variable=check_hiwatch_dsi400).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsi400 = Entry(frame_5_3, width=width_of_entry)
enter_hiwatch_dsi400.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hiwatch_dsi206 = BooleanVar()
Checkbutton(frame_5_3, text='DS-I206', variable=check_hiwatch_dsi206).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsi206 = Entry(frame_5_3, width=width_of_entry)
enter_hiwatch_dsi206.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hiwatch_dsi202 = BooleanVar()
Checkbutton(frame_5_3, text='DS-I202', variable=check_hiwatch_dsi202).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsi202 = Entry(frame_5_3, width=width_of_entry)
enter_hiwatch_dsi202.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hiwatch_dsi214 = BooleanVar()
Checkbutton(frame_5_3, text='DS-I214', variable=check_hiwatch_dsi214).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsi214 = Entry(frame_5_3, width=width_of_entry)
enter_hiwatch_dsi214.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hiwatch_dsi456 = BooleanVar()
Checkbutton(frame_5_3, text='DS-I456', variable=check_hiwatch_dsi456).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_dsi456 = Entry(frame_5_3, width=width_of_entry)
enter_hiwatch_dsi456.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_5_4 = LabelFrame(tab5, text='HD-камеры HIWATCH', padx=5, pady=5, fg='red')
frame_5_4.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hiwatch_ds_t203 = BooleanVar()
Checkbutton(frame_5_4, text='DS-T203', variable=check_hiwatch_ds_t203).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hiwatch_ds_t203 = Entry(frame_5_4, width=width_of_entry)
enter_hiwatch_ds_t203.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_5_5 = LabelFrame(tab5, text='DAHUA', padx=5, pady=5, fg='red')
frame_5_5.grid(row=0, column=4, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_ez_ipc_b1b40p_0360b = BooleanVar()
Checkbutton(frame_5_5, text='EZ-IPC-B1B40P-0360B', variable=check_ez_ipc_b1b40p_0360b).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ez_ipc_b1b40p_0360b = Entry(frame_5_5, width=width_of_entry)
enter_ez_ipc_b1b40p_0360b.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_6_1 = LabelFrame(tab6, text='ЖЕСТКИЕ ДИСКИ', padx=5, pady=5, fg='red')
frame_6_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_hdd_1 = BooleanVar()
Checkbutton(frame_6_1, text='HDD 1 TB', variable=check_hdd_1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_1 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hdd_2 = BooleanVar()
Checkbutton(frame_6_1, text='HDD 2 TB', variable=check_hdd_2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_2 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hdd_3 = BooleanVar()
'''Checkbutton(frame_6_1, text='HDD 3 TB', variable=check_hdd_3).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_3 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_3.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1'''
check_hdd_4 = BooleanVar()
Checkbutton(frame_6_1, text='HDD 4 TB', variable=check_hdd_4).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_4 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_4.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hdd_6 = BooleanVar()
Checkbutton(frame_6_1, text='HDD 6 TB', variable=check_hdd_6).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_6 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_6.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hdd_8 = BooleanVar()
Checkbutton(frame_6_1, text='HDD 8 TB', variable=check_hdd_8).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_8 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_8.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hdd_10 = BooleanVar()
Checkbutton(frame_6_1, text='HDD 10 TB', variable=check_hdd_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_10 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_hdd_12 = BooleanVar()
Checkbutton(frame_6_1, text='HDD 12 TB', variable=check_hdd_12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_hdd_12 = Entry(frame_6_1, width=width_of_entry)
enter_hdd_12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1


frame_6_2 = LabelFrame(tab6, text='КРОНШТЕЙНЫ HIKVISION', padx=5, pady=5, fg='red')
frame_6_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_DS_1260ZJ = BooleanVar()
Checkbutton(frame_6_2, text='DS-1260ZJ', variable=check_DS_1260ZJ).grid(row=temp_row, column=temp_col1, sticky=W)
enter_DS_1260ZJ = Entry(frame_6_2, width=width_of_entry)
enter_DS_1260ZJ.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_DS_1280ZJ_S = BooleanVar()
Checkbutton(frame_6_2, text='DS-1280ZJ-S', variable=check_DS_1280ZJ_S).grid(row=temp_row, column=temp_col1, sticky=W)
enter_DS_1280ZJ_S = Entry(frame_6_2, width=width_of_entry)
enter_DS_1280ZJ_S.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
Label(frame_6_2, text='Кронштейн для DS-2CD1123G0-I').grid(row=temp_row, column=temp_col1, sticky=W)
temp_row += 1
check_DS_1280ZJ_DM18 = BooleanVar()
Checkbutton(frame_6_2, text='DS-1280ZJ-DM18', variable=check_DS_1280ZJ_DM18).grid(row=temp_row, column=temp_col1, sticky=W)
enter_DS_1280ZJ_DM18 = Entry(frame_6_2, width=width_of_entry)
enter_DS_1280ZJ_DM18.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_6_3 = LabelFrame(tab6, text='КРОНШТЕЙНЫ DAHUA', padx=5, pady=5, fg='red')
frame_6_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_DH_PFA152_E = BooleanVar()
Checkbutton(frame_6_3, text='DH-PFA152-E', variable=check_DH_PFA152_E).grid(row=temp_row, column=temp_col1, sticky=W)
enter_DH_PFA152_E = Entry(frame_6_3, width=width_of_entry)
enter_DH_PFA152_E.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

check_DH_PFA134 = BooleanVar()
Checkbutton(frame_6_3, text='DH-PFA134', variable=check_DH_PFA134).grid(row=temp_row, column=temp_col1, sticky=W)
enter_DH_PFA134 = Entry(frame_6_3, width=width_of_entry)
enter_DH_PFA134.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_6_4 = LabelFrame(tab6, text='МОНИТОРЫ', padx=5, pady=5, fg='red')
frame_6_4.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_AOC_E2270SWN = BooleanVar()
Checkbutton(frame_6_4, text='AOC E2270SWN', variable=check_AOC_E2270SWN).grid(row=temp_row, column=temp_col1, sticky=W)
enter_AOC_E2270SWN = Entry(frame_6_4, width=width_of_entry)
enter_AOC_E2270SWN.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_6_5 = LabelFrame(tab6, text='ПРИЕМО-ПЕРЕДАТЧИК', padx=5, pady=5, fg='red')
frame_6_5.grid(row=0, column=4, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_DH_PFM800_E = BooleanVar()
Checkbutton(frame_6_5, text='DH-PFM800-E', variable=check_DH_PFM800_E).grid(row=temp_row, column=temp_col1, sticky=W)
enter_DH_PFM800_E = Entry(frame_6_5, width=width_of_entry)
enter_DH_PFM800_E.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_7_1 = LabelFrame(tab7, text='ББП', padx=5, pady=5, fg='red')
frame_7_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_bbp20_1 = BooleanVar()
Checkbutton(frame_7_1, text='ББП 20', variable=check_bbp20_1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_bbp20_1 = Entry(frame_7_1, width=width_of_entry)
enter_bbp20_1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_bbp40_1 = BooleanVar()
Checkbutton(frame_7_1, text='ББП 40', variable=check_bbp40_1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_bbp40_1 = Entry(frame_7_1, width=width_of_entry)
enter_bbp40_1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_bbp60_1 = BooleanVar()
Checkbutton(frame_7_1, text='ББП 60 ', variable=check_bbp60_1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_bbp60_1 = Entry(frame_7_1, width=width_of_entry)
enter_bbp60_1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_bbp60_2 = BooleanVar()
Checkbutton(frame_7_1, text='ББП 60 исп.2', variable=check_bbp60_2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_bbp60_2 = Entry(frame_7_1, width=width_of_entry)
enter_bbp60_2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_7_2 = LabelFrame(tab7, text='АККУМУЛЯТОРЫ', padx=5, pady=5, fg='red')
frame_7_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_akk7 = BooleanVar()
Checkbutton(frame_7_2, text='Аккумулятор 7 А/ч', variable=check_akk7).grid(row=temp_row, column=temp_col1, sticky=W)
enter_akk7 = Entry(frame_7_2, width=width_of_entry)
enter_akk7.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_akk18 = BooleanVar()
Checkbutton(frame_7_2, text='Аккумулятор 18 А/ч', variable=check_akk18).grid(row=temp_row, column=temp_col1, sticky=W)
enter_akk18 = Entry(frame_7_2, width=width_of_entry)
enter_akk18.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_7_3 = LabelFrame(tab7, text='БЛОКИ ПИТАНИЯ', padx=5, pady=5, fg='red')
frame_7_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_blok_pitania_1a = BooleanVar()
Checkbutton(frame_7_3, text='Блок питания 1А', variable=check_blok_pitania_1a).grid(row=temp_row, column=temp_col1, sticky=W)
enter_blok_pitania_1a = Entry(frame_7_3, width=width_of_entry)
enter_blok_pitania_1a.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_7_4 = LabelFrame(tab7, text='ИБП', padx=5, pady=5, fg='red')
frame_7_4.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_UT1500E = BooleanVar()
Checkbutton(frame_7_4, text='CyberPower UT1500E', variable=check_UT1500E).grid(row=temp_row, column=temp_col1, sticky=W)
enter_UT1500E = Entry(frame_7_4, width=width_of_entry)
enter_UT1500E.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_8_1 = LabelFrame(tab8, text='ЗАМКИ, ЗАЩЕЛКИ', padx=5, pady=5, fg='red')
frame_8_1.grid(row=0, column=10, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_ml194k_be = BooleanVar()
Checkbutton(frame_8_1, text='Замок ML-194K (Б/Э)', variable=check_ml194k_be).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ml194k_be = Entry(frame_8_1, width=width_of_entry)
enter_ml194k_be.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1 
check_jis_1711 = BooleanVar()
Checkbutton(frame_8_1, text='Защелка Jis 1711', variable=check_jis_1711).grid(row=temp_row, column=temp_col1, sticky=W)
enter_jis_1711 = Entry(frame_8_1, width=width_of_entry)
enter_jis_1711.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1 

frame_8_2 = LabelFrame(tab8, text='КНОПКИ', padx=5, pady=5, fg='red')
frame_8_2.grid(row=0, column=20, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_AT_H805A = BooleanVar()
Checkbutton(frame_8_2, text='Кнопка выхода AT-H805A', variable=check_AT_H805A).grid(row=temp_row, column=temp_col1, sticky=W)
enter_AT_H805A = Entry(frame_8_2, width=width_of_entry)
enter_AT_H805A.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1 
check_AA_UD808G2 = BooleanVar()
Checkbutton(frame_8_2, text='Устр-во разблокировки двери', variable=check_AA_UD808G2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_AA_UD808G2 = Entry(frame_8_2, width=width_of_entry)
enter_AA_UD808G2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_8_3 = LabelFrame(tab8, text='ПЛАНКИ', padx=5, pady=5, fg='red')
frame_8_3.grid(row=0, column=30, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_jis_904G = BooleanVar()
Checkbutton(frame_8_3, text='Планка Jis 904G', variable=check_jis_904G).grid(row=temp_row, column=temp_col1, sticky=W)
enter_jis_904G = Entry(frame_8_3, width=width_of_entry)
enter_jis_904G.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_8_4 = LabelFrame(tab8, text='КАРТЫ ДОСТУПА', padx=5, pady=5, fg='red')
frame_8_4.grid(row=0, column=40, sticky=NW)

check_SL_05_EM = BooleanVar()
Checkbutton(frame_8_4, text='Карта Clamshell SL-05 EM', variable=check_SL_05_EM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_SL_05_EM = Entry(frame_8_4, width=width_of_entry)
enter_SL_05_EM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_SL_05_MF = BooleanVar()
Checkbutton(frame_8_4, text='Карта Clamshell SL-05 MF', variable=check_SL_05_MF).grid(row=temp_row, column=temp_col1, sticky=W)
enter_SL_05_MF = Entry(frame_8_4, width=width_of_entry)
enter_SL_05_MF.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_SL_06_EM = BooleanVar()
Checkbutton(frame_8_4, text='Карта PVC SL-06 EM', variable=check_SL_06_EM).grid(row=temp_row, column=temp_col1, sticky=W)
enter_SL_06_EM = Entry(frame_8_4, width=width_of_entry)
enter_SL_06_EM.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_SL_06_MF = BooleanVar()
Checkbutton(frame_8_4, text='Карта PVC SL-06 MF', variable=check_SL_06_MF).grid(row=temp_row, column=temp_col1, sticky=W)
enter_SL_06_MF = Entry(frame_8_4, width=width_of_entry)
enter_SL_06_MF.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_SL_06_EM_MF = BooleanVar()
Checkbutton(frame_8_4, text='Карта PVC SL-06 EM+MF', variable=check_SL_06_EM_MF).grid(row=temp_row, column=temp_col1, sticky=W)
enter_SL_06_EM_MF = Entry(frame_8_4, width=width_of_entry)
enter_SL_06_EM_MF.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_SL_01_EM_BW = BooleanVar()
Checkbutton(frame_8_4, text='Брелок SL-01 EM BW', variable=check_SL_01_EM_BW).grid(row=temp_row, column=temp_col1, sticky=W)
enter_SL_01_EM_BW = Entry(frame_8_4, width=width_of_entry)
enter_SL_01_EM_BW.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_SL_03_MF = BooleanVar()
Checkbutton(frame_8_4, text='Брелок SL-03 MF', variable=check_SL_03_MF).grid(row=temp_row, column=temp_col1, sticky=W)
enter_SL_03_MF = Entry(frame_8_4, width=width_of_entry)
enter_SL_03_MF.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_8_5 = LabelFrame(tab8, text='КОНТРОЛЛЕРЫ', padx=5, pady=5, fg='red')
frame_8_5.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_sigur_e500u = BooleanVar()
Checkbutton(frame_8_5, text='Sigur E500U', variable=check_sigur_e500u).grid(row=temp_row, column=temp_col1, sticky=W)
enter_sigur_e500u = Entry(frame_8_5, width=width_of_entry)
enter_sigur_e500u.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_perco_ctl_042 = BooleanVar()
Checkbutton(frame_8_5, text='PERCo-CT/L04.2', variable=check_perco_ctl_042).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_ctl_042 = Entry(frame_8_5, width=width_of_entry)
enter_perco_ctl_042.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_perco_cr012 = BooleanVar()
Checkbutton(frame_8_5, text='PERCo-CR01.2', variable=check_perco_cr012).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_cr012 = Entry(frame_8_5, width=width_of_entry)
enter_perco_cr012.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_matrix_ii_net = BooleanVar()
Checkbutton(frame_8_5, text='Matrix-II Net', variable=check_matrix_ii_net).grid(row=temp_row, column=temp_col1, sticky=W)
enter_matrix_ii_net = Entry(frame_8_5, width=width_of_entry)
enter_matrix_ii_net.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_z397_web = BooleanVar()
Checkbutton(frame_8_5, text='Z-397 (мод. WEB)', variable=check_z397_web).grid(row=temp_row, column=temp_col1, sticky=W)
enter_z397_web = Entry(frame_8_5, width=width_of_entry)
enter_z397_web.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_8_6 = LabelFrame(tab8, text='СЧИТЫВАТЕЛИ', padx=5, pady=5, fg='red')
frame_8_6.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_matrix_ii = BooleanVar()
Checkbutton(frame_8_6, text='Matrix-II', variable=check_matrix_ii).grid(row=temp_row, column=temp_col1, sticky=W)
enter_matrix_ii = Entry(frame_8_6, width=width_of_entry)
enter_matrix_ii.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_perco_ir031b = BooleanVar()
Checkbutton(frame_8_6, text='PERCo-IR03.1B', variable=check_perco_ir031b).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_ir031b = Entry(frame_8_6, width=width_of_entry)
enter_perco_ir031b.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_ir031d = BooleanVar()
Checkbutton(frame_8_6, text='PERCo-IR03.1D', variable=check_perco_ir031d).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_ir031d = Entry(frame_8_6, width=width_of_entry)
enter_perco_ir031d.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_ir04 = BooleanVar()
Checkbutton(frame_8_6, text='PERCo-IR04', variable=check_perco_ir04).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_ir04 = Entry(frame_8_6, width=width_of_entry)
enter_perco_ir04.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_ir041 = BooleanVar()
Checkbutton(frame_8_6, text='PERCo-IR04.1', variable=check_perco_ir041).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_ir041 = Entry(frame_8_6, width=width_of_entry)
enter_perco_ir041.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_ir07 = BooleanVar()
Checkbutton(frame_8_6, text='PERCo-IR07', variable=check_perco_ir07).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_ir07 = Entry(frame_8_6, width=width_of_entry)
enter_perco_ir07.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_9_4 = LabelFrame(tab9, text='ПО PERCo', padx=5, pady=5, fg='red')
frame_9_4.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_perco_sl02 = BooleanVar()
Checkbutton(frame_9_4, text='SL02 "Локальное ПО с видеоидентификацией"', variable=check_perco_sl02).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sl02 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sl02.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm01 = BooleanVar()
Checkbutton(frame_9_4, text='SM01 "Администратор"', variable=check_perco_sm01).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm01 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm01.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm02 = BooleanVar()
Checkbutton(frame_9_4, text='SM02 "Персонал"', variable=check_perco_sm02).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm02 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm02.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm03 = BooleanVar()
Checkbutton(frame_9_4, text='SM03 "Бюро пропусков"', variable=check_perco_sm03).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm03 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm03.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm04 = BooleanVar()
Checkbutton(frame_9_4, text='SM04 "Управление доступом"', variable=check_perco_sm04).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm04 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm04.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm05 = BooleanVar()
Checkbutton(frame_9_4, text='SM05 "Дисциплинарные отчеты"', variable=check_perco_sm05).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm05 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm05.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm07 = BooleanVar()
Checkbutton(frame_9_4, text='SM07 "Учет рабочего времени"', variable=check_perco_sm07).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm07 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm07.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm08 = BooleanVar()
Checkbutton(frame_9_4, text='SM08 "Мониторинг"', variable=check_perco_sm08).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm08 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm08.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm09 = BooleanVar()
Checkbutton(frame_9_4, text='SM09 "Верификация"', variable=check_perco_sm09).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm09 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm09.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm10 = BooleanVar()
Checkbutton(frame_9_4, text='SM10 "Прием посетителей"', variable=check_perco_sm10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm10 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm12 = BooleanVar()
Checkbutton(frame_9_4, text='SM12 "Видеонаблюдение"', variable=check_perco_sm12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm12 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm13 = BooleanVar()
Checkbutton(frame_9_4, text='SM13 "Центральный пост"', variable=check_perco_sm13).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm13 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm13.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm14 = BooleanVar()
Checkbutton(frame_9_4, text='SM14 "Дизайнер пропусков"', variable=check_perco_sm14).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm14 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm14.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm15 = BooleanVar()
Checkbutton(frame_9_4, text='SM15 "Прозрачное здание"', variable=check_perco_sm15).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm15 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm15.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm16 = BooleanVar()
Checkbutton(frame_9_4, text='SM16 "Кафе"', variable=check_perco_sm16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm16 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm17 = BooleanVar()
Checkbutton(frame_9_4, text='SM17 "Автотранспортная проходная"', variable=check_perco_sm17).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm17 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm17.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm18 = BooleanVar()
Checkbutton(frame_9_4, text='SM18 "Интеграция с ИСО Орион"', variable=check_perco_sm18).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm18 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm18.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm19 = BooleanVar()
Checkbutton(frame_9_4, text='SM19 "Интеграция с 1С:Предприятие"', variable=check_perco_sm19).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm19 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm19.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sm20 = BooleanVar()
Checkbutton(frame_9_4, text='SM20 "Интеграция с видеоподсистемой "Trassir"', variable=check_perco_sm20).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sm20 = Entry(frame_9_4, width=width_of_entry)
enter_perco_sm20.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
Label(frame_9_4, text='Часть ПО скрыта программно', fg='red').grid(row=temp_row, column=temp_col1, sticky=W)

frame_9_5 = LabelFrame(tab9, text='ПО PERCo', padx=5, pady=5, fg='red')
#frame_9_5.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_perco_sn01 = BooleanVar()
Checkbutton(frame_9_5, text='SN01 "Базовое ПО"', variable=check_perco_sn01).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sn01 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sn01.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp09 = BooleanVar()
Checkbutton(frame_9_5, text='SP09 "Дисциплина и УРВ"', variable=check_perco_sp09).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp09 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp09.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp10 = BooleanVar()
Checkbutton(frame_9_5, text='SP10 "Контроль доступа и ОПС"', variable=check_perco_sp10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp10 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp11 = BooleanVar()
Checkbutton(frame_9_5, text='SP11 "Контроль доступа, ОПС и фотоидентификация"', variable=check_perco_sp11).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp11 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp11.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp12 = BooleanVar()
Checkbutton(frame_9_5, text='SP12 "Контроль доступа, ОПС и дисциплина"', variable=check_perco_sp12).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp12 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp12.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp13 = BooleanVar()
Checkbutton(frame_9_5, text='SP13 "Контроль доступа, ОПС, дисциплина и УРВ"', variable=check_perco_sp13).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp13 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp13.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp14 = BooleanVar()
Checkbutton(frame_9_5, text='SP14 "Усиленный контроль доступа с видеоидентификацией, ОПС, дисциплина"', variable=check_perco_sp14).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp14 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp14.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp15 = BooleanVar()
Checkbutton(frame_9_5, text='SP15 "Усиленный контроль доступа с видеоидентификацией, ОПС, дисциплина, УРВ"', variable=check_perco_sp15).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp15 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp15.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp16 = BooleanVar()
Checkbutton(frame_9_5, text='SP16 "Усиленный контроль доступа с видеоидентификацией, ОПС, видео, дисциплина, УРВ"', variable=check_perco_sp16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp16 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_perco_sp17 = BooleanVar()
Checkbutton(frame_9_5, text='SP17 "Усиленный контроль доступа с видеоидентификацией, ОПС, видео, дисциплина, центральный пост охраны"', variable=check_perco_sp17).grid(row=temp_row, column=temp_col1, sticky=W)
enter_perco_sp17 = Entry(frame_9_5, width=width_of_entry)
enter_perco_sp17.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1 
             
frame_9_6 = LabelFrame(tab9, text='GUARD SAAS КОМПЛЕКТ', padx=5, pady=5, fg='red')
frame_9_6.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_guard_saas_2_50 = BooleanVar()
Checkbutton(frame_9_6, text='Guard Saas-2/50 Web', variable=check_guard_saas_2_50).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_2_50 = Entry(frame_9_6, width=width_of_entry)
enter_guard_saas_2_50.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_2_100 = BooleanVar()
Checkbutton(frame_9_6, text='Guard Saas-2/100 Web', variable=check_guard_saas_2_100).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_2_100 = Entry(frame_9_6, width=width_of_entry)
enter_guard_saas_2_100.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_2_250 = BooleanVar()
Checkbutton(frame_9_6, text='Guard Saas-2/250 Web', variable=check_guard_saas_2_250).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_2_250 = Entry(frame_9_6, width=width_of_entry)
enter_guard_saas_2_250.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_5_100 = BooleanVar()
Checkbutton(frame_9_6, text='Guard Saas-5/100 Web', variable=check_guard_saas_5_100).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_5_100 = Entry(frame_9_6, width=width_of_entry)
enter_guard_saas_5_100.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_10_250 = BooleanVar()
Checkbutton(frame_9_6, text='Guard Saas-10/250 Web', variable=check_guard_saas_10_250).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_10_250 = Entry(frame_9_6, width=width_of_entry)
enter_guard_saas_10_250.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_9_7 = LabelFrame(tab9, text='GUARD SAAS ЛИЦЕНЗИЯ', padx=5, pady=5, fg='red')
frame_9_7.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_guard_saas_2_50_l = BooleanVar()
Checkbutton(frame_9_7, text='Guard Saas-2/50L', variable=check_guard_saas_2_50_l).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_2_50_l = Entry(frame_9_7, width=width_of_entry)
enter_guard_saas_2_50_l.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_2_100_l = BooleanVar()
Checkbutton(frame_9_7, text='Guard Saas-2/100L', variable=check_guard_saas_2_100_l).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_2_100_l = Entry(frame_9_7, width=width_of_entry)
enter_guard_saas_2_100_l.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_2_250_l = BooleanVar()
Checkbutton(frame_9_7, text='Guard Saas-2/250L', variable=check_guard_saas_2_250_l).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_2_250_l = Entry(frame_9_7, width=width_of_entry)
enter_guard_saas_2_250_l.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_5_100_l = BooleanVar()
Checkbutton(frame_9_7, text='Guard Saas-5/100L', variable=check_guard_saas_5_100_l).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_5_100_l = Entry(frame_9_7, width=width_of_entry)
enter_guard_saas_5_100_l.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_guard_saas_10_250_l = BooleanVar()
Checkbutton(frame_9_7, text='Guard Saas-10/250L', variable=check_guard_saas_10_250_l).grid(row=temp_row, column=temp_col1, sticky=W)
enter_guard_saas_10_250_l = Entry(frame_9_7, width=width_of_entry)
enter_guard_saas_10_250_l.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_11_1 = LabelFrame(tab11, text='D-LINK FAST ETHERNET', padx=5, pady=5, fg='red')
frame_11_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_des_1005c = BooleanVar()
Checkbutton(frame_11_1, text='DES-1005C', variable=check_des_1005c).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1005c = Entry(frame_11_1, width=width_of_entry)
enter_des_1005c.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1005d = BooleanVar()
Checkbutton(frame_11_1, text='DES-1005D', variable=check_des_1005d).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1005d = Entry(frame_11_1, width=width_of_entry)
enter_des_1005d.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1005p = BooleanVar()
Checkbutton(frame_11_1, text='DES-1005P', variable=check_des_1005p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1005p = Entry(frame_11_1, width=width_of_entry)
enter_des_1005p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1008c = BooleanVar()
Checkbutton(frame_11_1, text='DES-1008C', variable=check_des_1008c).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1008c = Entry(frame_11_1, width=width_of_entry)
enter_des_1008c.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1008d = BooleanVar()
Checkbutton(frame_11_1, text='DES-1008D', variable=check_des_1008d).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1008d = Entry(frame_11_1, width=width_of_entry)
enter_des_1008d.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1008p = BooleanVar()
Checkbutton(frame_11_1, text='DES-1008P', variable=check_des_1008p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1008p = Entry(frame_11_1, width=width_of_entry)
enter_des_1008p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1008pp = BooleanVar()
Checkbutton(frame_11_1, text='DES-1008P+', variable=check_des_1008pp).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1008pp = Entry(frame_11_1, width=width_of_entry)
enter_des_1008pp.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1016d = BooleanVar()
Checkbutton(frame_11_1, text='DES-1016D', variable=check_des_1016d).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1016d = Entry(frame_11_1, width=width_of_entry)
enter_des_1016d.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1018p = BooleanVar()
Checkbutton(frame_11_1, text='DES-1018P', variable=check_des_1018p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1018p = Entry(frame_11_1, width=width_of_entry)
enter_des_1018p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_des_1018mp = BooleanVar()
Checkbutton(frame_11_1, text='DES-1018MP', variable=check_des_1018mp).grid(row=temp_row, column=temp_col1, sticky=W)
enter_des_1018mp = Entry(frame_11_1, width=width_of_entry)
enter_des_1018mp.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_11_2 = LabelFrame(tab11, text='D-LINK GIGABIT ETHERNET', padx=5, pady=5, fg='red')
frame_11_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_dgs_1005a = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1005A', variable=check_dgs_1005a).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1005a = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1005a.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1005d = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1005D', variable=check_dgs_1005d).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1005d = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1005d.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1005p = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1005P', variable=check_dgs_1005p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1005p = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1005p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1008a = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1008A', variable=check_dgs_1008a).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1008a = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1008a.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1008d = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1008D', variable=check_dgs_1008d).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1008d = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1008d.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1008p = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1008P', variable=check_dgs_1008p).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1008p = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1008p.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1008mp = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1008MP', variable=check_dgs_1008mp).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1008mp = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1008mp.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1010mp = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1010MP', variable=check_dgs_1010mp).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1010mp = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1010mp.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1016c = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1016C', variable=check_dgs_1016c).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1016c = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1016c.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1024c = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1024C', variable=check_dgs_1024c).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1024c = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1024c.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1026mp = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1026MP', variable=check_dgs_1026mp).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1026mp = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1026mp.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1026x = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1026X', variable=check_dgs_1026x).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1026x = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1026x.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_dgs_1052x = BooleanVar()
Checkbutton(frame_11_2, text='DGS-1052X', variable=check_dgs_1052x).grid(row=temp_row, column=temp_col1, sticky=W)
enter_dgs_1052x = Entry(frame_11_2, width=width_of_entry)
enter_dgs_1052x.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_11_3 = LabelFrame(tab11, text='ТОЧКИ ДОСТУПА', padx=5, pady=5, fg='red')
frame_11_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_MikroTik_RBwAP2nD = BooleanVar()
Checkbutton(frame_11_3, text='MikroTik RBwAP2nD', variable=check_MikroTik_RBwAP2nD).grid(row=temp_row, column=temp_col1, sticky=W)
enter_MikroTik_RBwAP2nD = Entry(frame_11_3, width=width_of_entry)
enter_MikroTik_RBwAP2nD.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_MikroTik_RBcAP2nD = BooleanVar()
Checkbutton(frame_11_3, text='MikroTik RBcAP2nD', variable=check_MikroTik_RBcAP2nD).grid(row=temp_row, column=temp_col1, sticky=W)
enter_MikroTik_RBcAP2nD = Entry(frame_11_3, width=width_of_entry)
enter_MikroTik_RBcAP2nD.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_MikroTik_RBcAPGi_5acD2nD = BooleanVar()
Checkbutton(frame_11_3, text='MikroTik RBcAPGi-5acD2nD', variable=check_MikroTik_RBcAPGi_5acD2nD).grid(row=temp_row, column=temp_col1, sticky=W)
enter_MikroTik_RBcAPGi_5acD2nD = Entry(frame_11_3, width=width_of_entry)
enter_MikroTik_RBcAPGi_5acD2nD.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_MikroTik_SXT_2 = BooleanVar()
Checkbutton(frame_11_3, text='MikroTik SXT 2', variable=check_MikroTik_SXT_2).grid(row=temp_row, column=temp_col1, sticky=W)
enter_MikroTik_SXT_2 = Entry(frame_11_3, width=width_of_entry)
enter_MikroTik_SXT_2.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
Label(frame_11_3, text='Кронштейн для SXT 2', fg='blue').grid(row=temp_row, column=temp_col1, sticky=W)
temp_row += 1
check_MikroTik_QMP = BooleanVar()
Checkbutton(frame_11_3, text='MikroTik QMP', variable=check_MikroTik_QMP).grid(row=temp_row, column=temp_col1, sticky=W)
enter_MikroTik_QMP = Entry(frame_11_3, width=width_of_entry)
enter_MikroTik_QMP.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_11_4 = LabelFrame(tab11, text='МАРШРУТИЗАТОРЫ', padx=5, pady=5, fg='red')
frame_11_4.grid(row=0, column=3, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_MikroTik_RB951Ui_2HnD = BooleanVar()
Checkbutton(frame_11_4, text='MikroTik RB951Ui-2HnD', variable=check_MikroTik_RB951Ui_2HnD).grid(row=temp_row, column=temp_col1, sticky=W)
enter_MikroTik_RB951Ui_2HnD = Entry(frame_11_4, width=width_of_entry)
enter_MikroTik_RB951Ui_2HnD.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_11_5 = LabelFrame(tab11, text='Wi-Tek', padx=5, pady=5, fg='red')
frame_11_5.grid(row=0, column=5, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_WI_PS210G_O = BooleanVar()
Checkbutton(frame_11_5, text='WI-PS210G-O', variable=check_WI_PS210G_O).grid(row=temp_row, column=temp_col1, sticky=W)
enter_WI_PS210G_O = Entry(frame_11_5, width=width_of_entry)
enter_WI_PS210G_O.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_12_1 = LabelFrame(tab12, text='ВВГ', padx=5, pady=5, fg='red')
frame_12_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_vvg_ng_ls_2_15 = BooleanVar()
Checkbutton(frame_12_1, text='ВВГнг-LS 2х1,5', variable=check_vvg_ng_ls_2_15).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vvg_ng_ls_2_15 = Entry(frame_12_1, width=width_of_entry)
enter_vvg_ng_ls_2_15.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_vvg_ng_ls_2_25 = BooleanVar()
Checkbutton(frame_12_1, text='ВВГнг-LS 2х2,5', variable=check_vvg_ng_ls_2_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vvg_ng_ls_2_25 = Entry(frame_12_1, width=width_of_entry)
enter_vvg_ng_ls_2_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_vvg_ng_ls_3_15 = BooleanVar()
Checkbutton(frame_12_1, text='ВВГнг-LS 3х1,5', variable=check_vvg_ng_ls_3_15).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vvg_ng_ls_3_15 = Entry(frame_12_1, width=width_of_entry)
enter_vvg_ng_ls_3_15.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_vvg_ng_ls_3_25 = BooleanVar()
Checkbutton(frame_12_1, text='ВВГнг-LS 3х2,5', variable=check_vvg_ng_ls_3_25).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vvg_ng_ls_3_25 = Entry(frame_12_1, width=width_of_entry)
enter_vvg_ng_ls_3_25.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_vvg_ng_ls_3_40 = BooleanVar()
Checkbutton(frame_12_1, text='ВВГнг-LS 3х4', variable=check_vvg_ng_ls_3_40).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vvg_ng_ls_3_40 = Entry(frame_12_1, width=width_of_entry)
enter_vvg_ng_ls_3_40.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_vvg_ng_ls_3_60 = BooleanVar()
Checkbutton(frame_12_1, text='ВВГнг-LS 3х6', variable=check_vvg_ng_ls_3_60).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vvg_ng_ls_3_60 = Entry(frame_12_1, width=width_of_entry)
enter_vvg_ng_ls_3_60.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_vvg_ng_ls_5_60 = BooleanVar()
Checkbutton(frame_12_1, text='ВВГнг-LS 5х6', variable=check_vvg_ng_ls_5_60).grid(row=temp_row, column=temp_col1, sticky=W)
enter_vvg_ng_ls_5_60 = Entry(frame_12_1, width=width_of_entry)
enter_vvg_ng_ls_5_60.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_12_2 = LabelFrame(tab12, text='ШВВП', padx=5, pady=5, fg='red')
frame_12_2.grid(row=0, column=10, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_svvp_2_05 = BooleanVar()
Checkbutton(frame_12_2, text='ШВВП 2х0,5', variable=check_svvp_2_05).grid(row=temp_row, column=temp_col1, sticky=W)
enter_svvp_2_05 = Entry(frame_12_2, width=width_of_entry)
enter_svvp_2_05.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1                 
check_svvp_2_075 = BooleanVar()
Checkbutton(frame_12_2, text='ШВВП 2х0,75', variable=check_svvp_2_075).grid(row=temp_row, column=temp_col1, sticky=W)
enter_svvp_2_075 = Entry(frame_12_2, width=width_of_entry)
enter_svvp_2_075.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_12_3 = LabelFrame(tab12, text='АВВГ', padx=5, pady=5, fg='red')
frame_12_3.grid(row=0, column=11, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_avvg_2_10 = BooleanVar()
Checkbutton(frame_12_3, text='АВВГ 2х10', variable=check_avvg_2_10).grid(row=temp_row, column=temp_col1, sticky=W)
enter_avvg_2_10 = Entry(frame_12_3, width=width_of_entry)
enter_avvg_2_10.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_avvg_2_16 = BooleanVar()
Checkbutton(frame_12_3, text='АВВГ 2х16', variable=check_avvg_2_16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_avvg_2_16 = Entry(frame_12_3, width=width_of_entry)
enter_avvg_2_16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_12_4 = LabelFrame(tab12, text='ПВС', padx=5, pady=5, fg='red')
frame_12_4.grid(row=0, column=12, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_pvs_2_15 = BooleanVar()
Checkbutton(frame_12_4, text='ПВС 2х1.5', variable=check_pvs_2_15).grid(row=temp_row, column=temp_col1, sticky=W)
enter_pvs_2_15 = Entry(frame_12_4, width=width_of_entry)
enter_pvs_2_15.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_13_1 = LabelFrame(tab13, text='МИКРОФОНЫ ДЛЯ ВИДЕО', padx=5, pady=5, fg='red')
frame_13_1.grid(row=0, column=10, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_stelberry_m70hd = BooleanVar()
Checkbutton(frame_13_1, text='STELBERRY M-70HD', variable=check_stelberry_m70hd).grid(row=temp_row, column=temp_col1, sticky=W)
enter_stelberry_m70hd = Entry(frame_13_1, width=width_of_entry)
enter_stelberry_m70hd.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_stelberry_m80hd = BooleanVar()
Checkbutton(frame_13_1, text='STELBERRY M-80HD', variable=check_stelberry_m80hd).grid(row=temp_row, column=temp_col1, sticky=W)
enter_stelberry_m80hd = Entry(frame_13_1, width=width_of_entry)
enter_stelberry_m80hd.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_stelberry_m90hd = BooleanVar()
Checkbutton(frame_13_1, text='STELBERRY M-90HD', variable=check_stelberry_m90hd).grid(row=temp_row, column=temp_col1, sticky=W)
enter_stelberry_m90hd = Entry(frame_13_1, width=width_of_entry)
enter_stelberry_m90hd.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
Label(frame_13_1, text='РоЕ-сплиттер для микрофона').grid(row=temp_row, column=temp_col1, sticky=W)
temp_row += 1
check_stelberry_mx225 = BooleanVar()
Checkbutton(frame_13_1, text='STELBERRY MX-225', variable=check_stelberry_mx225).grid(row=temp_row, column=temp_col1, sticky=W)
enter_stelberry_mx225 = Entry(frame_13_1, width=width_of_entry)
enter_stelberry_mx225.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_13_2 = LabelFrame(tab13, text='УСИЛИТЕЛИ', padx=5, pady=5, fg='red')
frame_13_2.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_ROXTON_AA_60M = BooleanVar()
Checkbutton(frame_13_2, text='ROXTON AA-60M', variable=check_ROXTON_AA_60M).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ROXTON_AA_60M = Entry(frame_13_2, width=width_of_entry)
enter_ROXTON_AA_60M.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_13_3 = LabelFrame(tab13, text='ГРОМКОГОВОРИТЕЛИ', padx=5, pady=5, fg='red')
frame_13_3.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_ROXTON_PA_620T = BooleanVar()
Checkbutton(frame_13_3, text='ROXTON PA-620T', variable=check_ROXTON_PA_620T).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ROXTON_PA_620T = Entry(frame_13_3, width=width_of_entry)
enter_ROXTON_PA_620T.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_13_4 = LabelFrame(tab13, text='МИКРОФОНЫ', padx=5, pady=5, fg='red')
frame_13_4.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_ROXTON_RM_03 = BooleanVar()
Checkbutton(frame_13_4, text='ROXTON RM-03', variable=check_ROXTON_RM_03).grid(row=temp_row, column=temp_col1, sticky=W)
enter_ROXTON_RM_03 = Entry(frame_13_4, width=width_of_entry)
enter_ROXTON_RM_03.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_14_1 = LabelFrame(tab14, text='ВЫЗЫВНЫЕ ПАНЕЛИ', padx=5, pady=5, fg='red')
frame_14_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_HIKVISION_DS_KV6113_PE1 = BooleanVar()
Checkbutton(frame_14_1, text='HIKVISION DS-KV6113-PE1', variable=check_HIKVISION_DS_KV6113_PE1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_HIKVISION_DS_KV6113_PE1 = Entry(frame_14_1, width=width_of_entry)
enter_HIKVISION_DS_KV6113_PE1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1
check_Fanvil_i16 = BooleanVar()
Checkbutton(frame_14_1, text='Fanvil i16', variable=check_Fanvil_i16).grid(row=temp_row, column=temp_col1, sticky=W)
enter_Fanvil_i16 = Entry(frame_14_1, width=width_of_entry)
enter_Fanvil_i16.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1


frame_14_2 = LabelFrame(tab14, text='МОНИТОРЫ ДОМОФОНА', padx=5, pady=5, fg='red')
frame_14_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_HIKVISION_DS_KH6320_TE1 = BooleanVar()
Checkbutton(frame_14_2, text='HIKVISION DS-KH6320-TE1', variable=check_HIKVISION_DS_KH6320_TE1).grid(row=temp_row, column=temp_col1, sticky=W)
enter_HIKVISION_DS_KH6320_TE1 = Entry(frame_14_2, width=width_of_entry)
enter_HIKVISION_DS_KH6320_TE1.grid(row=temp_row, column=temp_col2, sticky=W)
cnt += 1
temp_row += 1

frame_100_1 = LabelFrame(tab100, text='РАБОТЫ', padx=5, pady=5, fg='red')
frame_100_1.grid(row=0, column=0, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_work1 = BooleanVar() 
Checkbutton(frame_100_1, text='Скрытая прокладка кабеля', variable=check_work1).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work1 = Entry(frame_100_1, width=width_of_entry) 
enter_work1.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work2 = BooleanVar() 
Checkbutton(frame_100_1, text='Открытая прокладка кабеля', variable=check_work2).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work2 = Entry(frame_100_1, width=width_of_entry) 
enter_work2.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work3 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка кабель-канала шириной менее 60мм', variable=check_work3).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work3 = Entry(frame_100_1, width=width_of_entry) 
enter_work3.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work4 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка кабель-канала шириной более 60мм', variable=check_work4).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work4 = Entry(frame_100_1, width=width_of_entry) 
enter_work4.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work5 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка аксессуаров для кабель-каналов', variable=check_work5).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work5 = Entry(frame_100_1, width=width_of_entry) 
enter_work5.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work6 = BooleanVar() 
Checkbutton(frame_100_1, text='Открытие/закрытие установленного кабель-канала', variable=check_work6).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work6 = Entry(frame_100_1, width=width_of_entry) 
enter_work6.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work7 = BooleanVar() 
Checkbutton(frame_100_1, text='Снятие установленного кабель-канала', variable=check_work7).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work7 = Entry(frame_100_1, width=width_of_entry) 
enter_work7.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work8 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка трубы гофрированной', variable=check_work8).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work8 = Entry(frame_100_1, width=width_of_entry) 
enter_work8.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work9 = BooleanVar() 
Checkbutton(frame_100_1, text='Сверление отверстия', variable=check_work9).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work9 = Entry(frame_100_1, width=width_of_entry) 
enter_work9.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work10 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка подрозетника в стену', variable=check_work10).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work10 = Entry(frame_100_1, width=width_of_entry) 
enter_work10.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work11 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка стяжек на потолки и стены из твердых материалов', variable=check_work11).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work11 = Entry(frame_100_1, width=width_of_entry) 
enter_work11.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work12 = BooleanVar() 
Checkbutton(frame_100_1, text='Сборка и установка шкафа телекоммуникационного напольного', variable=check_work12).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work12 = Entry(frame_100_1, width=width_of_entry) 
enter_work12.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work13 = BooleanVar() 
Checkbutton(frame_100_1, text='Сборка и установка шкафа телекоммуникационного настенного', variable=check_work13).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work13 = Entry(frame_100_1, width=width_of_entry) 
enter_work13.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work14 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка оборудования в шкаф', variable=check_work14).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work14 = Entry(frame_100_1, width=width_of_entry) 
enter_work14.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work15 = BooleanVar() 
Checkbutton(frame_100_1, text='Установка оборудования на стену', variable=check_work15).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work15 = Entry(frame_100_1, width=width_of_entry) 
enter_work15.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work16 = BooleanVar() 
Checkbutton(frame_100_1, text='Расключение розетки', variable=check_work16).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work16 = Entry(frame_100_1, width=width_of_entry) 
enter_work16.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work17 = BooleanVar() 
Checkbutton(frame_100_1, text='Обжим коннектора', variable=check_work17).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work17 = Entry(frame_100_1, width=width_of_entry) 
enter_work17.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work18 = BooleanVar() 
Checkbutton(frame_100_1, text='Кроссирование патч-панели', variable=check_work18).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work18 = Entry(frame_100_1, width=width_of_entry) 
enter_work18.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work19 = BooleanVar() 
Checkbutton(frame_100_1, text='Кроссирование плинтов KRONE, рапределительной коробки', variable=check_work19).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work19 = Entry(frame_100_1, width=width_of_entry) 
enter_work19.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work20 = BooleanVar() 
Checkbutton(frame_100_1, text='Тестирование и маркировка порта линк-тестером', variable=check_work20).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work20 = Entry(frame_100_1, width=width_of_entry) 
enter_work20.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1

frame_100_2 = LabelFrame(tab100, text='РАБОТЫ', padx=5, pady=5, fg='red')
frame_100_2.grid(row=0, column=1, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

check_work21 = BooleanVar() 
Checkbutton(frame_100_2, text='Прокладка ВОК для внутр. прокладки', variable=check_work21).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work21 = Entry(frame_100_2, width=width_of_entry) 
enter_work21.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work22 = BooleanVar() 
Checkbutton(frame_100_2, text='Прокладка бронированного ВОК', variable=check_work22).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work22 = Entry(frame_100_2, width=width_of_entry) 
enter_work22.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work23 = BooleanVar() 
Checkbutton(frame_100_2, text='Оконцевание ВОК', variable=check_work23).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work23 = Entry(frame_100_2, width=width_of_entry) 
enter_work23.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work24 = BooleanVar() 
Checkbutton(frame_100_2, text='Тестирование волоконно-оптического кабеля', variable=check_work24).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work24 = Entry(frame_100_2, width=width_of_entry) 
enter_work24.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work25 = BooleanVar() 
Checkbutton(frame_100_2, text='Сборка-разборка фальшпотолков или полов', variable=check_work25).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work25 = Entry(frame_100_2, width=width_of_entry) 
enter_work25.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work26 = BooleanVar() 
Checkbutton(frame_100_2, text='Прочие дополнительные сетевые работы', variable=check_work26).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work26 = Entry(frame_100_2, width=width_of_entry) 
enter_work26.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1
check_work27 = BooleanVar() 
Checkbutton(frame_100_2, text='Транспортные расходы', variable=check_work27).grid(row=temp_row, column=temp_col1, sticky=W) 
enter_work27 = Entry(frame_100_2, width=width_of_entry) 
enter_work27.grid(row=temp_row, column=temp_col2, sticky=W) 
temp_row += 1

frame_100_3 = LabelFrame(tab100, text='ОПИСАНИЕ РАБОТ', padx=5, pady=5, fg='red')
frame_100_3.grid(row=0, column=2, sticky=NW)

temp_row = 0
temp_col1 = 0
temp_col2 = 1

temp_row += 1
text_1 = BooleanVar()
Checkbutton(frame_100_3, text='Прокладка кабеля', variable=text_1).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_2 = BooleanVar() 
Checkbutton(frame_100_3, text='Установка кабель-канала', variable=text_2).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_3 = BooleanVar() 
Checkbutton(frame_100_3, text='Установка трубы гофрированной', variable=text_3).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_14 = BooleanVar() 
Checkbutton(frame_100_3, text='Монтаж сетевых розеток', variable=text_14).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_4 = BooleanVar() 
Checkbutton(frame_100_3, text='Сборка и установка шкафа телекоммуникационного', variable=text_4).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_6 = BooleanVar() 
Checkbutton(frame_100_3, text='Кроссирование патч-панелей', variable=text_6).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_7 = BooleanVar() 
Checkbutton(frame_100_3, text='Прокладка ВОК', variable=text_7).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_8 = BooleanVar() 
Checkbutton(frame_100_3, text='Сварка ВОК', variable=text_8).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_9 = BooleanVar() 
Checkbutton(frame_100_3, text='Установка сетевого оборудования', variable=text_9).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_13 = BooleanVar() 
Checkbutton(frame_100_3, text='Установка видеокамер', variable=text_13).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_10 = BooleanVar()
Checkbutton(frame_100_3, text='Пуско-наладочные работы', variable=text_10).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_11 = BooleanVar()
Checkbutton(frame_100_3, text='Транспортные расходы', variable=text_11).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1
text_12 = BooleanVar()
Checkbutton(frame_100_3, text='Прочие дополнительные сетевые работы', variable=text_12).grid(row=temp_row, column=temp_col1, sticky=W) 
temp_row += 1


# add information about number of positions
main_menu.add_cascade(label = 'There are ' + str(cnt) + ' positions in program')

# launch program window
root.mainloop()