import tkinter as tk
import csv
import uuid
import pandas as pd

populationSize = 100000

class App(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.labelCount = tk.Label(self,text ='Qty')
		self.labelCount.grid(row=1,column=1,sticky='W')
		
		self.labelDigits = tk.Label(self,text ='Digits')
		self.labelDigits.grid(row=1,column=2,sticky='W')
		
		self.radioTemplate = tk.IntVar()
		self.count =  tk.IntVar()
		self.entryCount = tk.Entry(self,textvariable=self.count,width=20)
		self.entryCount.grid(row=2,column=1,sticky='E')

		self.digits = tk.IntVar()
		self.entryDigits = tk.Entry(self,textvariable=self.digits,width=10)
		self.entryDigits.grid(row=2,column=2,sticky='E')	

		self.groupRadioTemplate = tk.Radiobutton(self, text=str.center('Click to Populate',50), variable=self.radioTemplate,value=1,indicatoron=0,command=self.click_populate)
		self.groupRadioTemplate.grid(row=3,column=1,columnspan=3)

	def click_populate(self):
		if self.count.get() != 0:
			sampleCount = self.count.get()
			digits = self.digits.get()
			if digits <= 0 or digits > 32:
				digits = 32

			# using pandas
			uuidPopulationList = []
			
			for i in range(populationSize):
				uuidPopulationList.append(str(uuid.uuid4()))
			df_population = pd.DataFrame(data=uuidPopulationList,columns=['uuid'])
			df_population['uuid']=df_population['uuid'].str.replace('-','')

			s_unique=set(df_population['uuid'].str[0:digits])

			df_sample = pd.DataFrame(data=list(s_unique),columns=['uuid'])
			df_sample.index = df_sample.index + 1
			df_sample.index.name = 'seq'
			df_sample[0:sampleCount].to_csv('output.csv',index=True)

			# using CSV modules
			# with open('output.csv','w', newline='') as csvfile:
			# 	writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
			# 	writer.writerow(['seq','uuid'])
			# 	for i in range(count):
			# 		writer.writerow([i+1,uuid.uuid4()])
			
			exit()
		else:
			pass
            

def main():
    application = App(None)
    application.mainloop()

if __name__ == '__main__':
    main()
