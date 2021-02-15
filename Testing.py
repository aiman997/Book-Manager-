 # SET @textEnglish = N'(insert your Arabic text here)'
 # @name nvarchar ( 50 ); set @name = N 'محسن' ; insert into tests values ( @name) Permalink

 # CREATE TABLE Books ( col1 VARCHAR(100) COLLATE Latin1_General_100_CI_AI, col2 VARCHAR(100) COLLATE Arabic_CI_AI_KS_WS, col3 NVARCHAR(100) ) INSERT INTO Books VALUES(N'لا أتكلم العربية',N'لا أتكلم العربية',N'لا أتكلم العربية')
txt = u'Arabic (\u0627\u0644\u0637\u064a\u0631\u0627\u0646)'
print(txt)
