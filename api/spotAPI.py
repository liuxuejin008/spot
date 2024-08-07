import markdown
from flask import Blueprint, render_template

from services.TralineService import TralineService

spots_bp = Blueprint('spots', __name__)

@spots_bp.route('/spot/<traline_id>',methods=['GET'])
def spot(traline_id):
    print("----------------------++++++++++++++++++"+traline_id)
    traline = TralineService.get_traline(traline_id)
    traline_infos = TralineService.traline_info_list(traline_id)
    return render_template('spot.html', traline=traline,traline_infos=traline_infos)