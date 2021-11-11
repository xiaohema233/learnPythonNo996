	Sub 生成日报()
	Dim i As Integer
	Dim sht As Worksheet
	For i = 1 To 30
	Set sht = Sheets.Add
	sht.Name = "6月" & i & "日"
	Sheets("模板").Range("A1:B15").Copy sht.Range("A1")
	Next i
	End Sub
