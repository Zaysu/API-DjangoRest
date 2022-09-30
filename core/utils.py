from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse



class PDFGenerator:
    
    def render_to_pdf(self, template_src, context_dict={}):
        template = get_template(template_src)
        html  = template.render(context_dict)
        result = BytesIO()
        
        try:
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        except Exception as e:
            return None