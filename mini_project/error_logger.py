import datetime
import os
class ReportError:
    def __init__(self):
        self.error_dir_name = 'error_logs'
        self.file_name = datetime.datetime.now().strftime("%Y-%m-%d{}").format('_log.txt')
        if not os.path.exists(self.error_dir_name):
            os.makedirs(self.error_dir_name)
    def report_error_log(self,error_raised_file_name, error):
        try:
            error_date_time = str(datetime.datetime.now())+' : '
            with open(self.error_dir_name+'/'+self.file_name, 'a') as error_file:
                error_file.writelines(error_date_time +error_raised_file_name +" : "+ error+'\n')
                # print('Error written in File')
        except Exception as e:
            print(e)