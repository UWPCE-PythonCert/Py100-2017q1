#   $Id: ch_proj01.py,v 1.9 2017/03/09 01:58:12 larry Exp $

# IMPORTS
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import six
import sys
import pytest
import doctest
import csv
from buzhug import Base

# Function to create database
def create_db():
    """
    Open csv file, cleanup data
    """

    # Keep GUI very simple
    Tk().withdraw()

    # Get csv filename
    try:
        fn = askopenfilename(filetypes=[("csv files","*.csv")])
        if not fn:
            sys.exit()
    except:
        sys.exit()

    lst1 = []
    lst2  =[]

    # Open csv file, convert to list
    try:
        csv_file = open(fn, "r")
        myfile = csv.reader(csv_file)
        for x in myfile:
            lst1.append(x)
    except:
        print("Could not open csv file.")
    finally:
        csv_file.close()

    # Clean up data, back & forth between 2 lists
    # Remove first line
    lst1 = lst1[1:]

    # Upper case all data
    for x in lst1:
        lst2.append(map (lambda var: var.upper(), x))

    lst1 = []
    # Remove the last 6 elements of the list
    for x in lst2:
        lst1.append(x[:-6])

    # Remove ODD/EVEN from list
    for x in lst1:
        del x[9]

    # Remove the five couplers & all blanks
    csv_data = []
    for x in lst1:
        if x[1]:
            csv_data.append(x[:-7] + x[17:])

    # Create database if not existing
    # Folder name is CH_FILE, object name is ch_dat
    ch_dat = Base('CH_FILE')
    # "open" MODE WILL NOT OVERWRITE, "override" MODE WILL

    # Creates an empty database
    ch_dat.create(('SITE_NAME',str),
                  ('JT_NUM',str),
                  ('PHASE',str),
                  ('HUB',str),
                  ('PRETERM',str),
                  ('PORT',str),
                  ('SHEATH',str),
                  ('TOWER_TX',str),
                  ('HUB_TX',str),
                  ('HUB_MUX_NUM',str),
                  ('HUB_MUX_TYPE',str),
                  ('TWR_GROUP',str),
                  ('FIELD_MUX_NAME',str),
                  ('FIELD_MUX_TYPE',str),mode='override')

    # # Insert into database
    for var in csv_data:
        ch_dat.insert(var[0],var[1],var[2],var[3],var[4],
                      var[5],var[6],var[7],var[8],var[9],
                      var[10],var[11],var[12],var[13])

