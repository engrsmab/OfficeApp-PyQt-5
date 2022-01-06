
root_width = "900"
root_height = "650"

font = ("Times 16")
bold_font = ("Times 14 bold")
big_font = ("Times 20")
small_font = ("Times 12")
hug_font = ("Times 35")
hug_bold_font = ("Times 40 bold")

bg_color = "#383d3a"
fg_color = "#1c211e"
light_fg = "white"
hover_color = "#9da1a6"
path = "/Users/macbookpro/Desktop/Projects/Application_Development/OfficeApp/Files/Img/"
Images = [path+"Official Logo [Azeem Ent.].jpg",path+"RegButton.png",path+"home-32.png",path+"gear-2-32.png",path+"bill-32.png",path+"us-dollar-32.png",
          path+"group-32.png",path+"account-logout-32.png",path+"exit.png",path+"logo.png",path+"edit-user-24.png",path+"key-3-24.png",path+"logo_resized.png",path+"login_bg.png",path+"tick.png",path+"orange-bg.png",path+"green-bg.png",path+"dashboard-bg.png",path+"green-tick.png",path+"cancel.png"]
Image_Titles = ["Select Office Logo","Select Register Button Icon","Select Home Icon","Select Settings Icon","Select Bill Icon","Select Payment Icon",
"Select Members Icon","Select Logout Icon","Select Exit Icon","Select Login Window Logo","Select Login Icon","Select Password Icon","Select success tick image","Select Green Background","Select Orange Background","Select Resized Logo Image","Select Green Tick icon","Select red cancel icon"]
doc_path = "/Users/macbookpro/Desktop/Projects/Application_Development/OfficeApp/Files/Tampletes/"
docs = [doc_path+'Demand_Sample.docx']
font_path = "/Users/macbookpro/Desktop/Projects/Application_Development/OfficeApp/Files/fonts/"
fonts_file = [font_path+"Rockwell-Font/ROCK.TTF",font_path+"Rockwell-Font/rockb.ttf"]

import socket
pc_name = str(socket.gethostname())
pc_name = pc_name.split("-")
mac = False
if pc_name[0] == "MacBook" or pc_name[0] == "Macbook" or pc_name[0] == "Macbooks" or pc_name == "Macbooks":
    from tkmacosx import Button
    if type(pc_name) != str:
        pc_name = pc_name[0]
       


firms_setting = {
    'Azeem Enterprises:':
        {'y':[240,230,210,180,40],
        'heading_size':14,
        'border_bg':'black',
        'border_text':'white',
        'font':'Times-Roman',
        'font_bold':'Times-Bold',
        'page_size':"A4"},
        
    'Muazzam Enterprises':
        {'y':[230,220,210,170,20],
        'heading_size':14,
        'border_bg':'white',
        'border_text':'black',
        'font':'Courier',
        'font_bold':'Courier-Bold',
        'page_size':"A4"},
        
    'Masood Traders':
        {'y':[230,220,210,170,40],
        'heading_size':11,
        'border_bg':'white',
        'border_text':'black',
        'font':'Helvetica',
        'font_bold':'Helvetic-Bold',
        'page_size':"A4"},
        
    'Hadi Enterprises':
        {'y':[230,220,210,170,20],
        'heading_size':11,
        'border_bg':'black',
        'border_text':'white',
        'font':'Calibri',
        'font_bold':'Calibri-Bold',
        'page_size':"A4"},
        
    'Zahid Enterprises':
        {'y':[230,220,210,170,20],
        'heading_size':16,
        'border_bg':'white',
        'border_text':'black',
        'font':'Garamond',
        'font_bold':'Garamond-Bold',
        'page_size':"A4"},
        
    'Al Jannat Enterprises':
        {'y':[230,220,210,170,20],
        'heading_size':16,
        'border_bg':'white',
        'border_text':'black',
        'font':'Rockwell',
        'font_bold':'Rockwell-Bold',
        'page_size':"A4"},

    'Other':
        {'y':[230,220,210,170,20],
        'heading_size':16,
        'border_bg':'white',
        'border_text':'black',
        'font':'Rockwell',
        'font_bold':'Rockwell-Bold',
        'page_size':"A4"}}

