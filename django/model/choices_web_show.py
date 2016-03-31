数据库:
	选择列表(choices)
	   class Choice(models.Model)
	       input_choice = ((0,'display_name_1'),(1,'display_name_2'))
		   choicetype  = models.IntegerField(choices=input_choice)
	   页面显示:
	       choice = Choice.objects.all()
		   页面显示名称： choice.get_choicetype_display
		   页面显示数值： choice.choicetype