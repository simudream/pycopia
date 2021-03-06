#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

attribUnique_3882054017216351376 = pycopia.XML.POM.XMLAttribute(u'unique', pycopia.XML.POM.Enumeration((u'true', u'false')), 13, u'true')


attribSrc_3443572122774772041 = pycopia.XML.POM.XMLAttribute(u'src', 1, 12, None)


attribStyle_733285237156411536 = pycopia.XML.POM.XMLAttribute(u'style', 1, 12, None)


attribIcon_541823984710737481 = pycopia.XML.POM.XMLAttribute(u'icon', 1, 12, None)


attribName_3839651748354608356 = pycopia.XML.POM.XMLAttribute(u'name', 1, 11, None)


attribTerm_2943920413903779025 = pycopia.XML.POM.XMLAttribute(u'term', pycopia.XML.POM.Enumeration((u'true', u'false')), 13, u'false')


attribVisible_686906346921881956 = pycopia.XML.POM.XMLAttribute(u'visible', pycopia.XML.POM.Enumeration((u'true', u'false')), 13, u'true')


attribType_4574891062544652004 = pycopia.XML.POM.XMLAttribute(u'type', pycopia.XML.POM.Enumeration((u'file', u'system')), 13, u'file')


attribCmd_1694194058866410000 = pycopia.XML.POM.XMLAttribute(u'cmd', 1, 11, None)


attribSnotify_3151943522720133376 = pycopia.XML.POM.XMLAttribute(u'snotify', pycopia.XML.POM.Enumeration((u'true', u'false')), 13, u'false')




#  xfdesktop-menu.dtd defines xfce4 desktop menu files. 


class Xfdesktop_menu(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'xfdesktop-menu'


class Menu(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'visible': attribVisible_686906346921881956, 
         u'name': attribName_3839651748354608356, 
         u'icon': attribIcon_541823984710737481, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	KWATTRIBUTES = {
         'visible': attribVisible_686906346921881956, 
         'name': attribName_3839651748354608356, 
         'icon': attribIcon_541823984710737481, 
         }
	_name = u'menu'


#  name="Name in menu" icon="iconfile" visible="true" 


class App(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'term': attribTerm_2943920413903779025, 
         u'name': attribName_3839651748354608356, 
         u'cmd': attribCmd_1694194058866410000, 
         u'visible': attribVisible_686906346921881956, 
         u'snotify': attribSnotify_3151943522720133376, 
         u'icon': attribIcon_541823984710737481, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	KWATTRIBUTES = {
         'term': attribTerm_2943920413903779025, 
         'name': attribName_3839651748354608356, 
         'cmd': attribCmd_1694194058866410000, 
         'visible': attribVisible_686906346921881956, 
         'snotify': attribSnotify_3151943522720133376, 
         'icon': attribIcon_541823984710737481, 
         }
	_name = u'app'


#  name="Name" cmd="Command to run" term="false" icon="iconfile"  snotify="false" visible="true" 


class Separator(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'visible': attribVisible_686906346921881956, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	KWATTRIBUTES = {
         'visible': attribVisible_686906346921881956, 
         }
	_name = u'separator'


#  visible="true" 


class Include(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'src': attribSrc_3443572122774772041, 
         u'style': attribStyle_733285237156411536, 
         u'unique': attribUnique_3882054017216351376, 
         u'type': attribType_4574891062544652004, 
         u'visible': attribVisible_686906346921881956, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	KWATTRIBUTES = {
         'src': attribSrc_3443572122774772041, 
         'style': attribStyle_733285237156411536, 
         'unique': attribUnique_3882054017216351376, 
         'type': attribType_4574891062544652004, 
         'visible': attribVisible_686906346921881956, 
         }
	_name = u'include'


#  type="file" src="menu2.xml" visible="true" 


#  type="system" style="simple" unique="true" 


class Title(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'visible': attribVisible_686906346921881956, 
         u'name': attribName_3839651748354608356, 
         u'icon': attribIcon_541823984710737481, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	KWATTRIBUTES = {
         'visible': attribVisible_686906346921881956, 
         'name': attribName_3839651748354608356, 
         'icon': attribIcon_541823984710737481, 
         }
	_name = u'title'


#  title name="Name in menu" icon="iconfile" visible="true" 


class Builtin(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'cmd': attribCmd_1694194058866410000, 
         u'name': attribName_3839651748354608356, 
         u'icon': attribIcon_541823984710737481, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	KWATTRIBUTES = {
         'cmd': attribCmd_1694194058866410000, 
         'name': attribName_3839651748354608356, 
         'icon': attribIcon_541823984710737481, 
         }
	_name = u'builtin'


#  name="Quit" cmd="quit" icon="gnome-logout" 


GENERAL_ENTITIES = {}

# Cache for dynamic classes for this dtd.


_CLASSCACHE = {}


