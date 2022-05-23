
import sympy as sym
import PySimpleGUI as sg

table_content = []
layout = [
    [sg.Table(headings = ['Point','distance 1 (km)','distance 2 (km)','Actual Elevation (m)','height (m)', 'Corrected Elevation (m)'], values = table_content, expand_x=True, key = 'table1')],
    [sg.Input(key = 'input1', expand_x = True),sg.Text('distance 1'), sg.Input(key = 'input2', expand_x = True),sg.Text('Actual Elevation'),  sg.Input(key = 'input3', expand_x = True),sg.Text('Total Distance'),sg.Button('Enter',key = 'Enter1'),
     sg.Button('Clear',key = 'Clear1')]

]

window = sg.Window('Path Profiler', layout)

d2var = 0
initial = False

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    
    if event == 'Enter1':

        try:
            if d2var == 0 and float(values['input1']) == 0 and initial == False:
                inchecker = float(values['input1']) - d2var
                print(inchecker)
                if inchecker  == 0:
                   dmax = float(values['input3'])
                   d2 = dmax - float(values['input1'])
                   d2var = float(values['input1'])
                   h1 = (float(values['input1']) * d2)/17
                   CE1 = float(values['input2']) + h1
                   initial = True
                   table_content.append([len(table_content)+1,float(values['input1']), d2 ,float(values['input2']),h1,CE1])
                   window['table1'].update(table_content)
                   window['input3'].update(disabled = True)
            if d2var == 0 and float(values['input1']) != 0 and initial == True:
                in2checker = float(values['input1']) - d2var
                print(in2checker)
                if in2checker  > 0:
                   dmax = float(values['input3'])
                   d2 = dmax - float(values['input1'])
                   d2var = float(values['input1'])
                   h1 = (float(values['input1']) * d2)/17
                   CE1 = float(values['input2']) + h1
                   if d2 > 0:
                        table_content.append([len(table_content)+1,float(values['input1']), d2 ,float(values['input2']),h1,CE1])
                        window['table1'].update(table_content)
                        window['input3'].update(disabled = True)
            if d2var != 0 and float(values['input1']) != 0 and initial == True:
                in2checker = float(values['input1']) - d2var
                print(in2checker)
                if in2checker  > 0:
                   dmax = float(values['input3'])
                   d2 = dmax - float(values['input1'])
                   d2var = float(values['input1'])
                   h1 = (float(values['input1']) * d2)/17
                   CE1 = float(values['input2']) + h1
                   if d2 > 0:
                        table_content.append([len(table_content)+1,float(values['input1']), d2 ,float(values['input2']),h1,CE1])
                        window['table1'].update(table_content)
                        window['input3'].update(disabled = True)


        except ValueError:
            sg.popup('Please Input Some Acceptable Shit')
        



           
window.close()

