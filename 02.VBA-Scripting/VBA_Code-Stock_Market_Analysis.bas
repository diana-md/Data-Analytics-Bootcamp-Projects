Attribute VB_Name = "Module2"

'This function takes a worksheet(ws), a row number (i) of the big table, a row number of the new table where new data 
'needs to pe added (x) and the value of the stock at the beginning of the year (open_value). It calculates and adds values
'to the Yearly Change and Percent Change columns.
Sub write_to_cell(ws, i, x, open_value)
    'Calculate and format Yearly Change Value
    yearly_change = ws.Cells(i, 6).Value - open_value
    ws.Cells(i, 6).NumberFormat = "0.000000000"
    ws.Cells(x, 10).Value = yearly_change
    If yearly_change < 0 Then
        ws.Cells(x, 10).Interior.ColorIndex = 3
    Else
        ws.Cells(x, 10).Interior.ColorIndex = 4
    End If
    'Calculate and format Percent Change Value
    If open_value = 0 Then
        If yearly_change = 0 Then
            ws.Cells(x, 11).Value = 0
        Else
            ws.Cells(x, 11).Value = 1
        End If
    Else
        ws.Cells(x, 11).Value = yearly_change / open_value
    End If
    ws.Cells(x, 11).NumberFormat = "0.00%"

End Sub

'getStockVolume() function loops through each of the Worksheets, sets new column names on each sheet and 
'loops through each of the rows keeping track of the ticker value and total in the previous rows. 
Sub getStockVolume()
    
    Dim i As Long
    Dim last_row As Long
    Dim current_ticker As String
    Dim current_total As Double
    Dim current_open As Double
    Dim yearly_change As Double
    
    'Variable x keeps track of the row number on the table in the right that contains the summary of the stock
    Dim x As Integer
    Dim ws As Worksheet
    
    For Each ws In Worksheets
    
        'Define Column Titles
        ws.Range("I1").Value = "Ticker"
        ws.Range("J1").Value = "Yearly Change"
        ws.Range("K1").Value = "Percent Change"
        ws.Range("L1").Value = "Total Stock Volume"
        ws.Range("P1").Value = "Ticker"
        ws.Range("Q1").Value = "Value"
        ws.Range("O2").Value = "Greatest % Increase"
        ws.Range("O3").Value = "Greatest % Decrease"
        ws.Range("O4").Value = "Greatest Total Volume"
        
        x = 2
        last_row = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
        current_ticker = ws.Cells(2, 1).Value
        current_total = ws.Cells(2, 7).Value
        current_open = ws.Cells(2, 3).Value
        
        Dim start_row As Integer
        If ws.Cells(3, 1).Value <> ws.Cells(2, 1).Value Then
            ws.Cells(2, 9).Value = current_ticker
            Call write_to_cell(ws, 2, 2, current_open)
            ws.Cells(2, 12).Value = current_total
            x = 3
            start_row = 4
        Else
            start_row = 3
        End If
        
        For i = start_row To last_row + 1
            If ws.Cells(i, 1).Value = current_ticker Then
            'If the ticker in this row is the same with the ticker in the previous row, add value to the total
                current_total = current_total + ws.Cells(i, 7)
            Else
            'If the ticker in this row is different than the ticker in the previous row, add a new row to the summary table 
                ws.Cells(x, 9).Value = current_ticker
                Call write_to_cell(ws, i - 1, x, current_open)
                ws.Cells(x, 12).Value = current_total
                current_open = ws.Cells(i, 3).Value
                current_ticker = ws.Cells(i, 1).Value
                current_total = ws.Cells(i, 7).Value
                x = x + 1
            End If
        Next i
        
        'Calulate the Greatest % Increase & Decrease and Greatest Total Volume
        Dim max_increase As Double
        Dim max_increase_ticker As String
        Dim min_decrease As Double
        Dim min_decrease_ticker As String
        Dim max_total As Double
        Dim max_total_ticker As String
        
        max_increase = ws.Range("K2").Value
        max_increase_ticker = ws.Range("I2").Value
        min_decrease = ws.Range("K2").Value
        min_decrease_ticker = ws.Range("I2").Value
        max_total = ws.Range("L2").Value
        max_total_ticker = ws.Range("I2").Value
        
        For i = 3 To x + 1
            If ws.Cells(i, 11).Value > max_increase Then
                max_increase = ws.Cells(i, 11).Value
                max_increase_ticker = ws.Cells(i, 9).Value
            End If
            If ws.Cells(i, 11).Value < min_decrease Then
                min_decrease = ws.Cells(i, 11).Value
                min_decrease_ticker = ws.Cells(i, 9).Value
            End If
            If ws.Cells(i, 12).Value > max_total Then
                max_total = ws.Cells(i, 12).Value
                max_total_ticker = ws.Cells(i, 9).Value
            End If
        Next i
        
        ws.Range("Q2").Value = max_increase
        ws.Range("Q3").Value = min_decrease
        ws.Range("Q4").Value = max_total
        ws.Range("P2").Value = max_increase_ticker
        ws.Range("P3").Value = min_decrease_ticker
        ws.Range("P4").Value = max_total_ticker
        ws.Range("Q2:Q3").NumberFormat = "0.00%"
        ws.Range("Q4").NumberFormat = "0"
        ws.Columns("O:O").EntireColumn.AutoFit
    Next ws

End Sub

