# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
# Import render module
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import EmailForm
from django.views import View
from django.template.loader import render_to_string, get_template
from django.utils.translation import activate

#def contact(request, filename=''):
 
   #return render(request,'contact.html') 
activate('es')

class contact(View):
    form_class = EmailForm
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
         form = self.form_class(request.POST, request.FILES)

         if form.is_valid():
             lugar_destino = form.cleaned_data['lugar_destino']  
             lugar_recogida = form.cleaned_data['lugar_recogida']
             fecha_servicio = form.cleaned_data['fecha_servicio']
             cantidad_pasajeros = form.cleaned_data['cantidad_pasajeros']  
             nombre = form.cleaned_data['nombre']
             telefono = form.cleaned_data['telefono']
             if not lugar_destino:
                lugar_destino = 'No esta especificado'
                
             if not lugar_recogida:
                lugar_recogida = 'No esta especificado'  

             if not fecha_servicio:
                fecha_servicio = 'No aplica'
                #cantidad_pasajeros = 'No aplica'
             if not cantidad_pasajeros:
                cantidad_pasajeros = 'No aplica'    
           

                
             empresa = form.cleaned_data['empresa']
             tipo_transporte = form.cleaned_data['tipo_transporte']
             subject = form.cleaned_data['subject']
             mensaje = form.cleaned_data['message']
             sender = 'servicioalcliente@juanthosa.com'
             email = form.cleaned_data['email']
             buzon = form.cleaned_data['tipo_peticion']
             try:
                attach = request.FILES['attach']
             except:
                attach = ''   
             
             #message = form.cleaned_data['message']
             #html_message = html
             if buzon == 'pqr@juanthosa.com':
               req = 'PQR'
             elif buzon == 'solicitudes@juanthosa.com':
               req = 'Solicitud'
             else:
               req = 'error'    
             ctx = {
             'nombre' : nombre,
             'telefono': telefono,
             
              'lugar_destino': lugar_destino,
              'lugar_recogida': lugar_recogida,
            

            
             'empresa': empresa,
             'tipo_transporte': tipo_transporte,
             'subject':subject,
             
             
             'email': email,
             'buzon': req,
             'mensaje': mensaje,
             'fecha_servicio': fecha_servicio,
             'cantidad_pasajeros': cantidad_pasajeros
    }
             message = get_template('email.html').render(ctx)
             if not attach:
                mail = EmailMessage(subject,  message, sender, [buzon])
                mail.content_subtype ="html"
               
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Pronto nos comunicaremos contigo %s'%email})     
             else:

                try:
                    mail = EmailMessage(subject,  message, sender, [buzon])
                    mail.content_subtype ="html"
                    mail.attach(attach.name, attach.read(), attach.content_type)
                    mail.send()
                    return render(request, self.template_name, {'email_form': form, 'error_message': 'Pronto nos comunicaremos contigo %s'%email})
                except:
                    return render(request, self.template_name, {'email_form': form, 'error_message': 'El archivo es demasiado grande o esta corrupto'})

         return render(request, self.template_name, {'email_form': form, 'error_message': 'Error. Intenta de nuevo mas tarde'})


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
         form = self.form_class(request.POST, request.FILES)

         if form.is_valid():
             lugar_destino = form.cleaned_data['lugar_destino']  
             lugar_recogida = form.cleaned_data['lugar_recogida']
             fecha_servicio = form.cleaned_data['fecha_servicio']
             cantidad_pasajeros = form.cleaned_data['cantidad_pasajeros']  
             nombre = form.cleaned_data['nombre']
             telefono = form.cleaned_data['telefono']
             if not lugar_destino:
                lugar_destino = 'No esta especificado'
                
             if not lugar_recogida:
                lugar_recogida = 'No esta especificado'  

             if not fecha_servicio:
                fecha_servicio = 'No aplica'
                #cantidad_pasajeros = 'No aplica'
             if not cantidad_pasajeros:
                cantidad_pasajeros = 'No aplica'    
           

                
             empresa = form.cleaned_data['empresa']
             tipo_transporte = form.cleaned_data['tipo_transporte']
             subject = form.cleaned_data['subject']
             mensaje = form.cleaned_data['message']
             sender = 'servicioalcliente@juanthosa.com'
             email = form.cleaned_data['email']
             buzon = form.cleaned_data['tipo_peticion']
             try:
                attach = request.FILES['attach']
             except:
                attach = ''   
             
             #message = form.cleaned_data['message']
             #html_message = html
             if buzon == 'pqr@juanthosa.com':
               req = 'PQR'
             elif buzon == 'solicitudes@juanthosa.com':
               req = 'Solicitud'
             else:
               req = 'error'    
             ctx = {
             'nombre' : nombre,
             'telefono': telefono,
             
              'lugar_destino': lugar_destino,
              'lugar_recogida': lugar_recogida,
            

            
             'empresa': empresa,
             'tipo_transporte': tipo_transporte,
             'subject':subject,
             
             
             'email': email,
             'buzon': req,
             'mensaje': mensaje,
             'fecha_servicio': fecha_servicio,
             'cantidad_pasajeros': cantidad_pasajeros
    }
             message = get_template('email.html').render(ctx)
             if not attach:
                mail = EmailMessage(subject,  message, sender, [buzon])
                mail.content_subtype ="html"
               
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Pronto nos comunicaremos contigo %s'%email})     
             else:

                try:
                    mail = EmailMessage(subject,  message, sender, [buzon])
                    mail.content_subtype ="html"
                    mail.attach(attach.name, attach.read(), attach.content_type)
                    mail.send()
                    return render(request, self.template_name, {'email_form': form, 'error_message': 'Pronto nos comunicaremos contigo %s'%email})
                except:
                    return render(request, self.template_name, {'email_form': form, 'error_message': 'El archivo es demasiado grande o esta corrupto'})

         return render(request, self.template_name, {'email_form': form, 'error_message': 'Error. Intenta de nuevo mas tarde'})

