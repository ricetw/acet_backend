from flask import Blueprint
from .views import *

web_bp = Blueprint('web', __name__, template_folder='templates')

web_bp.add_url_rule('/login', view_func=Login.as_view('login'), methods=['POST'])
web_bp.add_url_rule('/getpermissions', view_func=GetPermission.as_view('getpermission'), methods=['GET'])
web_bp.add_url_rule('/index', view_func=Index.as_view('index'), methods=['GET'])
web_bp.add_url_rule('/personnel', view_func=Personnel.as_view('personnel'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/personnel/detail', view_func=PersonnelDetail.as_view('personneldetail'), methods=['POST'])
web_bp.add_url_rule('/personnel/add', view_func=PersonnelAdd.as_view('personneladd'), methods=['POST'])
web_bp.add_url_rule('/medications', view_func=Medicine.as_view('medicine'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/medications/detail', view_func=MedicationsDetail.as_view('medicationsdetail'), methods=['GET', 'POST'])
web_bp.add_url_rule('/medications/add', view_func=MedicationsAdd.as_view('medicationsadd'), methods=['GET', 'POST'])
web_bp.add_url_rule('/patients', view_func=PatientURL.as_view('patient'), methods=['GET', 'POST', 'PUT'])
web_bp.add_url_rule('/patient/add', view_func=PatientAdd.as_view('patientadd'), methods=['POST'])
web_bp.add_url_rule('/patient/<string:id>', view_func=PatientMedicalRecord.as_view('patientmedicalrecord'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/medical_record/<string:id>/add', view_func=AddMedicalRecord.as_view('addmedicalrecord'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/medical_records', view_func=MedicalRecord.as_view('medicalrecords'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/medical_record/<string:pid>&<int:mid>', view_func=ViewMedicalRecord.as_view('viewmedicalrecord'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/ward', view_func=WardBed.as_view('ward'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/database', view_func=Database.as_view('database'), methods=['GET', 'POST', 'PUT', 'DELETE'])
web_bp.add_url_rule('/settings', view_func=Setting.as_view('setting'), methods=['GET', 'POST', 'PUT', 'DELETE'])