class ChannelTool(Frame):
    '''
    Class for basic data input and output
    '''

    def __init__(self, parent):
        '''
        Ininializes basic GUI
        Calls basic methods
        '''

        # List of Washington State HUBs
        self.hubs = ["ABERDEEN","ANACORTES","AVONDALE","BELLEVUE","BELLINGHAM",
                     "BEVERLY LANE","BONNEY LAKE","BREMERTON","BURIEN",
                     "BURLINGTON","CEDAR DOWNS","CENTRALIA","CLEARVIEW","DEMING",
                     "ELMA","ENUMCLAW","EVERETT","FEDERAL WAY","FERNDALE",
                     "FORT LEWIS","FREELAND","GIG HARBOR","GRAHAM","GREEN LAKE",
                     "ISSAQUAH","KENT VISTA","KIRKLAND","LAKE CITY EAST",
                     "LAKE CITY WEST","LAKE STEVENS","LAKEWOOD","LYNDEN",
                     "LYNNWOOD","MADISON PARK","MARYSVILLE","MONROE",
                     "NORTH BEND","NORTH EVERETT","OAK HARBOR","OB2 EAST DATA",
                     "OLYMPIA","TUMWATER","OTN A","OTN B","OTN C","OTN D",
                     "OTN E","OTN F","PARKLAND","PINE LAKE","POULSBO","PUYALLUP",
                     "QUEEN ANNE","RAYMOND","REDMOND","ROOSEVELT","SEA TAC",
                     "SHELTON","SILVER LAKE","SNOHOMISH","SOUTH SEATTLE",
                     "SPOKANE","SPOKANE EAST","SPOKANE WEST","TACOMA",
                     "TACOMA EAST","UNIVERSITY EAST","UNIVERSITY WEST","VASHON",
                     "WESTIN","WESTPORT","WOODINVILLE"]

        # GUI
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.make_widgets()

    def initUI(self):
        self.parent.title('Channel tool')
        self.pack(fill=BOTH, expand=1)

    def make_widgets(self):
        '''
        Creates all basic frames and widgets
        '''

        # String variables
        # Site Name
        self.sitename_var =     StringVar()
        # JT Number
        self.jt_var =           StringVar()
        # Preterm
        self.preterm_var =      StringVar()
        # Port
        self.port_var =         StringVar()
        # HUB MUX number
        self.hubmuxnum_var =    StringVar()
        # HUB MUX Type
        self.hubmuxtype_var =   StringVar()
        # Field MUX Name
        self.fieldmuxname_var = StringVar()
        # Field MUX Type
        self.fieldmuxtype_var = StringVar()
        # Tower Group
        self.towergroup_var =   StringVar()
        # HUB TX
        self.hubtx_var =        StringVar()
        # Tower TX
        self.twrtx_var =        StringVar()

        # Frames
        # Main Frame (Holds all other frames)
        self.frm_00 = Frame(self)
        self.frm_00.config(relief=RIDGE,bd=2)
        self.frm_00.pack(expand=1,fill=BOTH,side=TOP,anchor=N)

        # Menu Frame (Top of main frame)
        self.frm_mnu = Frame(self.frm_00)
        self.frm_mnu.pack(side=TOP,anchor=W)

        # View Data Label Frame
        self.frm_modify_label = Frame(self.frm_00)
        self.frm_modify_label.pack(side=TOP,anchor=N,fill=BOTH)
        
        # Modify Frame
        self.frm_modify = Frame(self.frm_00)
        self.frm_modify.pack(expand=0,fill=BOTH,side=TOP,anchor=N,padx=1,pady=1)

        # Modify Right Frame
        self.frm_modify_right = Frame(self.frm_modify)
        self.frm_modify_right.pack(expand=1,fill=BOTH,side=RIGHT,anchor=N,padx=2,pady=1)

        # Modify Left Frame
        self.frm_modify_left = Frame(self.frm_modify)
        self.frm_modify_left.pack(expand=0,fill=BOTH,side=LEFT,anchor=N,padx=1,pady=0)

        # View Data Label Frame
        self.frm_view_label = Frame(self.frm_00)
        self.frm_view_label.pack(side=TOP,anchor=N,fill=BOTH)
        
        # Entry Frame Parent
        self.frm_entry = Frame(self.frm_modify_right)
        self.frm_entry.pack(expand=1,fill=BOTH,side=TOP,anchor=N,padx=1,pady=1)

        # Entry Frame A
        self.frm_entry_a = Frame(self.frm_entry)
        self.frm_entry_a.pack(expand=1,fill=BOTH,side=TOP,anchor=N)

        # Entry Frame B
        self.frm_entry_b = Frame(self.frm_entry)
        self.frm_entry_b.pack(expand=1,fill=BOTH,side=TOP,anchor=N)

        # Entry Frame C
        self.frm_entry_c = Frame(self.frm_entry)
        self.frm_entry_c.pack(expand=1,fill=BOTH,side=TOP,anchor=N)

        # Category Labels Frame
        self.frm_cat = Frame(self.frm_00,bg='light grey')
        self.frm_cat.pack(side=TOP,anchor=NW,fill=X,expand=0)
        
        # View Frame
        self.frm_view = Frame(self.frm_00,bg='light grey')
        self.frm_view.pack(side=TOP,fill=BOTH,expand=1,anchor=N)

        # View Right Frame
        self.frm_view_right = Frame(self.frm_view,bg='light grey')
        self.frm_view_right.pack(side=LEFT,fill=BOTH,expand=1,anchor=NW)
        
        # Report Frame
        self.frm_report = Frame(self.frm_00)
        self.frm_report.pack(side=TOP,fill=BOTH,expand=1,anchor=N)

        # Button Frame
        self.frm_run = Frame(self.frm_00)
        self.frm_run.pack(side=BOTTOM,fill=X,anchor=S)

        # File Menu
        self.mnu_file_btn = Menubutton(self.frm_mnu,text='File',underline=0,bg='grey')
        self.mnu_file_btn.pack(side=LEFT)
        file = Menu(self.mnu_file_btn, tearoff=0)
        self.mnu_file_btn.config(menu=file)

        # Menu Exit (File)
        file.add_command(label='Quit...',underline=0,command=sys.exit)

        # Tools Menu
        self.mnu_edit_btn = Menubutton(self.frm_mnu,text='Tools',underline=0,bg='grey')
        self.mnu_edit_btn.pack(side=LEFT)
        file = Menu(self.mnu_edit_btn, tearoff=0)
        self.mnu_edit_btn.config(menu=file)

        # New Record (Tools)
        file.add_command(label='New site...',underline=0)

        # Modify (Tools)
        file.add_command(label='Modify site...',underline=0)

        # Remove (Tools)
        file.add_command(label='Remove site...',underline=0)

        # Search jobs (Tools)
        file.add_command(label='Search site...',underline=0)

        # View Menu
        self.mnu_view_btn = Menubutton(self.frm_mnu,text='View',underline=0,bg='grey')
        self.mnu_view_btn.pack(side=LEFT)
        file = Menu(self.mnu_view_btn, tearoff=0)
        self.mnu_view_btn.config(menu=file)

        # Sort (View)
        file.add_command(label='Sort...',underline=0)

        # Menu Help
        self.mnu_help_btn = Menubutton(self.frm_mnu,text='Help',underline=0,bg='grey')
        self.mnu_help_btn.pack(side=LEFT)
        file = Menu(self.mnu_help_btn, tearoff=0)
        self.mnu_help_btn.config(menu=file)

        # About
        file.add_command(label='About...',underline=0)

        # Help
        file.add_command(label='Help...',underline=0)

        # Filler Button (Menu)
        dummy = Menubutton(self.frm_mnu,text=' '*900,bg='grey',state=DISABLED)
        dummy.pack(side=LEFT,fill=X)

        # Widgets

        # Simple Line
        Frame(self.frm_modify_label,bg='BLACK',relief=GROOVE,bd=2,height=2).pack(fill=X,expand=0,pady=0,side=TOP,anchor=NW)
        
        # Modify Label
        Label(self.frm_modify_label,text='--- MODIFY OR ADD DATA ---',fg='blue').pack(side=TOP)

        # Simple Line
        Frame(self.frm_view_label,bg='BLACK',relief=GROOVE,bd=2,height=2).pack(fill=X,expand=0,pady=0,side=TOP,anchor=NW)
        
        # View Data Label
        Label(self.frm_view_label,text='--- VIEW DATA ---',fg='blue').pack()
        
        # Category Labels
        lbl = 'HUB NAME\t\t      JT #\t        HUB MX\t     FIELD MX\t\t\t\t\tTWR TX\tHUB TX\t        SITE NAME'
        self.txt_desc = Text(self.frm_cat,height=1,wrap=NONE)
        self.txt_desc.pack(pady=2,anchor=W,fill=X,expand=1)
        self.txt_desc.insert(END, lbl)
        self.txt_desc.config(state='disabled',font='Arial 9',relief=FLAT,bg='light grey')

        # Scroll Bar (Top Left)
        self.sb_sites = Scrollbar(self.frm_view_right)
        self.sb_sites.pack(side=RIGHT,padx=1,pady=6,fill=Y)

        # Text Widget (Top Left)
        self.txt_sites = Text(self.frm_view_right,height=10,width=100,wrap=NONE)
        self.txt_sites.config(state='normal',yscrollcommand=self.sb_sites.set)
        self.txt_sites.pack(pady=2,fill=BOTH,expand=1,anchor=N)
        self.sb_sites.config(command=self.txt_sites.yview)

        # Label
        Label(self.frm_modify_left,text='LIST OF HUBS').pack(side=TOP)

        # Scroll Bar
        self.hub_scrollbar = Scrollbar(self.frm_modify_left)
        self.hub_scrollbar.pack(side=RIGHT,padx=1,pady=1,fill=Y)

        # Hub Name
        self.lst_hub = Listbox(self.frm_modify_left,height=6,width=14,selectmode=SINGLE)
        self.lst_hub.config(state=DISABLED,yscrollcommand=self.hub_scrollbar.set)
        self.lst_hub.pack(padx=1,pady=1,fill=BOTH,expand=1,anchor=N)
        self.hub_scrollbar.config(command=self.lst_hub.yview)

        # Site Name
        Label(self.frm_entry_a,text='Site Name: ').pack(anchor=NW,padx=2,pady=4,side=LEFT)
        self.ent_name=Entry(self.frm_entry_a,width=22,textvariable=self.sitename_var)
        self.ent_name.config(state=DISABLED)
        self.ent_name.pack(anchor=NW,padx=2,pady=4,side=LEFT,expand=1,fill=X)

        # JT Number
        Label(self.frm_entry_a,text=' JT Number:').pack(anchor=NW,padx=2,pady=4,side=LEFT)
        self.ent_jt=Entry(self.frm_entry_a,width=6,textvariable=self.jt_var)
        self.ent_jt.config(state=DISABLED)
        self.ent_jt.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # Preterm
        Label(self.frm_entry_a,text=' Preterm:').pack(anchor=NW,padx=2,pady=4,side=LEFT)
        self.ent_preterm=Entry(self.frm_entry_a,width=10,textvariable=self.preterm_var)
        self.ent_preterm.config(state=DISABLED)
        self.ent_preterm.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # Port
        Label(self.frm_entry_a,text=' Port:').pack(anchor=NW,padx=2,pady=4,side=LEFT)
        self.ent_port=Entry(self.frm_entry_a,width=5,textvariable=self.port_var)
        self.ent_port.config(state=DISABLED)
        self.ent_port.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # HUB MUX Number
        Label(self.frm_entry_a,text='HUB MUX #:').pack(anchor=NW,padx=2,pady=6,side=LEFT)
        self.ent_hubmuxnum=Entry(self.frm_entry_a,width=6,textvariable=self.hubmuxnum_var)
        self.ent_hubmuxnum.config(state=DISABLED)
        self.ent_hubmuxnum.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # HUB MUX Type
        Label(self.frm_entry_a,text=' HUB MUX Type:').pack(anchor=NW,padx=2,pady=6,side=LEFT)
        self.hubmuxtype_var.set('40')
        self.opt_mnu_hubmuxtype = OptionMenu(self.frm_entry_a,self.hubmuxtype_var, '40','40X')
        self.opt_mnu_hubmuxtype.config(width=6,state=DISABLED)
        self.opt_mnu_hubmuxtype.pack(anchor=NW,padx=1,pady=4,side=LEFT)

        # Field MUX Name
        Label(self.frm_entry_b,text='MUX Name:').pack(anchor=NW,padx=2,pady=6,side=LEFT)
        self.ent_fieldmuxname=Entry(self.frm_entry_b,width=43,textvariable=self.fieldmuxname_var)
        self.ent_fieldmuxname.config(state=DISABLED)
        self.ent_fieldmuxname.pack(anchor=NW,padx=2,pady=4,side=LEFT,expand=0,fill=X)

        # Field MUX Type
        Label(self.frm_entry_b,text=' Field MUX Type:').pack(anchor=NW,padx=2,pady=6,side=LEFT)
        self.fieldmuxtype_var.set('TBD')
        self.opt_mnu_fieldmuxtype = OptionMenu(self.frm_entry_b,self.fieldmuxtype_var, "One","Two","Three")
        self.opt_mnu_fieldmuxtype.config(width=8,state=DISABLED)
        self.opt_mnu_fieldmuxtype.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # Tower Group
        Label(self.frm_entry_b,text=' Tower Group:').pack(anchor=NW,padx=2,pady=6,side=LEFT)
        self.towergroup_var.set('0')
        self.opt_mnu_twrgroup = OptionMenu(self.frm_entry_b,self.towergroup_var, '0','1','2','3','421','422','423')
        self.opt_mnu_twrgroup.config(width=8,state=DISABLED)
        self.opt_mnu_twrgroup.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # HUB TX
        Label(self.frm_entry_b,text=' HUB TX:').pack(anchor=NW,padx=2,pady=4,side=LEFT)
        self.ent_hubtx=Entry(self.frm_entry_b,width=9,textvariable=self.hubtx_var)
        self.ent_hubtx.config(state=DISABLED)
        self.ent_hubtx.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # TWR TX
        Label(self.frm_entry_b,text=' Tower TX:').pack(anchor=NW,padx=2,pady=4,side=LEFT)
        self.ent_twrtx=Entry(self.frm_entry_b,width=10,textvariable=self.twrtx_var)
        self.ent_twrtx.config(state=DISABLED)
        self.ent_twrtx.pack(anchor=NW,padx=2,pady=4,side=LEFT)

        # Apply
        self.btn_go = Button(self.frm_entry_c,text='Apply')
        self.btn_go.pack(side=RIGHT,anchor=W,pady=1,padx=2)
        self.btn_go.config(state=DISABLED)
        Label(self.frm_entry_c,text='Create or modify data, then press apply. ').pack(anchor=W,side=RIGHT)

        # Simple Line
        Frame(self.frm_report,bg='BLACK',relief=GROOVE,bd=2,height=2).pack(fill=X,expand=0,pady=1,side=TOP,anchor=NW)

        # Report Label (Report Frame)
        Label(self.frm_report,text='--- CHANNEL REPORT ---',fg='blue').pack()

        # Scroll Bar (Report Frame)
        self.report_scrollbar = Scrollbar(self.frm_report)
        self.report_scrollbar.pack(side=RIGHT,padx=1,pady=2,fill=Y)

        # Report View (Report Frame)
        self.txt_report = Text(self.frm_report,height=10,width=125)
        self.txt_report.config(state='normal',yscrollcommand=self.report_scrollbar.set)
        self.txt_report.pack(padx=1,pady=1,fill=BOTH,expand=1,anchor=N)
        self.report_scrollbar.config(command=self.txt_report.yview)

        # Report (Report Frame)
        self.btn_report = Button(self.frm_run,text='Run')
        self.btn_report.pack(side=RIGHT,anchor=SE,padx=5,pady=1)

        # Report Label (Run Frame)
        ch_label='Create channel report.'
        Label(self.frm_run,text=ch_label).pack(side=RIGHT,anchor=E)