def home(request):
   return render(request,'index.html')

def login(request):
   return render(request,'404.html')

def about(request, filename=''):
 
   return render(request,'about.html')   
def transportefluv(request, filename=''):
 
   return render(request,'transportefluv.html') 


def transporteterr(request, filename=''):
 
   return render(request,'transporteterr.html') 


def transporteaer(request, filename=''):
 
   return render(request,'transporteaer.html') 

def mision(request, filename=''):
 
   return render(request,'mision.html') 

def vision(request, filename=''):
 
   return render(request,'vision.html')    
def pqrs(request, filename=''):
 
   return render(request,'pqrs.html') 
# Define function to download pdf file using template
def download_pdf_file(request, filename=None):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/Files/' + filename
        print(filepath)
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return redirect(reverse('download_pdf_file', kwargs={'filename': filename}))


def simple_send_mail(request):
    if request.method == 'POST':
        fm = SendMailForm(request.POST or None, request.FILES or None)
        if fm.is_valid():
            subject = fm.cleaned_data['subject']
            message = fm.cleaned_data['msg']
            from_mail = request.user.email
            print(from_mail)
            to_mail = fm.cleaned_data['email_id']
            to_cc = fm.cleaned_data['email_cc']
            to_bcc = fm.cleaned_data['email_bcc']
            print(fm.cleaned_data)
            attach = fm.cleaned_data['attachment']
            if from_mail and to_mail:
                try:
                    mail = EmailMessage(subject=subject, body=message, from_email=from_mail, to=[to_mail], bcc=[to_bcc],
                                        cc=[to_cc]
                                        )
                    mail.attach(attach.name, attach.read(), attach.content_type)
                    mail.send()
                # except Exception as ex:
                except ArithmeticError as aex:
                    print(aex.args)
                    return HttpResponse('Invalid header found')
                return HttpResponseRedirect('/mail/thanks/')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')
    else:
        fm = SendMailForm()
    return render(request, 'mail/send_mail.html', {'fm': fm})        