#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import Tkinter
import collections
from textwrap import fill
from time import gmtime, strftime
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

class App:

    def __init__(self, master):
        #self.controller = controller
        self.listLabelID = []
        self.listButtonsActions = {}
        self.tableRule = []
        self.filterOptions = {}#self.controller.list_filters()
        self.optionsDropDownVNF = ["Estatistica","DPI"]#self.controller.list_vnf()
        self.optionsDropDownProtocol = ["Ethernet", "ARP"]#self.controller.list_protocols()
        self.addedID = 0
        self.chosenVNF = ''
        self.chosenProtocol = ''
        self.master = master
        self.window_width = 797
        self.window_height = 314
        self.list_vnfs = ["Estatistica","DPI"]#deletar

        labels = []
        entries = []

        self.initialize_program(master)

    def initialize_program(self, master):
        master.geometry(str(self.window_width)+"x"+str(self.window_height))

        self.Frame = Frame(master)
        self.Frame.pack(fill=BOTH, side=LEFT, expand=TRUE)

        #///////////////////VIEW VNFS///////////////////////////
        self.subFrame1 = Frame(self.Frame)
        self.subFrame1.pack(fill=X, side=TOP)

        view_vnfs = Button(self.subFrame1, fg='blue', text="Show VNFs", command=lambda master=master: self.show_vnfs(master))
        view_vnfs.pack(side=RIGHT)

        #///////////////////VNF///////////////////////////
        self.subFrame2 = Frame(self.Frame,bd=1, relief=GROOVE)
        self.subFrame2.pack(fill=BOTH, side=TOP, expand=TRUE)

        self.subFrame21 = Frame(self.subFrame2, width=(self.subFrame2.winfo_width()/2))
        self.subFrame21.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame22 = Frame(self.subFrame2, width=(self.subFrame2.winfo_width()/2))
        self.subFrame22.pack(fill=BOTH, side=LEFT, expand=TRUE)

        label_vnf = Label(self.subFrame21, text="Choose VNF to Instantiate:")
        label_vnf.pack(side=RIGHT)

        self.vnf_var = StringVar()
        self.vnf_var.set('Select VNF')
        self.vnf_dropdown = OptionMenu(self.subFrame22, self.vnf_var, *self.optionsDropDownVNF, command=lambda event: self.optionMenuPressed(event))
        self.vnf_dropdown.pack(side=LEFT)
        self.vnf_dropdown.config(width=20)

        #///////////////////SOURCE IP///////////////////////////
        self.subFrame3 = Frame(self.Frame)
        self.subFrame3.pack(fill=BOTH, expand=TRUE)

        self.subFrame31 = Frame(self.subFrame3, width=(self.subFrame3.winfo_width()/2),bd=1, relief=GROOVE)
        self.subFrame31.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame311 = Frame(self.subFrame31, width=(self.subFrame31.winfo_width()/2))
        self.subFrame311.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame312 = Frame(self.subFrame31, width=(self.subFrame31.winfo_width()/2))
        self.subFrame312.pack(fill=BOTH, side=LEFT, expand=TRUE)

        label_srcip = Label(self.subFrame311, text="Source IP:")
        label_srcip.pack(side=RIGHT)

        self.srcip_var = StringVar()
        self.srcip_var.set('ex: 10.0.0.1')
        self.entry_srcip = Entry(self.subFrame312, textvariable=self.srcip_var)
        self.entry_srcip.pack(side=RIGHT)
        self.entry_srcip.bind("<Button-1>", lambda event: self.clear_placeholder_srcip(event))

        #///////////////////DESTINATION IP///////////////////////////
        self.subFrame32 = Frame(self.subFrame3, width=(self.subFrame3.winfo_width()/2),bd=1, relief=GROOVE)
        self.subFrame32.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame321 = Frame(self.subFrame32, width=(self.subFrame32.winfo_width()/2))
        self.subFrame321.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame322 = Frame(self.subFrame32, width=(self.subFrame32.winfo_width()/2))
        self.subFrame322.pack(fill=BOTH, side=LEFT, expand=TRUE)

        label_dstip = Label(self.subFrame321, text="Destination IP:")
        label_dstip.pack(side=RIGHT)

        self.dstip_var = StringVar()
        self.dstip_var.set('ex: 10.0.0.2')
        self.entry_dstip = Entry(self.subFrame322, textvariable=self.dstip_var)
        self.entry_dstip.pack(side=RIGHT)
        self.entry_dstip.bind("<Button-1>", lambda event: self.clear_placeholder_dstip(event))

        #///////////////////SOURCE PORT///////////////////////////
        self.subFrame4 = Frame(self.Frame)
        self.subFrame4.pack(fill=BOTH, expand=TRUE)

        self.subFrame41 = Frame(self.subFrame4, width=(self.subFrame4.winfo_width()/2),bd=1, relief=GROOVE)
        self.subFrame41.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame411 = Frame(self.subFrame41, width=(self.subFrame41.winfo_width()/2))
        self.subFrame411.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame412 = Frame(self.subFrame41, width=(self.subFrame41.winfo_width()/2))
        self.subFrame412.pack(fill=BOTH, side=LEFT, expand=TRUE)

        label_srcp = Label(self.subFrame411, text="Source Port:")
        label_srcp.pack(side=RIGHT)

        self.srcp_var = StringVar()
        self.srcp_var.set('ex: 57332')
        self.entry_srcp = Entry(self.subFrame412, textvariable=self.srcp_var)
        self.entry_srcp.pack(side=RIGHT)
        self.entry_srcp.bind("<Button-1>", lambda event: self.clear_placeholder_srcp(event))

        #///////////////////DESTINATION PORT///////////////////////////
        self.subFrame42 = Frame(self.subFrame4, width=(self.subFrame4.winfo_width()/2),bd=1, relief=GROOVE)
        self.subFrame42.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame421 = Frame(self.subFrame42, width=(self.subFrame42.winfo_width()/2))
        self.subFrame421.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame422 = Frame(self.subFrame42, width=(self.subFrame42.winfo_width()/2))
        self.subFrame422.pack(fill=BOTH, side=LEFT, expand=TRUE)

        label_dstp = Label(self.subFrame421, text="Destination Port:")
        label_dstp.pack(side=RIGHT)

        self.dstp_var = StringVar()
        self.dstp_var.set('ex: 80')
        self.entry_dstp = Entry(self.subFrame422, textvariable=self.dstp_var)
        self.entry_dstp.pack(side=RIGHT)
        self.entry_dstp.bind("<Button-1>", lambda event: self.clear_placeholder_dstp(event))

        #///////////////////PROTOCOL///////////////////////////
        self.subFrame5 = Frame(self.Frame,bd=1, relief=GROOVE)
        self.subFrame5.pack(fill=BOTH, expand=TRUE)

        self.subFrame51 = Frame(self.subFrame5, width=(self.subFrame2.winfo_width()/2))
        self.subFrame51.pack(fill=BOTH, side=LEFT, expand=TRUE)

        self.subFrame52 = Frame(self.subFrame5, width=(self.subFrame2.winfo_width()/2))
        self.subFrame52.pack(fill=BOTH, side=LEFT, expand=TRUE)

        label_prot = Label(self.subFrame51, text="Protocol:")
        label_prot.pack(side=RIGHT)

        self.prot_var = StringVar()
        self.prot_var.set('Select Protocol')
        self.entry_prot = OptionMenu(self.subFrame52, self.prot_var, *self.optionsDropDownProtocol, command=lambda event: self.optionMenuPressedProtocol(event))
        self.entry_prot.pack(side=LEFT)

        #///////////////////MESSAGE///////////////////////////
        self.subFrame6 = Frame(self.Frame)
        self.subFrame6.pack(fill=BOTH, expand=TRUE)

        self.message = StringVar()
        self.message.set(" ")
        self.label_message = Label(self.subFrame6, textvariable=self.message, fg='green')
        self.label_message.pack()

        #///////////////////SAVE BUTTON///////////////////////////
        self.subFrame7 = Frame(self.Frame,bd=1, relief=GROOVE)  
        self.subFrame7.pack(fill=BOTH, side=BOTTOM)

        self.saveButton = Button(self.subFrame7, text="Save/Instantiate", width=15, command= self.save_vnf, fg='green')
        self.saveButton.pack(side=RIGHT)

        #///////////////////CANCEL BUTTON///////////////////////////
        cancelButton = Button(self.subFrame7, text="Exit", width=10, command=lambda master=master: self.quit_program(master), fg='red')
        cancelButton.pack(side=LEFT)

        self.Frame2 = Frame(master, bd=1, relief=SUNKEN)
        self.Frame2.pack(fill=BOTH, side=LEFT)

        #self.label_logo = Label(self.Frame2, text="LOGO")
        #self.label_logo.grid(column=0, row=0, pady=3, padx=3)
        img = ImageTk.PhotoImage(Image.open("Drawing.png"))
        panel = Label(self.Frame2, image = img)
        panel.image = img
        panel.pack(side=TOP, fill=X)

        FrameCopyRight = Frame(self.Frame2)
        FrameCopyRight.pack(fill=BOTH, side=BOTTOM)

        text="Copyright © 2016 Giovanni & Lucas"
        self.label_copyright = Label(FrameCopyRight, text=text)
        self.label_copyright.pack(side=TOP, fill=X)

        text2="Coordinators Elias Duarte & Rogerio Turchetti"
        self.label_copyright = Label(FrameCopyRight, text=text2)
        self.label_copyright.pack(side=TOP, fill=X)

        text3='Last updated: '
        text3 += strftime("%d %b %Y %H:%M:%S", gmtime())
        self.label_last_updated = Label(FrameCopyRight, text=text3)
        self.label_last_updated.pack(side=TOP, fill=X)

        master.update_idletasks()
        w = master.winfo_screenwidth()
        h = master.winfo_screenheight()
        size = tuple(int(_) for _ in master.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        master.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.vnf_dropdown.focus()

    def quit_program(self, master):
        #self.controller.stop_network()
        self.master.destroy()

    def clear_placeholder_srcip(self, event):
        self.srcip_var.set('')
        self.message.set(" ")

    def clear_placeholder_dstip(self, event):
        self.dstip_var.set('')
        self.message.set(" ")

    def clear_placeholder_srcp(self, event):
        self.srcp_var.set('')
        self.message.set(" ")

    def clear_placeholder_dstp(self, event):
        self.dstp_var.set('')
        self.message.set(" ")

    def quitWindow(self, window):
        window.destroy()

    def optionMenuPressed(self, event):
        self.message.set(" ")
        self.chosenVNF = event

    def optionMenuPressedProtocol(self, event):
        self.message.set(" ")
        self.chosenProtocol = event

    def save_vnf(self):
        if(len(self.chosenVNF)>0):
            rule = {}
            rule['_id'] = self.addedID
            rule['vnf'] = self.chosenVNF
            if self.chosenProtocol:
                rule['Protocol'] = self.chosenProtocol
            if(len(self.srcip_var.get())>0):
                if(self.srcip_var.get().split()[0] != 'ex:'):
                    rule['Source IP'] = self.srcip_var.get()
            if(len(self.dstip_var.get())>0):
                if(self.dstip_var.get().split()[0] != 'ex:'):
                    rule['Destination IP'] = self.dstip_var.get()
            if(len(self.srcp_var.get())>0):
                if(self.srcp_var.get().split()[0] != 'ex:'):
                    rule['Source Port'] = self.srcp_var.get()
            if(len(self.dstp_var.get())>0):
                if(self.dstp_var.get().split()[0] != 'ex:'):
                    rule['Destination Port'] = self.dstp_var.get()

            self.chosenVNF = ''

            self.addedID += 1
            self.vnf_var.set('Select VNF')
            self.prot_var.set('Select Protocol')
            self.srcip_var.set('')
            self.dstip_var.set('')
            self.srcp_var.set('')
            self.dstp_var.set('')
            self.message.set("Your new VNF was created successfully!")
            self.label_message.config(fg='green')
            self.srcip_var.set('ex: 10.0.0.1')
            self.dstip_var.set('ex: 10.0.0.2')
            self.srcp_var.set('ex: 57332')
            self.dstp_var.set('ex: 80')
            self.chosenProtocol = ''
            self.tableRule.append(rule)
            #self.controller.insert_rule(rule)
            self.vnf_dropdown.focus()
        else:
            self.message.set("VNF must be chosen!")
            self.label_message.config(fg='red')

    def show_vnfs(self, master):
        self.label_id = []
        self.label = []
        self.delete_vnf = []
        self.show_stats = []
        self.frames = []
        self.frames_bckup = []
        #self.tableRule = self.controller.get_rules()

        #Deleting inicial frame
        self.quitWindow(self.Frame)
        self.quitWindow(self.Frame2)

        #Building secondary frame
        self.frameBtn = Frame(master, bd=2, relief=GROOVE)
        self.frameBtn.pack(fill=X, side=TOP)

        labelid = Label(self.frameBtn, text="  ")
        labelid.pack(side=LEFT, padx=5, pady=5)

        label = Label(self.frameBtn, text="Instantiated VNF's")
        label.pack(side=LEFT, padx=5, pady=5)
        label.config(font=("Helvetica", 13))

        add_new_vnf = Button(self.frameBtn, text="Back/Add New VNF", fg='green', width=15, command=lambda master=master: self.add_new_vnf_func(master))
        add_new_vnf.pack(side=RIGHT, padx=5, pady=5)

        #-----------------------------------------------------------------------------------------------------------------------------------------
        self.frameVNFs = Frame(master, bd=2, relief=GROOVE)
        self.frameVNFs.pack(fill=X, side=TOP)

        label = Label(self.frameVNFs, text='VNFs: ')
        label.grid(column=0, row=0, padx=5, pady=5)
        label.config(font=("Helvetica", 10))


        if self.tableRule:
            list_vnfs = self.list_vnfs #self.controller.active_vnfs
            self.label_vnf = []

            wwidth = 0
            column = 1
            row = 0
            count = 0
            for elem in list_vnfs:
                if(column==5):
                    column = 0
                    row+=1
                self.label_vnf.append(Label(self.frameVNFs, text=elem, bd=1, relief=GROOVE))
                self.label_vnf[count].grid(column=column, row=row, padx=5, pady=5)
                self.label_vnf[count].config(font=("Helvetica", 10), bg='#66CCFF', fg='black')
                column+=1
                count+=1

            #-----------------------------------------------------------------------------------------------------------------
            wwidth = 0
            #Canvas
            self.canvas = Canvas(master)
            self.canvas.pack(expand=TRUE, fill=BOTH, side=LEFT)

            #ScrollBar
            self.yscrollbar = Scrollbar(master, orient='vertical')
            self.yscrollbar.pack(fill=Y, side=RIGHT)

            #Config
            self.yscrollbar.configure(command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.yscrollbar.set)

            self.FrameRules = Frame(self.canvas)
            self.FrameRules.pack(expand=TRUE, fill=BOTH, side=TOP)

            count = 0
            text = str()
            for elem in self.tableRule:
                text += 'VNF: '+elem['vnf']+' '
                for ind in elem:
                    if(ind != 'vnf' and ind != '_id'):
                        text += ' | ' + ind + ': ' + str(elem[ind])
                self.frames.append(Frame(self.FrameRules, bd=2, relief=GROOVE))
                self.frames[count].pack(expand=TRUE, fill=X, side=TOP)

                self.frames_bckup.append(self.frames[count])

                if(wwidth < len(text)):
                    wwidth += len(text)

                self.label_id.append(Label(self.frames[count], text=elem['_id']))
                self.label_id[count].pack(side=LEFT, padx=5, pady=5)

                self.label.append(Label(self.frames[count], text=text))
                self.label[count].pack(side=LEFT, padx=5, pady=5)

                self.delete_vnf.append(Button(self.frames[count], text="Stop/Delete", fg='red', width=15, command=lambda line=count: self.delete_vnf_func(line)))
                self.delete_vnf[count].pack(side=RIGHT, padx=5, pady=5)

                self.show_stats.append(Button(self.frames[count], fg='orange', text="Show Stats", width=15, command=lambda _id=elem['_id']: self.show_results(_id)))
                self.show_stats[count].pack(side= RIGHT, padx=5, pady=5)

                count += 1
                text=''

            wwidth += 90
            wwidth *= 5
            self.master.geometry(str(wwidth)+"x"+str(self.master.winfo_height()))
            self.CFrame = self.canvas.create_window((0, 0), window = self.FrameRules, anchor = N+W)
            self.canvas.bind("<Configure>", lambda event: self.resize_frame(event))
            self.FrameRules.bind("<Configure>", lambda event: self.scrollevent(event))
        else:
            self.canvas = Canvas(master)
            self.yscrollbar = Scrollbar(master, orient='vertical')

            padding = ' '*40

            label = Label(self.frameVNFs, text="No VNF instantiated!" + padding)
            label.grid(column=1, row=0, padx=5, pady=5)
            label.config(font=("Helvetica", 10), fg='red')

            self.FrameRules = Frame(master, width = 1000)
            self.FrameRules.pack(expand=TRUE, fill=BOTH, side=TOP)

            label = Label(self.FrameRules, text='No VNFs instantiated untill the moment!')
            label.pack(padx=5, pady=5)
            label.config(font=("Helvetica", 10), fg="red")

    def resize_frame(self, e):
        self.canvas.itemconfig(self.CFrame, width = e.width)

    def scrollevent(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def delete_vnf_func(self, line):

        exists = False
        for i in range(line+1, len(self.tableRule)):
            self.delete_vnf[i].config(command=lambda line=i-1: self.delete_vnf_func(line))
        rule = self.tableRule.pop(line)
        #self.controller.delete_rule(rule)
        self.frames[line].destroy()
        self.label_id[line].destroy()
        self.label[line].destroy()
        self.delete_vnf[line].destroy()
        self.show_stats[line].destroy()
        self.frames.pop(line)
        self.label_id.pop(line)
        self.label.pop(line)
        self.delete_vnf.pop(line)
        self.show_stats.pop(line)
        if len(self.tableRule):
            for elem in self.tableRule:
                if elem['vnf'] == rule['vnf']:
                    exists = True

        if not exists:
            count = 0
            for elem in self.label_vnf:
                if elem.cget('text') == rule['vnf']:
                    self.label_vnf[count].destroy()
                    self.label_vnf.pop(count)
                count+=1

    def add_new_vnf_func(self, master):
        self.quitWindow(self.canvas)
        self.quitWindow(self.yscrollbar)
        self.quitWindow(self.frameBtn)
        self.quitWindow(self.FrameRules)
        self.quitWindow(self.frameVNFs)
        self.initialize_program(master)

    def show_results(self, _id):
        listPkts = [50,70,100,120,200,300,500]
        listBytes = [200,500,1500,2000,3000,5000]

        self.WindowResults = Toplevel(self.frameBtn, width=500, height=200)
        self.WindowResults.wm_title("Statistics")
        self.WindowResults.update_idletasks()
        w = self.WindowResults.winfo_screenwidth()
        h = self.WindowResults.winfo_screenheight()
        size = tuple(int(_) for _ in self.WindowResults.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.WindowResults.geometry("%dx%d+%d+%d" % (size + (x, y)))

        widthSubFrames = self.WindowResults.winfo_width()

        FrameResults = Frame(self.WindowResults, width=widthSubFrames)
        FrameResults.pack(side=TOP, expand=TRUE, fill=BOTH)

        #Label Top
        FrameTop = Frame(FrameResults, width=widthSubFrames)
        FrameTop.pack(side=TOP, expand=TRUE, fill=BOTH)

        labelTop = Label(FrameTop, text="Statistics Results for 'rule'")
        labelTop.pack()
        labelTop.config(font=("Helvetica", 15))

        #Frame Results Labels Graphs
        FrameEncapsulate = Frame(FrameResults)
        FrameEncapsulate.pack(side=TOP, expand=TRUE, fill=BOTH)

        #Frame Labels
        FrameLabels = Frame(FrameEncapsulate)
        FrameLabels.pack(expand=TRUE, fill=BOTH,side=LEFT)

        #Frame Buttons Graphs
        FrameButtonGraphs = Frame(FrameEncapsulate)
        FrameButtonGraphs.pack(expand=TRUE, fill=BOTH, side=LEFT)

        #SubFrame Labels
        subFrameLabels1 = Frame(FrameLabels, width=(widthSubFrames/3)*2)
        subFrameLabels1.pack(fill=Y, side=TOP, expand=TRUE)

        subFrameBytes2 = Frame(FrameLabels, width=(widthSubFrames/3)*2)
        subFrameBytes2.pack(fill=Y, side=TOP, expand=TRUE)

        #SubFrame Buttons Graphs
        subFrameGraph1 = Frame(FrameButtonGraphs, width=(widthSubFrames/3))
        subFrameGraph1.pack(fill=Y, side=TOP, expand=TRUE)

        subFrameGraph2 = Frame(FrameButtonGraphs, width=(widthSubFrames/3))
        subFrameGraph2.pack(fill=Y, side=TOP, expand=TRUE)

        #Label Results Number Packets
        labelNumberPkts = Label(subFrameLabels1, text="Number of Packets: ")
        labelNumberPkts.pack(side=RIGHT)

        #Button Graph Results Number Packets
        buttonNumberPkts = Button(subFrameBytes2, text="Graph", fg='yellow', command= lambda results=listPkts, l="Number Packets": self.show_graph(results, l))
        buttonNumberPkts.pack(side=RIGHT)

        #Label Results Number Bytes
        labelNumberBytes = Label(subFrameGraph1, text="Total Size of all Packets: ")
        labelNumberBytes.pack(side=RIGHT)

        #Button Graph Results Number Bytes
        buttonGraphBytes = Button(subFrameGraph2, text="Graph", fg='yellow', command= lambda results=listBytes, l="Number Bytes": self.show_graph(results, l))
        buttonGraphBytes.pack(side=RIGHT)

        FrameButton = Frame(FrameResults)
        FrameButton.pack(fill=BOTH)

        buttonRefresh = Button(FrameButton, text="Refresh", fg='green', command=self.refresh_results)
        buttonRefresh.pack(side=LEFT)

    def refresh_results(self):
        print "refreshing"

    def show_graph(self, results, label):
        time = []
        count = 1
        for elem in results:
            time.append(30*count)
            count = count + 1

        plt.bar(time, results)
        plt.xlabel('Time (sec)')
        plt.ylabel(label)
        plt.title('Statistics Results for '+label)
        plt.grid(True)
        plt.show()

        # WindowGraphs = Toplevel(self.WindowResults)

        # FrameGraphs = Frame(WindowGraphs)
        # FrameGraphs.pack(side=TOP, expand=TRUE, fill=BOTH)

        # img = ImageTk.PhotoImage(Image.open(plt))
        # panel = Label(FrameGraphs, image = img)
        # panel.image = img
        # panel.pack(side=TOP, fill=X)

root = Tk()

def on_closing():
    #self.controller.stop_network()
    root.destroy()

root.wm_title("OnTheFly VNF")

app = App(root)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()