class Hub:
    """
    Primary or secondary HUB.  Attributes are ...
    - HUB name (from list, eg. "WABU", "WAGL", etc.)
    - HUB type (eg. "PRI", "SEC")
    - List of preterm panels (objects)
    - List of equipment (eg. "JUNIPER", "4200")
    - List of MUXes (objects)
    """

    def __init__(self, hub_name, hub_type, hub_equip):
        """
        Initialize HUB variables with some error checking
        """

        # HUB name with error checking
        if not hub_name in self.hub_lst:
            raise ParamException("Hub name must be a valid HUB.")
        else:
            self._hub_name = hub_name

        # HUB type with error checking
        if not hub_type in self.hub_type_lst:
            raise ParamException("Hub type must be PRI or SEC.")
        else:
            self._hub_type = hub_type

    # Set up decorators
    @property
    def hub_name(self):
        """
        Returns HUB name
        """
        return self._hub_name

    @hub_name.setter
    def hub_name(self, var):
        """
        Set HUB name with error checking
        """
        if var in self.hub_lst:
            self._hub_name = var

    @property
    def hub_type(self):
        """
        Returns HUB type
        """
        return self._hub_type

    @hub_type.setter
    def hub_type(self, var):
        """
        Set HUB type with error checking
        """
        if var in self.hub_type_lst:
            self._hub_type = var


    def add_preterms(self, pre_name):
        self.preterms.append(PreTerm(self.pre_name))


class PreTerm:
    """
    Placeholder
    """
    def __init__(self, pre_name):
        self.pre_name = pre_name

def main():
    # One time use, creates database from csv file record
    # create_db()

    # Call dialog
    root = Tk()
    # Get screen width
    wid = root.winfo_screenwidth()
    # Get screen height
    hgt = root.winfo_screenheight()
    # Dialog is full screen
    root.geometry("%dx%d+0+0" % (wid, hgt))
    # Create instance and run
    ch_app = ChannelTool(root)
    root.mainloop()

# ---------------------------------------------------------------
if __name__ == '__main__':
    main()
