import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os



class EmailNotify():
    def __init__(self, subject, body, input_file):
        self.From = "esubcentre@dhanushinfotech.com"
        #self.To = "santhosh.emmadi@dhanushinfotech.net,srinivas.p@dhanushinfotech.com, prasad.ama@dhanushinfotech.com, dsn.murthy@dhanushinfotech.com, n.venkatesh@dhanushinfotech.com,varun.k@dhanushinfotech.com, murthy.kl@dhanushinfotech.com"
        self.To = "rathnakar.k@dhanushinfotech.net"
        self.subject = subject
        self.body = body
        #self.Cc = "santhosh.emmadi@dhanushinfotech.net,chandra.t@dhanushinfotech.com,krishnachary.b@dhanushinfotech.net, babu.sivagnanam@dhanushinfotech.com, dilip.yenduri@dhanushinfotech.net,narasimharao.b@dhanushinfotech.net,subhash.n@dhanushinfotech.net, hrushikesh.v@dhanushinfotech.net,naveena.d@dhanushinfotech.net,rathnakar.k@dhanushinfotech.net, shashikanth.g@dhanushinfotech.net, esubcentre@dhanushinfotech.com, Mohd.Qasim@dhanushinfotech.net,aditya.v@dhanushinfotech.net, manjunath.b@dhanushinfotech.net, nagendra.korada@dhanushinfotech.net,arun.k@dhanushinfotech.net, Madhavaramu.n@dhanushinfotech.net"
        self.Cc = "santhosh.emmadi@dhanushinfotech.net"
        self.input_file = input_file
        self.send_email_alert()

    def send_email_alert(self):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.From
            msg['To'] = self.To
            msg['Subject'] = self.subject
            if self.input_file:
                with open(self.input_file, "rb") as fil: 
                    basename = os.path.basename(self.input_file)
                    ext = self.input_file.split('.')[-1:]
                    attachedfile = MIMEApplication(fil.read(), _subtype = ext)
                    attachedfile.add_header(
                        'content-disposition', 'attachment', filename=basename )
                msg.attach(attachedfile)
            msg.attach(MIMEText(self.body, 'html'))
            mail_server = smtplib.SMTP('smtp.diplemailsrvr.com', 587)
            mail_server.starttls()
            mail_server.login("smtpmail@dhanushinfotech.net", "239#@ER%^FDds")            
            mail_server.sendmail(self.From, self.To.split(",") + self.Cc.split(","),msg.as_string())
            mail_server.quit()
        except Exception as e:
            traceback.print_exc()
            pass
        pass
